import sys
from mainwindow import MainWindow
from PySide6 import QtCore, QtWidgets, QtGui
# import armdetector


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)  
    app = QtWidgets.QApplication([])
    w = MainWindow()
    w.show()

    # armdetector.detect_arm()
    
    sys.exit(app.exec())

