from imutils.video import VideoStream
import imagezmq
import socket
import time
import cv2
import imutils


sender = imagezmq.ImageSender(connect_to="tcp://192.168.3.101:5555")
rpiName2 = socket.gethostname()
#vs = VideoStream(src=0).start()
vs = cv2.VideoCapture("data.mp4")
time.sleep(2.0)
 
while True:
    #print("sending data to server ....", end="\r")
    ret, frame = vs.read()
    frame = imutils.resize(frame, width=320)
    sender.send_image(rpiName2, frame)
    