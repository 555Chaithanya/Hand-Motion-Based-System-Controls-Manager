import cv2
import time
import numpy as np
from Modules import combined_twohands_module as cm
import pyautogui, autopy
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc

wCam, hCam = 860, 640
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime = 0
alist = []
detector = cm.handDetector(maxHands=2, detectionCon=0.85, trackCon=0.8)

def putText(mode, loc=(300, 450), color=(0, 255, 255)):
    cv2.putText(img, str(mode), loc, cv2.FONT_HERSHEY_COMPLEX_SMALL,
                2, color, 2)

######################################### volume section
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None
)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0
area = 0
colorVol = (0,0,255)
#########################################################

#########################################################
tipIds = [4, 8, 12, 16, 20]
mode = ''
active = 0
############################### cursor section
pyautogui.FAILSAFE = False

########################### Brightness section
val = 0
blevel= 100
#################################################

while True:
    success, img = cap.read(0)
    img = cv2.flip(img, 1)
    fingers = []
    img = detector.findHands(img, draw=False)
    lmList = detector.findPosition(img, draw=False)
    clmList = detector.findPositionwrtcursor(img, draw=False)

    if clmList:
        #Thumb
        if clmList[1][tipIds[0]][1] > clmList[1][tipIds[0 -1]][1]:
            if clmList[1][tipIds[0]][1] >= clmList[1][tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
        elif clmList[1][tipIds[0]][1] < clmList[1][tipIds[0 -1]][1]:
            if clmList[1][tipIds[0]][1] <= clmList[1][tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        for id in range(1,5):
            if clmList[1][tipIds[id]][2] < clmList[1][tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # Selection of modes for hand signs
        # if clmList[0] == "both":
        #     if (fingers == [0, 0, 0, 0, 0]) & (active == 0):
        #         mode = 'N'
        if clmList[0] == "Left":
            if (fingers == [0, 0, 0, 0, 0]) & (active == 0):
                mode = 'N'
            elif (fingers != [0, 1, 1, 1, 0] and fingers != [0, 1, 1, 1, 1] and (fingers == [0, 1, 0, 0, 0] or fingers == [0, 1, 1, 0, 0])) & (active == 0):
                mode = 'Scroll'
                active = 1
            elif (fingers == [1, 1, 1, 1, 1]) & (active == 0):
                mode = 'Volume'
                active = 1
            elif ((fingers == [0, 1, 1, 1, 1] and fingers != [0, 1, 1, 1, 0])) & (active == 0):
                mode = "tab_change"
                active = 1
            elif (fingers == [0, 1, 1, 1, 0] ) & (active == 0):
                mode = "tab_close_min"
                active = 1
            elif (fingers == [1, 0, 0, 0, 1] or fingers == [0, 1, 0, 0, 1]) & (active == 0):
                mode = "zoom"
                active = 1

        elif clmList[0] == "Right":
            if (fingers == [0, 0, 0, 0, 0]) & (active == 0):
                mode = 'N'
            elif (fingers == [1, 1, 1, 0, 0]) & (active == 0):
                mode = 'Cursor'
                active = 1
            elif (fingers == [0, 1, 1, 0, 0] or fingers == [0, 1, 0, 0, 0]) & (active == 0):
                mode = 'copy_paste'
                active = 1
            elif (fingers == [1, 1, 0, 0, 1]) & (active == 0):
                mode = "Brightness"
                active = 1



    #######################################################################
    if mode == 'Cursor':
        active = 1
        putText(mode)
        imgc = detector.findHands(img, draw=True)

        cv2.rectangle(imgc, (30, 30), (750, 460), (255, 255, 255), 3)

        if fingers[1:] == [0,0,0,0]: #except thumb
            active = 0
            pyautogui.keyUp('shift')
            mode = 'N'
            print(mode)
        else:
            if len(clmList) != 0:
                xl1, yl1 = clmList[1][8][1], clmList[1][8][2]
                xl2, yl2 = clmList[1][12][1], clmList[1][12][2]
                w, h = autopy.screen.size()
                X = int(np.interp(xl1, [110, 620], [0, w - 1]))
                Y = int(np.interp(yl1, [20, 350], [0, h - 1]))
                cv2.circle(imgc, (clmList[1][8][1], clmList[1][8][2]), 7, (255, 255, 255), cv2.FILLED)
                cv2.circle(imgc, (clmList[1][12][1], clmList[1][12][2]), 7, (255, 255, 255), cv2.FILLED)
                cv2.circle(imgc, (clmList[1][4][1], clmList[1][4][2]), 10, (0, 255, 0), cv2.FILLED)  #thumb

                if X%2 !=0:
                    X = X - X%2
                if Y%2 !=0:
                    Y = Y - Y%2
                print(X,Y)
                if fingers == [1, 1, 1, 0, 0]:
                    autopy.mouse.move(X, Y)
                if fingers[0] == 0:
                    cv2.circle(imgc, (clmList[1][4][1], clmList[1][4][2]), 10, (0, 0, 255), cv2.FILLED)  # thumb
                    pyautogui.click()
                if fingers == [1, 1, 0, 0, 1]:
                    pyautogui.keyDown('shift')
                    time.sleep(0.1)
                    pyautogui.press('down')
                    time.sleep(0.1)
                    pyautogui.keyDown('shift')
                    time.sleep(0.2)

    #######################################################################
    if mode == 'Volume':
        active = 1
        # print(mode)
        putText(mode)
        img = detector.findHands(img)
        bbox, vlmList = detector.findPosition(img, draw=True)
        if len(vlmList) != 0:
            if fingers == [0, 0, 0, 0, 0]:
                active = 0
                mode = 'N'
                print(mode)

            elif fingers == [1, 1, 1, 1, 1] or fingers == [1, 1, 1, 1, 0] or fingers == [1, 0, 1, 1, 1] or fingers == [1, 0, 1, 1, 0]:

                area = ((bbox[2] - bbox[0]) * (bbox[3] - bbox[1])) // 100
                # print(area)
                if 250 < area < 1000:

                    # Find distance between index and thumb
                    length, img, lineInfo = detector.findDistance(4, 8, img)
                    # print(length)

                    # Convert Volume
                    volBar = np.interp(length, [30, 230], [400, 150])
                    volPer = np.interp(length, [30, 230], [0, 100])

                    # Reduce Resolution to make it smoother
                    smoothness = 10
                    volPer = smoothness * round((volPer / smoothness))

                    # Check which of fingers are up
                    fingers = detector.fingersUp()
                    # check if pinky is down to set the volume
                    if not fingers[4]:
                        volume.SetMasterVolumeLevelScalar(volPer / 100, None)
                        cv2.circle(img, (lineInfo[4], lineInfo[5]), 10, (255, 200, 0), cv2.FILLED)
                        colorVol = (255, 200, 0)

                    else:
                        colorVol = (0, 0, 255)

                cv2.rectangle(img, (50, 150), (70, 400), (0, 0, 0), 3)
                cv2.rectangle(img, (50, int(volBar)), (70, 400), (0, 0, 255), cv2.FILLED)
                cv2.putText(img, f'{int(volPer)}%', (50, 450), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

                cVol = int(volume.GetMasterVolumeLevelScalar() * 100)
                cv2.putText(img, f'Vol Set:{int(cVol)}', (710, 450), cv2.FONT_HERSHEY_PLAIN, 1.5, colorVol,
                            2)

    #######################################################################
    if mode == 'Brightness':
        active = 1
        # print(mode)
        putText(mode)
        img = detector.findHands(img)
        bbox, vlmList = detector.findPosition(img, draw=True)
        if len(vlmList) != 0:
            if fingers == [0, 0, 0, 0, 0]:
                active = 0
                mode = 'N'
                print(mode)

            elif fingers == [1, 1, 0, 0, 1] or fingers == [1, 1, 0, 0, 0]:

                area = ((bbox[2] - bbox[0]) * (bbox[3] - bbox[1])) // 100
                # print(area)
                if 100 < area < 1000:

                    # Find distance between index and thumb
                    length, img3, lineInfo = detector.findDistance(4, 8, img)
                    # print(length)
                    # Convert Brightness
                    blevel = np.interp(length, [25, 145], [0, 100])
                    val = np.interp(length, [0, 100], [400, 150])
                    blevel = int(blevel)
                    sbc.set_brightness(blevel)


                    cv2.rectangle(img, (50, 150), (70, 400), (0, 0, 0), 4)
                    cv2.rectangle(img, (50, int(val)), (70, 400), (0, 255, 255), -1)
                    cv2.putText(img, str(blevel) + '%', (20, 430), cv2.FONT_HERSHEY_COMPLEX, 1,
                               (255, 0, 0), 3)

    ###################################################################################
    if mode == 'Scroll':
        active = 1
        putText(mode)
        img2 = detector.findHands(img, draw=True)
        cv2.rectangle(img2, (100, 410), (145, 460), (255, 255, 255), cv2.FILLED)
        if len(clmList) != 0:
            if fingers == [0,1,0,0,0]:
              #print('up')

                putText(mode = 'U', loc=(100, 455), color = (0, 255, 0))
                pyautogui.scroll(150)
                time.sleep(0.1)
            if fingers == [0,1,1,0,0]:
                #print('down')

                putText(mode = 'D', loc = (100, 455), color = (0, 0, 255))
                pyautogui.scroll(-150)
                time.sleep(0.1)
            elif fingers == [0, 0, 0, 0, 0]:
                active = 0
                mode = 'N'
    ############################################################################Tab_Change
    if mode == "tab_change":
        active = 1
        putText(mode)
        img3 = detector.findHands(img, draw=True)
        lmList, bbox = detector.findPosition(img3)
        if lmList:
            if detector.fingersUp() == [0, 1, 0, 0, 1]:
                pyautogui.hotkey('alt', 'tab')
                time.sleep(0)
            elif fingers == [0, 0, 0, 0, 0]:
                active = 0
                mode = 'N'
    ####################################################################################
    if mode == "tab_close_min":
        active = 1
        putText(mode)
        img3 = detector.findHands(img, draw=True)
        lmList, bbox = detector.findPosition(img3)
        if lmList:
            if detector.fingersUp() == [0, 1, 1, 0, 0] :
                pyautogui.hotkey('alt', 'F4')
                time.sleep(0)
            elif detector.fingersUp() == [0, 1, 0, 0, 0] :
                # pyautogui.hotkey('win', 'down')
                time.sleep(0)
            elif fingers == [0, 0, 0, 0, 0]:
                active = 0
                mode = 'N'
    ####################################################################################
    if mode == "copy_paste":
        active = 1
        putText(mode)
        img3 = detector.findHands(img, draw=True)
        lmList, bbox = detector.findPosition(img3)

        if lmList:
            if detector.fingersUp() == [0, 1, 1, 0, 0]:
                pyautogui.keyDown('ctrl')
                time.sleep(0.1)
                pyautogui.press('c')
                pyautogui.keyUp('ctrl')
                time.sleep(0.1)
            elif detector.fingersUp() == [0, 1, 0, 0, 0]:
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(0.3)
            elif fingers == [0, 0, 0, 0, 0]:
                active = 0
                mode = 'N'
    ####################################################################################
    if mode == "zoom":
        active = 1
        putText(mode)
        img4 = detector.findHands(img, draw=True)
        bbox, zlmList = detector.findPosition(img4,draw=True)
        if zlmList:
            area = ((bbox[2] - bbox[0]) * (bbox[3] - bbox[1])) // 100
            fingers = detector.fingersUp()
            alist.append(area)
            print(alist)
            if fingers == [1, 0, 0, 0, 1]:
                if len(alist) > 2:
                    alist.pop(0)
                    if alist[-1] > alist[-2]:
                        pyautogui.hotkey("win", "=")
                        time.sleep(0.6)
                    elif alist[-1] < alist[-2]:
                        pyautogui.hotkey("win", "-")
                        time.sleep(0.6)
            elif fingers == [0, 1, 0, 0, 1]:
                if len(alist) > 2:
                    if alist[-1] > alist[-2]:
                        pyautogui.hotkey("ctrl", "=")
                        time.sleep(0.6)
                    elif alist[-1] < alist[-2]:
                        pyautogui.hotkey("ctrl", "-")
                        time.sleep(0.6)
            elif fingers == [0, 0, 0, 0, 0]:
                alist = []
                active = 0
                mode = 'N'
    ####################################################################################

    cTime = time.time()
    fps = 1 / ((cTime + 0.01) - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS:{int(fps)}', (720, 30), cv2.FONT_ITALIC, 1, (255, 0, 0), 2)
    cv2.imshow("Hand's LiveFeed", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break