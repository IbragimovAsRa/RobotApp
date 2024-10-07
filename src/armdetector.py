import cv2
import numpy as np
import mediapipe as mp
import time
import os
import sys
import time
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import QThread, Signal, QTimer
from PySide6.QtGui import QPixmap, QImage

            # Создаем новое изображение (для примера просто белое изображение)
            # image = QImage(300, 300, QImage.Format_RGB32)
            # image.fill(0xFFFFFFFF)  # Заполняем белым цветом
            # time.sleep(1)  # Задержка для демонстрации обновлений
            #Зацикливаем получение кадров от камеры

class Worker(QThread):
    update_signal = Signal(QImage)  # Сигнал для передачи нового изображения

    def run(self):
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

        while True:


            success, img = cap.read()
            
            img = cv2.flip(img,1) # Mirror flip

            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(imgRGB)
            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                    for id, lm in enumerate(handLms.landmark):
                        h,w,c = img.shape
                        cx, cy = int(lm.x*w), int(lm.y*h)
                    # print(id, lm)
                        if  id == 8 or id == 12:
                            cv2.circle(img, (cx,cy),10,(255,0,255),cv2.FILLED)
                    
                    npDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            

            cTime = time.time()
            fps = 1/(cTime-pTime)
            pTime = cTime

            height, width, channel = img.shape
            bytes_per_line = channel * width
            q_img = QImage(img.data, width, height, bytes_per_line, QImage.Format_RGB888)
            self.update_signal.emit(q_img)  # Отправляем изображение






    # cv2.putText(img, str(int(fps)),(10,30), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2) # ФреймРейт
    
    # cv2.imshow('python', img)
    # if cv2.waitKey(20) == 27: # exit on ESC
    #     break
        
# cv2.destroyWindow("python")
# cv2.waitKey(1)
# cap.release()