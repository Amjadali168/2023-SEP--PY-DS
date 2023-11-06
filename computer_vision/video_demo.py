import cv2
import numpy as np
import os
def load_video(path_of_video):
    if not os.path.exists(path_of_video):
        print(f"video file not found\n{path_of_video}")
        return None
    video = cv2.VideoCapture(path_of_video)
    while True:
        status, frame = video.read()
        if not status:
            print("video could not be read!!")
            break
        cv2.imshow("video",frame)
        if cv2.waitKey(1) == ord('q'):    # 1 represents 1 millisecond
            break
    # clear the memory
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    videofile = r"/Users/Amjad/Downloads/WhatsApp Video 2023-09-19 at 4.22.33 PM.mp4"
    load_video(videofile)