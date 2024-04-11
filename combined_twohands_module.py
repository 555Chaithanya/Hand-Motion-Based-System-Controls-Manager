import cv2
import mediapipe as mp
import math

class handDetector():
    def __init__(self, mode=False, maxHands=2, modelComp=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.modelComp = modelComp
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComp,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, draw=True):
        rlmlist = []
        xList = []
        yList = []
        bbox = []
        self.lmList = []
        if self.results.multi_hand_landmarks:
            if len(self.results.multi_hand_landmarks) == 2:
                rlmlist.append('both')
            elif len(self.results.multi_hand_landmarks) == 1:
                rlmlist.append(self.results.multi_handedness[0].classification[0].label)
            for n in self.results.multi_hand_landmarks:
                myHand = n
                for id, lm in enumerate(myHand.landmark):

                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    xList.append(cx)
                    yList.append(cy)

                    self.lmList.append([id, cx, cy])
                    if draw:
                        cv2.circle(img, (cx, cy), 5, (0, 200, 250), cv2.FILLED)
                rlmlist.append(self.lmList)
            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            bbox = xmin, ymin, xmax, ymax

            if draw:
                cv2.rectangle(img, (bbox[0] - 20, bbox[1] - 20), (bbox[2] + 20, bbox[3] + 20), (0, 255, 0), 2)

        return bbox, rlmlist

    def findPositionwrtcursor(self, img, draw=True, color =  (255, 0, 255), z_axis=False):

        clmlist = []
        self.lmList = []
        if self.results.multi_hand_landmarks:
            if len(self.results.multi_hand_landmarks) == 2:
                clmlist.append('both')
            elif len(self.results.multi_hand_landmarks) == 1:
                clmlist.append(self.results.multi_handedness[0].classification[0].label)
            for n in self.results.multi_hand_landmarks:
                myHand = n
                for id, lm in enumerate(myHand.landmark):
                    #   print(id, lm)
                    h, w, c = img.shape
                    if z_axis == False:
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        # print(id, cx, cy)
                        self.lmList.append([id, cx, cy])
                    elif z_axis:
                        cx, cy, cz = int(lm.x * w), int(lm.y * h), round(lm.z, 3)
                        # print(id, cx, cy, cz)
                        self.lmList.append([id, cx, cy, cz])
                        if draw:
                            cv2.circle(img, (cx, cy), 5, (0, 200, 250), cv2.FILLED)
                clmlist.append(self.lmList)
        return clmlist
    def fingersUp(self):
        tipIds = [4, 8, 12, 16, 20]
        fingers = []
        # Thumb
        if self.lmList[tipIds[0]][1] > self.lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Fingers
        for id in range(1, 5):

            if self.lmList[tipIds[id]][2] < self.lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # totalFingers = fingers.count(1)

        return fingers

    def findDistance(self, p1, p2, img, draw=True):
        x1, y1 = self.lmList[p1][1], self.lmList[p1][2]
        x2, y2 = self.lmList[p2][1], self.lmList[p2][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        if draw:
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)
        return length, img, [x1, y1, x2, y2, cx, cy]