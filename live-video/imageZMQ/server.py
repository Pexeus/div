import cv2
import time

from imagezmqServer import initiateZMQ, recvZMQ, closeZMQ

ZMQ = initiateZMQ()

while True:
    (camName, frame) = recvZMQ(ZMQ)
    decimg = cv2.imdecode(frame, 1)
    
    cv2.imshow("Frame", decimg)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break