from imutils import build_montages
from datetime import datetime
import numpy as np
import imagezmq
import argparse
import imutils
import cv2
import random
import time
import threading
from threading import Thread

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=True,
	help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True,
	help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.2,
	help="minimum probability to filter weak detections")
ap.add_argument("-mW", "--montageW", required=True, type=int,
	help="montage frame width")
ap.add_argument("-mH", "--montageH", required=True, type=int,
	help="montage frame height")
args = vars(ap.parse_args())



max_car_detect = 10
min_car_detect = 1
min_green = 5
max_green = 12

open_akhir = True
open_awal = True  

state_a = True
state_b = False
state_c = False
state_d = False

imageHub = imagezmq.ImageHub()
# initialize the list of class labels MobileNet SSD was trained to
# detect, then generate a set of bounding box colors for each class
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
# load our serialized model from disk
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

# initialize the consider set (class labels we care about and want
# to count), the object count dictionary, and the frame  dictionary
CONSIDER = set(["car"])
objCount = {obj: 0 for obj in CONSIDER}
frameDict = {}
# initialize the dictionary which will contain  information regarding
# when a device was last active, then store the last time the check
# was made was now
lastActive = {}
lastActiveCheck = datetime.now()
# stores the estimated number of Pis, active checking period, and
# calculates the duration seconds to wait before making a check to
# see if a device was active
ESTIMATED_NUM_PIS = 4
ACTIVE_CHECK_PERIOD = 10
ACTIVE_CHECK_SECONDS = ESTIMATED_NUM_PIS * ACTIVE_CHECK_PERIOD
# assign montage width and height so we can view all incoming frames
# in a single "dashboard"
mW = args["montageW"]
mH = args["montageH"]
print("[INFO] detecting: {}...".format(", ".join(obj for obj in
    CONSIDER)))

gate = False
state_1 = True
def countdown(t): 
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1

  


while True:
  
    # (rpiName, frame) = imageHub.recv_image()
    # imageHub.send_reply(b'OK')
    # if rpiName not in lastActive.keys():
    #     print("[INFO] receiving data from {}...".format(rpiName))
    
    # lastActive[rpiName] = datetime.now()
    # frame = imutils.resize(frame, width=400)
    # (h, w) = frame.shape[:2]


    # blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
    #     0.007843, (300, 300), 127.5)
    
    # net.setInput(blob)
    # detections = net.forward()
    
    # objCount = {obj: 0 for obj in CONSIDER}
    # for i in np.arange(0, detections.shape[2]):
    #     confidence = detections[0, 0, i, 2]
        
    #     if confidence > args["confidence"]:
            
    #         idx = int(detections[0, 0, i, 1])
            
    #         if CLASSES[idx] in CONSIDER:
                
    #             objCount[CLASSES[idx]] += 1
                
    #             box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
    #             (startX, startY, endX, endY) = box.astype("int")
                
    #             cv2.rectangle(frame, (startX, startY), (endX, endY),
    #                 (255, 0, 0), 2)
    # cv2.putText(frame, rpiName, (10, 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    
    # label = ", ".join("{}: {}".format(obj, count) for (obj, count) in objCount.items())
    # cv2.putText(frame, label, (10, h - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255,0), 2)
    # if (rpiName == "raspberrypi"):
    #     count_a = objCount["car"]
    # else:
    #     count_b = objCount["car"]
    count_a = random.randint(1,7)
    count_b = random.randint(1,9)
    count_c = random.randint(1,6)
    count_d = random.randint(1,7)
    
    
    ##################### 1
    if (count_a <= min_car_detect and count_a != 0):
        output_1 = min_green
    elif (count_a > min_car_detect and count_a <= max_car_detect):
        t_output_1 = (max_car_detect - count_a) / (max_car_detect - min_car_detect)
        output_1 = max_green - t_output_1*(max_car_detect - min_car_detect)
    elif (count_a == 0):
        output_1 = 0
    elif (count_a > max_car_detect):
        output_1 = max_green
    #################### 2
    if (count_b <= min_car_detect and count_b != 0):
        output_2 = min_green
    elif (count_b > min_car_detect and count_b <= max_car_detect):
        t_output_2 = (max_car_detect - count_b) / (max_car_detect - min_car_detect)
        output_2 = max_green - t_output_2*(max_car_detect - min_car_detect)
    elif (count_b == 0):
        output_2 = 0
    elif (count_b > max_car_detect):
        output_2 = max_green
    ################### 3
    if (count_c <= min_car_detect and count_c != 0):
        output_3 = min_green
    elif (count_c > min_car_detect and count_c <= max_car_detect):
        t_output_3 = (max_car_detect - count_c) / (max_car_detect - min_car_detect)
        output_3 = max_green - t_output_3*(max_car_detect - min_car_detect)
    elif (count_c == 0):
        output_3 = 0
    elif (count_c > max_car_detect):
        output_3 = max_green
    ################## 4
    if (count_d <= min_car_detect and count_d != 0):
        output_4 = min_green
    elif (count_d > min_car_detect and count_d <= max_car_detect):
        t_output_4 = (max_car_detect - count_d) / (max_car_detect - min_car_detect)
        output_4 = max_green - t_output_4*(max_car_detect - min_car_detect)
    elif (count_d == 0):
        output_4 = 0
    elif (count_d > max_car_detect):
        output_4 = max_green


    #print("Source 1 : "+str(output_1)+ " Source 2 : "+str(output_2)+ " Source 3 : "+str(output_3)+ " Source 4 : "+str(output_4), end="\r")
    #susunan (output_1, output_2, output_3, output_4)
    if (state_a == True):
        if (open_akhir == True):
            TTA = time.time()
            KA = TTA + 3
            task_print = True
        open_akhir = False        
        if task_print == True:
            print("State A : Lampu Kunign 4 ON")
        if (time.time() > KA):
            task_print = False
            if (open_awal == True):
                TA = time.time()
                HA = TA + output_1
            open_awal = False
            print("State A : Lampu Hijau 1 ON")
            if (time.time() > HA):
                state_b = True
                state_a = False
                open_akhir = True
                open_awal = True
                

    elif (state_b == True):
        if (open_akhir == True):
            TTB = time.time()
            KB = TTB + 3
            task_print = True
        open_akhir = False
        if task_print == True:
            print("State B : Lampu Kuning 1 ON")
        if (time.time() > KB):
            task_print = False
            if (open_awal == True):
                TB = time.time()
                HB = TB + output_2
            open_awal = False
            print("State B : Lampu Hijau 2 ON")
            if (time.time() > HB):
                state_c = True
                state_b = False
                open_akhir = True
                open_awal = True
                

    elif (state_c == True):
        if (open_akhir == True):
            TTC = time.time()
            KC = TTC + 3
            task_print = True
        open_akhir = False
        if task_print == True:
            print("State C : Lampu Kuning 2 ON")
        if (time.time() > KC):
            task_print = False
            if (open_awal == True):
                TC = time.time()
                HC = TC + output_3
            open_awal = False
            print("State C : Lampu Hijau 3 ON")
            if (time.time() > HC):
                state_d = True
                state_c = False
                open_akhir = True
                open_awal = True

    elif (state_d == True):
        if (open_akhir == True):
            TTD = time.time()
            KD = TTD + 3
            task_print = True
        open_akhir = False
        if task_print == True:
            print("State D : Lampu Kuning 3 ON")
        if (time.time() > KD):
            task_print = False
            if (open_awal == True):
                TD = time.time()
                HD = TD + output_4
            open_awal = False
            print("State D : Lampu Hijau 4 ON")
            if (time.time() > HD):
                state_a = True
                state_d = False
                open_akhir = True
                open_awal = True

    # frameDict[rpiName] = frame
    # if (gate == True):
    #     break
    # montages = build_montages(frameDict.values(), (w, h), (mW, mH))
	
    # for (i, montage) in enumerate(montages):
    #     cv2.imshow("Home pet location monitor ({})".format(i),
    #         montage)
	
    key = cv2.waitKey(1) & 0xFF
    # if (datetime.now() - lastActiveCheck).seconds > ACTIVE_CHECK_SECONDS:
           
    #     for (rpiName, ts) in list(lastActive.items()):
    #         if (datetime.now() - ts).seconds > ACTIVE_CHECK_SECONDS:
    #             print("[INFO] lost connection to {}".format(rpiName))
    #             lastActive.pop(rpiName)
    #             frameDict.pop(rpiName)
       
    #     lastActiveCheck = datetime.now()
    time.sleep(0.5)

    if key == ord("q"):
        break

cv2.destroyAllWindows()


    
    

            
