import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice
from PySide6 import QtWidgets
from PySide6.QtCore import QObject, Signal, Slot
from ui.mainwindow import Ui_MainWindow
from armdetector import Worker
from PySide6.QtCore import QObject, Signal, Slot
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import QThread, Signal, QTimer
from PySide6.QtGui import QPixmap, QImage
from robot3d import Robot3d

class MainWindow(QtWidgets.QMainWindow):
   def __init__(self):
      super().__init__()
      self.ui = Ui_MainWindow()
      self.ui.setupUi(self)


      self.robot3dWindow = Robot3d()
      self.robot3d = QtWidgets.QWidget.createWindowContainer(self.robot3dWindow)
      self.robot3d.show()
      self.ui.robotLayout.addWidget(self.robot3d)

      self.ui.armControllerButton.clicked.connect(self.start_arm_detection)

   def update_image(self, image):
      pixmap = QPixmap.fromImage(image)  # Преобразуем QImage в QPixmap
      self.ui.armViewLabel.setPixmap(pixmap)  # Обновляем изображение в QLabel

   def start_arm_detection(self):
      self.worker = Worker()
      self.worker.update_signal.connect(self.update_image)
      self.worker.start()  # Запускаем поток

   def stop_arm_detection():
      pass   
       