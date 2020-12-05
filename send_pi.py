from imutils.video import VideoStream
import imagezmq
import argparse
import socket
import time
import cv2
# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-s", "--server-ip", required=True,
# 	help="ip address of the server to which the client will connect")
# args = vars(ap.parse_args())
# initialize the ImageSender object with the socket address of the
# server
sender = imagezmq.ImageSender(connect_to="tcp://192.168.3.104:5555")

rpiName = socket.gethostname()
#vs = VideoStream(src=0).start()
#vs = VideoStream(src=0).start()
vs = cv2.VideoCapture(0)
time.sleep(2.0)
 
while True:
	# read the frame from the camera and send it to the server
    ret, frame = vs.read()
    sender.send_image(rpiName, frame)
    
