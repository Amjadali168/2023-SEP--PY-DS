import cv2
import numpy as np
import os
def load_video(camera_index):
    if not os.path.exists(camera_index):
        print(f"Camera not found\n{camera_index}")
        return None
    video = cv2.VideoCapture(camera_index)
    while True:
        status, frame = video.read()
        if not status:
            print("camera data not read!!")
            break
        cv2.imshow("Camera",frame)
        if cv2.waitKey(1) == ord('q'):    # 1 represents 1 millisecond
            break
    # clear the memory
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    cam_idx = 0
    load_video(cam_idx)