import cv2
import numpy as np
import mediapipe as mp
import time
import os

# Подключаем камеру
cap = cv2.VideoCapture(0)
cap.set(3, 640) # Width
cap.set(4, 480) # Lenght
cap.set(10, 100) # Brightness

mpHands = mp.solutions.hands
hands = mpHands.Hands(False)
npDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

#Зацикливаем получение кадров от камеры
success, img = cap.read()
img = cv2.flip(img,1) # Mirror flip


def detect_arm():
   
   imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
   
   results = hands.process(imgRGB)
   l_x = [ ]
   l_y = [ ]
   if results.multi_hand_landmarks:
       for handLms in results.multi_hand_landmarks:
           for id, lm in enumerate(handLms.landmark):
                h,w,c = img.shape
                # print(id, lm.x, lm.y)
                l_x.append(lm.x)
                l_y.append(lm.y)
       return l_x

#print(detect_arm())
