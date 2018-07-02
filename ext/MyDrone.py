import sys
import os.path
from controlGUI import *
from PyQt5.QtCore import QObject, pyqtSlot, QUrl
import sys
import os.path
from PyQt5.QtWidgets import QMainWindow, QWidget, QFrame, QSlider, QHBoxLayout, QPushButton, \
    QVBoxLayout, QAction, QFileDialog, QApplication
import vlc
from controlGUI import DroneGUI
from Bebop import Bebop




if __name__=="__main__":
    bebop = Bebop()
    app = QApplication(sys.argv)
    vision = DroneGUI()
    vision.setDrone(bebop)
    bebop.setVision(vision)
    vision.show()
    vision.resize(995, 720)
    sys.exit(app.exec_())
