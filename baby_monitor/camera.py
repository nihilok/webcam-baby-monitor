import threading
import time

import cv2

camera = None

last_accessed = 0

global_frame = None


def switch_on_off():
    global camera
    if camera is None:
        camera = cv2.VideoCapture(1)
    else:
        camera = None


def gen_frames():
    global global_frame
    while camera is not None:
        try:
            success, frame = camera.read()  # read the camera frame
        except AttributeError:
            break
        if not success:
            break
        if last_accessed and last_accessed - time.time() > 10:
            break
        else:
            ret, buffer = cv2.imencode(".jpg", frame)
            frame = buffer.tobytes()
            global_frame = (
                b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"
            )
            yield global_frame


thread = threading.Thread(target=gen_frames)
