import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice
from PySide6 import QtWidgets
from mainwindow_ui import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
   def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Создаем экземпляр класса Ui_MainWindow
        self.ui.setupUi(self)       # Настраиваем интерфейс