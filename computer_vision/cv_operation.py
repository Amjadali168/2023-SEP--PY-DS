import cv2
import numpy as np
import os
def load_video(path_of_video):
    if not os.path.exists(path_of_video):
        print(f"video file not found\n{path_of_video}")
        return None
    video = cv2.VideoCapture(path_of_video)
    cv2.namedWindow("Video")
    cv2.createTrackbar("ksize","video",3,100,lambda x:None)
    while True:
        status, frame = video.read()
        height, width, _ = frame.shape
        if not status:
            print("video could not be read!!")
            break
        # operations
        # 1. resize
        # frame = cv2.resize(frame,(640,480))
        frame = cv2.resize(frame,(None,None),fx=.5, fy=.5)  # half the size
        # 2. convert to grayscale
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 3. blur
        # frame = cv2.GaussianBlur(frame, (5, 5), 0)
        ksize = cv2.getTrackbarPos("ksize","Video")
        try:frame = cv2.GaussianBlur(frame,(ksize, ksize),0)
        except:pass
        # 4. add text
        frame = cv2.putText(
            img=frame,
            text="Hello World!",
            org=(width//2 - 70,height//2 + 50),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1,
            color=[0,0,255],
            thickness=2,
            lineType=cv2.LINE_AA
        )
        # 5. add graphics
        cv2.imshow("video",frame)
        if cv2.waitKey(2) == ord('q'):    # 1 represents 1 millisecond
            break
    # clear the memory
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    videofile = r"/Users/Amjad/Downloads/WhatsApp Video 2023-09-19 at 4.22.33 PM.mp4"
    load_video(videofile)
    # video will display on the screen