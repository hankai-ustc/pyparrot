# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
import vlc
import sys
import os.path
from PyQt5.QtCore import QObject, pyqtSlot, QUrl
from PyQt5.QtWebChannel import QWebChannel

class CallHandler(QObject):

    def setSensor(self,sensor):
        self.sensor = sensor

    @pyqtSlot(result=list)
    def getGps(self):
        longtitude = self.sensor.sensors_dict["GpsLocationChanged_longitude"]
        latitude = self.sensor.sensors_dict["GpsLocationChanged_latitude"]
        return [longtitude,latitude]



class DroneGUI(QMainWindow):

    def __init__(self,drone=None,master=None):
        QMainWindow.__init__(self,master)
        self.setWindowTitle("INFINITELAB Drone Control Plateform")
        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()
        self.isConnected = False
        self.createUI(self)
        self.drone = drone
        self.isPaused = False
        self.status = False
        self.setupSignals()
    def setDrone(self,drone):
        self.drone = drone
        if self.drone:
            self.connectDroneButton.clicked.connect(self.connectDrone)
            self.disconnectButton.clicked.connect(self.disconnectDrone)
            self.takeoffButton.clicked.connect(lambda :self.drone.safe_takeoff(1))
            self.upButton.clicked.connect(lambda :self.drone.fly_no_duration(roll=0, pitch=0, yaw=0, vertical_movement=50))
            self.downButton.clicked.connect(lambda :self.drone.fly_no_duration(roll=0, pitch=0, yaw=0, vertical_movement=-50))
            self.leftButton.clicked.connect(lambda :self.drone.fly_no_duration(roll=-50, pitch=0, yaw=0, vertical_movement=0))
            self.rightButton.clicked.connect(lambda :self.drone.fly_no_duration(roll=50, pitch=0, yaw=0, vertical_movement=0))
            self.frontButton.clicked.connect(lambda :self.drone.fly_no_duration(roll=0, pitch=50, yaw=0, vertical_movement=0))
            self.backButton.clicked.connect(lambda :self.drone.fly_no_duration(roll=0, pitch=-50, yaw=0, vertical_movement=0))
            self.landButton.clicked.connect(lambda :self.drone.safe_land(2))
            self.rightRollButton.clicked.connect(lambda :self.drone.fly_no_duration(roll=0, pitch=0, yaw=100, vertical_movement=0))
            self.leftRollButton.clicked.connect(lambda :self.drone.fly_no_duration(roll=0, pitch=0, yaw=-100, vertical_movement=0))
            self.emergencyButton.clicked.connect(self.drone.emergency_land)

            self.channel = QWebChannel()
            self.handler = CallHandler()
            self.handler.setSensor(self.drone.sensors)
            self.channel.registerObject('pyjs', self.handler)
            self.gpsframe.page().setWebChannel(self.channel)

    def connectDrone(self):

        if self.isConnected:
            return
        else:
            self.isConnected = self.drone.connect(5)
            self.drone.smart_sleep(2)
            self.drone.ask_for_state_update()
            self.drone.trim()

    def disconnectDrone(self):
        if not self.isConnected:
            return
        else:
            self.drone.disconnect()
            self.isConnected = False

    def createUI(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(995, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 951, 661))
        self.layoutWidget.setObjectName("layoutWidget")
        self.vboxLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.vboxLayout.setObjectName("vboxLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_6.setSpacing(40)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.openButton = QtWidgets.QPushButton(self.layoutWidget)
        self.openButton.setObjectName("openButton")
        self.horizontalLayout.addWidget(self.openButton)
        self.playButton = QtWidgets.QPushButton(self.layoutWidget)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout.addWidget(self.playButton)
        self.pauseButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout.addWidget(self.pauseButton)
        self.closeButton = QtWidgets.QPushButton(self.layoutWidget)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.horizontalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(40, -1, 40, -1)
        self.horizontalLayout_2.setSpacing(100)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.showGpsButton = QtWidgets.QPushButton(self.layoutWidget)
        self.showGpsButton.setObjectName("showGpsButton")
        self.horizontalLayout_2.addWidget(self.showGpsButton)
        self.closeGpsButton = QtWidgets.QPushButton(self.layoutWidget)
        self.closeGpsButton.setObjectName("closeGpsButton")
        self.horizontalLayout_2.addWidget(self.closeGpsButton)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.vboxLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout2.setObjectName("horizontalLayout2")
        self.videoframe = QtWidgets.QFrame(self.layoutWidget)
        self.videoframe.setAutoFillBackground(True)
        self.videoframe.setFrameShape(QtWidgets.QFrame.Box)
        self.videoframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.videoframe.setObjectName("videoframe")
        self.horizontalLayout2.addWidget(self.videoframe)
        self.gpsframe = QWebEngineView(self.centralwidget)
        self.gpsframe.setAutoFillBackground(True)
        self.gpsframe.setObjectName("gpsframe")
        self.horizontalLayout2.addWidget(self.gpsframe)
        self.horizontalLayout2.setStretch(0, 1)
        self.horizontalLayout2.setStretch(1, 1)
        self.vboxLayout.addLayout(self.horizontalLayout2)
        self.horizontalLayout3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout3.setObjectName("horizontalLayout3")
        self.controlframe = QtWidgets.QFrame(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.controlframe.sizePolicy().hasHeightForWidth())
        self.controlframe.setSizePolicy(sizePolicy)
        self.controlframe.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.controlframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.controlframe.setObjectName("controlframe")
        self.layoutWidget1 = QtWidgets.QWidget(self.controlframe)
        self.layoutWidget1.setGeometry(QtCore.QRect(80, 40, 281, 145))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(30)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.connectDroneButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.connectDroneButton.setObjectName("connectDroneButton")
        self.horizontalLayout_5.addWidget(self.connectDroneButton)
        self.disconnectButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.disconnectButton.setObjectName("disconnectButton")
        self.horizontalLayout_5.addWidget(self.disconnectButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.leftRollButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.leftRollButton.setAutoRepeat(True)
        self.leftRollButton.setObjectName("leftRollButton")
        self.gridLayout.addWidget(self.leftRollButton, 0, 0, 1, 1)
        self.emergencyButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.emergencyButton.setObjectName("emergencyButton")
        self.gridLayout.addWidget(self.emergencyButton, 1, 1, 1, 1)
        self.downButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.downButton.setAutoRepeat(True)
        self.downButton.setObjectName("downButton")
        self.gridLayout.addWidget(self.downButton, 2, 2, 1, 1)
        self.backButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.backButton.setAutoRepeat(True)
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 2, 1, 1, 1)
        self.rightButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.rightButton.setAutoRepeat(True)
        self.rightButton.setObjectName("rightButton")
        self.gridLayout.addWidget(self.rightButton, 1, 2, 1, 1)
        self.leftButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.leftButton.setAutoRepeat(True)
        self.leftButton.setObjectName("leftButton")
        self.gridLayout.addWidget(self.leftButton, 1, 0, 1, 1)
        self.rightRollButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.rightRollButton.setAutoRepeat(True)
        self.rightRollButton.setObjectName("rightRollButton")
        self.gridLayout.addWidget(self.rightRollButton, 0, 2, 1, 1)
        self.upButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.upButton.setAutoRepeat(True)
        self.upButton.setObjectName("upButton")
        self.gridLayout.addWidget(self.upButton, 2, 0, 1, 1)
        self.frontButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.frontButton.setAutoRepeat(True)
        self.frontButton.setObjectName("frontButton")
        self.gridLayout.addWidget(self.frontButton, 0, 1, 1, 1)
        self.takeoffButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.takeoffButton.setObjectName("takeoffButton")
        self.gridLayout.addWidget(self.takeoffButton, 3, 0, 1, 1)
        self.landButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.landButton.setObjectName("landButton")
        self.gridLayout.addWidget(self.landButton, 3, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout3.addWidget(self.controlframe)
        self.statusframe = QtWidgets.QFrame(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusframe.sizePolicy().hasHeightForWidth())
        self.statusframe.setSizePolicy(sizePolicy)
        self.statusframe.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.statusframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.statusframe.setObjectName("statusframe")
        self.layoutWidget2 = QtWidgets.QWidget(self.statusframe)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 30, 431, 153))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_3.setSpacing(50)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.showStatusButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.showStatusButton.setObjectName("showStatusButton")
        self.horizontalLayout_3.addWidget(self.showStatusButton)
        self.closeStatusButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.closeStatusButton.setObjectName("closeStatusButton")
        self.horizontalLayout_3.addWidget(self.closeStatusButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.longitude = QtWidgets.QLabel(self.layoutWidget2)
        self.longitude.setObjectName("longitude")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.longitude)
        self.longitudeValue = QtWidgets.QLineEdit(self.layoutWidget2)
        self.longitudeValue.setObjectName("longitudeValue")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.longitudeValue)
        self.latitude = QtWidgets.QLabel(self.layoutWidget2)
        self.latitude.setObjectName("latitude")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.latitude)
        self.latitudeValue = QtWidgets.QLineEdit(self.layoutWidget2)
        self.latitudeValue.setObjectName("latitudeValue")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.latitudeValue)
        self.altitude = QtWidgets.QLabel(self.layoutWidget2)
        self.altitude.setObjectName("altitude")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.altitude)
        self.altitudeValue = QtWidgets.QLineEdit(self.layoutWidget2)
        self.altitudeValue.setObjectName("altitudeValue")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.altitudeValue)
        self.battery = QtWidgets.QLabel(self.layoutWidget2)
        self.battery.setObjectName("battery")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.battery)
        self.batteryValue = QtWidgets.QLineEdit(self.layoutWidget2)
        self.batteryValue.setObjectName("batteryValue")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.batteryValue)
        self.horizontalLayout_4.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.speedxValue = QtWidgets.QLineEdit(self.layoutWidget2)
        self.speedxValue.setObjectName("speedxValue")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.speedxValue)
        self.speedy = QtWidgets.QLabel(self.layoutWidget2)
        self.speedy.setObjectName("speedy")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.speedy)
        self.speedyValue = QtWidgets.QLineEdit(self.layoutWidget2)
        self.speedyValue.setObjectName("speedyValue")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.speedyValue)
        self.speedz = QtWidgets.QLabel(self.layoutWidget2)
        self.speedz.setObjectName("speedz")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.speedz)
        self.speedzValue = QtWidgets.QLineEdit(self.layoutWidget2)
        self.speedzValue.setObjectName("speedzValue")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.speedzValue)
        self.speedx = QtWidgets.QLabel(self.layoutWidget2)
        self.speedx.setObjectName("speedx")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.speedx)
        self.horizontalLayout_4.addLayout(self.formLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout3.addWidget(self.statusframe)
        self.vboxLayout.addLayout(self.horizontalLayout3)
        self.vboxLayout.setStretch(0, 1)
        self.vboxLayout.setStretch(1, 13)
        self.vboxLayout.setStretch(2, 7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.centralwidget.setLayout(self.vboxLayout)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "INFINITELAB Drone Control Plateform"))
        self.openButton.setText(_translate("MainWindow", "打开"))
        self.playButton.setText(_translate("MainWindow", "播放"))
        self.pauseButton.setText(_translate("MainWindow", "暂停"))
        self.closeButton.setText(_translate("MainWindow", "关闭"))
        self.showGpsButton.setText(_translate("MainWindow", "显示GPS"))
        self.closeGpsButton.setText(_translate("MainWindow", "关闭GPS"))
        self.connectDroneButton.setText(_translate("MainWindow", "连接无人机"))
        self.disconnectButton.setText(_translate("MainWindow", "断开连接"))
        self.leftRollButton.setText(_translate("MainWindow", "左旋"))
        self.emergencyButton.setText(_translate("MainWindow", "紧急降落"))
        self.downButton.setText(_translate("MainWindow", "下"))
        self.backButton.setText(_translate("MainWindow", "后"))
        self.rightButton.setText(_translate("MainWindow", "右"))
        self.leftButton.setText(_translate("MainWindow", "左"))
        self.rightRollButton.setText(_translate("MainWindow", "右旋"))
        self.upButton.setText(_translate("MainWindow", "上"))
        self.frontButton.setText(_translate("MainWindow", "前"))
        self.takeoffButton.setText(_translate("MainWindow", "起飞"))
        self.landButton.setText(_translate("MainWindow", "降落"))
        self.showStatusButton.setText(_translate("MainWindow", "显示状态"))
        self.closeStatusButton.setText(_translate("MainWindow", "关闭状态"))
        self.longitude.setText(_translate("MainWindow", "经度"))
        self.latitude.setText(_translate("MainWindow", "纬度"))
        self.altitude.setText(_translate("MainWindow", "海拔"))
        self.speedy.setText(_translate("MainWindow", "Speed_Y"))
        self.speedz.setText(_translate("MainWindow", "Speed_Z"))
        self.battery.setText(_translate("MainWindow", "电量"))
        self.speedx.setText(_translate("MainWindow", "Speed_X"))

    def setupSignals(self):
        self.openButton.clicked.connect(self.OpenFile)
        self.playButton.clicked.connect(self.Play)
        self.pauseButton.clicked.connect(self.Pause)
        self.closeButton.clicked.connect(self.Stop)
        self.showGpsButton.clicked.connect(self.showGPS)
        self.showStatusButton.clicked.connect(self.showStatus)
        self.closeStatusButton.clicked.connect(self.closeStatus)



    def showStatus(self):
        if self.status == True:
            return
        self.status = True

    def closeStatus(self):
        if self.status == False:
            return
        self.status = False
        self.longitudeValue.setText("")
        self.altitudeValue.setText("")
        self.latitudeValue.setText("")
        self.batteryValue.setText("")
        self.speedxValue.setText("")
        self.speedyValue.setText("")
        self.speedzValue.setText("")

    def Play(self):

        if self.mediaplayer.is_playing():
            return
        else:
            if self.mediaplayer.play() == -1:
                self.OpenFile()
                return
            self.mediaplayer.play()
            self.isPaused = False

    def Pause(self):
        if self.mediaplayer.is_playing():
            self.mediaplayer.pause()
            self.isPaused = True

        else:
            return

    def Stop(self):
        """
           Stop player
        """
        self.drone.stop_video_stream()
        self.mediaplayer.stop()

    def OpenFile(self):

        filename = None
        filename = QFileDialog.getOpenFileName(self, "Open File", os.path.expanduser('~'))[0]
        if not filename:
            return
        #if sys.version < '3':
        #    filename = unicode(filename)
        self.media = self.instance.media_new(filename,":network-caching=100")
        print (self.media)
        self.mediaplayer.set_media(self.media)
        self.media.parse()
        #self.setWindowTitle(self.media.get_instance(0))
        if sys.platform.startswith('linux'):  # for Linux using the X Server
            self.mediaplayer.set_xwindow(self.videoframe.winId())
        elif sys.platform == "win32":  # for Windows
            self.mediaplayer.set_hwnd(self.videoframe.winId())
        elif sys.platform == "darwin":  # for MacOS
            self.mediaplayer.set_nsobject(int(self.videoframe.winId()))
        self.drone.start_video_stream()
        self.drone.set_video_stream_mode('low_latency')
        self.drone.set_video_stream_resolutions('rec1080_stream480')
        self.drone.set_vide_stream_framerate('25_FPS')
        self.Play()

    def showGPS(self):
        url_string = "file:///E:/SourceCode/pyparrot-master/pyparrot-master/ext/gps.html"
        self.gpsframe.load(QUrl(url_string))
