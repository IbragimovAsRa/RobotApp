import sys
from PySide6.QtCore import (Property, QObject, QPropertyAnimation, Signal)
from PySide6.QtGui import (QGuiApplication, QMatrix4x4, QQuaternion, QVector3D)
from PySide6.Qt3DExtras import (Qt3DExtras)
from PySide6.Qt3DCore import (Qt3DCore)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice
from PySide6 import QtWidgets
from PySide6.QtCore import QObject, Signal, Slot
from ui.mainwindow import Ui_MainWindow
from armdetector import Worker
from PySide6.QtCore import QObject, Signal, Slot
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import QThread, Signal, QTimer
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QWidget

class Robot3d(Qt3DExtras.Qt3DWindow):
    
    def __init__(self):
        super().__init__()
        self.createScene()

        self.camera().lens().setPerspectiveProjection(45, 16 / 9, 0.1, 1000)
        self.camera().setPosition(QVector3D(0, 0, 40))
        self.camera().setViewCenter(QVector3D(0, 0, 0))

        self.createScene()
        self.camController = Qt3DExtras.QOrbitCameraController(self.rootEntity)
        self.camController.setLinearSpeed(50)
        self.camController.setLookSpeed(180)
        self.camController.setCamera(self.camera())

        self.setRootEntity(self.rootEntity)

    def createScene(self):
        # Root entity
        self.rootEntity = Qt3DCore.QEntity()

        # Material
        self.material = Qt3DExtras.QPhongMaterial(self.rootEntity)

        #  Cub
        self.cubEntity = Qt3DCore.QEntity(self.rootEntity)
        self.cubMesh = Qt3DExtras.QCuboidMesh()
        self.cubMesh.setXExtent(10)
        self.cubMesh.setYExtent(10)
        self.cubMesh.setZExtent(10)
        
        #  Добавление компанентов к кубу
        self.cubEntity.addComponent(self.cubMesh)
        self.cubEntity.addComponent(self.material)

