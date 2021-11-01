import threading
import time

import cv2


class Camera:
    camera = None
    current_frame = None
    accessed = 0
    thread = None

    @classmethod
    def initialize(cls):
        if cls.thread is None:
            cls.accessed = time.time()
            cls.thread = threading.Thread(target=cls.cam_loop)
            cls.thread.start()
            if cls.current_frame is None:
                time.sleep(.01)

    @classmethod
    def cam_loop(cls):
        if cls.camera is None:
            cls.camera = cv2.VideoCapture(1)
            while True:
                success, frame = cls.camera.read()
                if not success:
                    break
