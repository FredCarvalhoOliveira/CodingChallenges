import numpy as np
import cv2
import matplotlib.pyplot as plt

import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


ASCII_BRIGHTNESS = " .:-=+*#%@"


def greyScale2ASCII(greyScaleValue):
    levelGap = (256 / len(ASCII_BRIGHTNESS))
    idx = int(greyScaleValue // levelGap)
    return ASCII_BRIGHTNESS[idx]

def img2ASCII(grey):
    asciiImg = ''
    for y in range(grey.shape[0]):
        for x in range(grey.shape[1]):
            asciiImg += greyScale2ASCII(grey[y][x])
        asciiImg += '\n'
    return asciiImg

def resizeImg(img, width=100):
    scaleFactor = width/img.shape[1]
    dim = (int(img.shape[1] * scaleFactor), int(img.shape[0] * scaleFactor))
    return cv2.resize(img, dim)

# # frame = cv2.imread('eiffel_tower.jpg')
# grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# resized = resizeImg(grey, 102)



# while True:
#     clearConsole()
#     print(img2ASCII(resized))

# define a video capture object
cap = cv2.VideoCapture(1)

while (True):

    # Capture the video frame
    ret, frame = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized = resizeImg(grey, 80)

    clearConsole()
    print(img2ASCII(resized))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
