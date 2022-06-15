import mss
import numpy as np
import cv2
import pyautogui
import keyboard
import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', path='/Users/mfavela/Desktop/AimlabsAimbot/aimlabs.pt')

with mss.mss() as sct:
    monitor = {'top': 30, 'left': 0, 'width': 1152, 'height': 864}

while True:
    img = np.array(sct.grab(monitor))
    results = model(img)

    rl = result.xyxy[0].tolist()
    print(rl)

    if len(rl) > 0:
        if rl[0][4] > .35:
            x = int(rl[0][2])
            y = int(rl[0][3])

            width = int(rl[0][2] - rl[0][0])
            height = int(rl[0][3] - rl[0][1])

            xpos = int(.37 * ((x - (width / 2)) - pyautogui.position()[0]))
            ypos = int(.30 * ((y - (height / 2)) - pyautogui.position()[1]))

            pyautogui.moveRel(xpos, ypos)
            pyautogui.click()
            pyautogui.moveRel(-xpos, -ypos)
    
    cv2.imshow('s', np.squeeze(results.render()))
    cv2.waitKey(1)
    if keyboard.is_pressed('q'):
        break
cv2.destroyAllWindows()
