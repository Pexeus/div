# Path: /ai/zmqServer.py
# Autors: Liam Benedetti
# Description: Initiates imageZMQ on port 5555 and passes frames from the Network to counter.py

import imagezmq

# initiate the ZMQ Socket server and make it accessible for couter.py
def initiateZMQ():
    imageHub = imagezmq.ImageHub()
    return imageHub

# takes the ZMQ hub and waits for a full frame
# if a full frame is recieved, return it
def recvZMQ(ZMQ):
    (camName, frame) = ZMQ.recv_image()
    ZMQ.send_reply(b'OK')

    return (camName, frame)

# deactivates the ZMQ Socket
# this prevents the program from blocking the port after exit
def closeZMQ(ZMQ):
    print("[INFO] closing imageZMQ")
    ZMQ.close()