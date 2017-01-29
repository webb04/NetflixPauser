# -*- coding:utf-8 -*-
import cv2
import subprocess

from boss_train import Model
from image_show import show_image
from appscript import app

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    cascade_path = "/Users/Jamie/miniconda3/envs/venv/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
    model = Model()
    model.load()
    timeSinceNoUser = 0
    timeSinceUser = 0
    while True:
        _, frame = cap.read()

        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cascade = cv2.CascadeClassifier(cascade_path)

        facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.2, minNeighbors=3, minSize=(10, 10))
        # facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.01, minNeighbors=3, minSize=(3, 3))

        if len(facerect) > 0:
            timeSinceUser = timeSinceUser + 1
            if timeSinceNoUser >= 10:
                print("User is present, resume streams")
                app('System Events').keystroke('\r')
            timeSinceNoUser = 0
            print('Face Detected')
            color = (255, 255, 255)
            for rect in facerect:
                #cv2.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)

                x, y = rect[0:2]
                width, height = rect[2:4]
                image = frame[y - 10: y + height, x: x + width]

                result = model.predict(image)
                print(result)
                if result == 0:  # boss
                    show_image()
                else:
                    print('Not the user')
        else:
            timeSinceUser = 0
            if timeSinceNoUser == 10:
                print("User is not present, pause streams")
                app('System Events').keystroke('\r')
                # subprocess.call("./sleep.sh", shell=True)
            elif timeSinceNoUser < 10:
                print("Time Since no user: " + str(timeSinceNoUser))
            timeSinceNoUser = timeSinceNoUser + 1

        k = cv2.waitKey(100)
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
