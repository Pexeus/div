import cv2
import zmq
import base64
import numpy as np

context = zmq.Context()
footage_socket = context.socket(zmq.SUB)
footage_socket.bind('tcp://*:5555')
footage_socket.setsockopt_string(zmq.SUBSCRIBE, "")

while True:
    try:
        rawbB64 = footage_socket.recv_string()
        img = base64.b64decode(rawbB64)

        npimg = np.frombuffer(img, dtype=np.uint8)
        frame = cv2.imdecode(npimg, 1)

        cv2.imshow("image", frame)
        cv2.waitKey(1) & 0xFF

    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        print("\n\nBye bye\n")
        break
