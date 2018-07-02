# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class MyDroneGUI(object):
    def __init__(self,drone,MainWindow):
        self.drone = drone
        self.MainWindow = MainWindow
        self.setupUi(self.MainWindow)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 230, 75, 23))
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoRepeatDelay(100)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.drone.safe_takeoff(1))
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 130, 75, 23))
        self.pushButton_2.setAutoRepeat(True)
        self.pushButton_2.setAutoRepeatDelay(100)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda :self.drone.fly_no_duration(roll=-50, pitch=0, yaw=0, vertical_movement=0))
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 180, 75, 23))
        self.pushButton_3.setAutoRepeat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda :self.drone.fly_no_duration(roll=0, pitch=0, yaw=0, vertical_movement=50))
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 130, 75, 23))
        self.pushButton_4.setAutoRepeat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda :self.drone.fly_no_duration(roll=50, pitch=0, yaw=0, vertical_movement=0))
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(180, 100, 75, 23))
        self.pushButton_5.setAutoRepeat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda :self.drone.fly_no_duration(roll=0, pitch=50, yaw=0, vertical_movement=0))
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(280, 180, 75, 23))
        self.pushButton_6.setAutoRepeat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(lambda :self.drone.fly_no_duration(roll=0, pitch=0, yaw=0, vertical_movement=-50))
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(280, 70, 75, 23))
        self.pushButton_7.setAutoRepeat(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(lambda :self.drone.fly_no_duration(roll=0, pitch=0, yaw=50, vertical_movement=0))
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(80, 70, 75, 23))
        self.pushButton_8.setAutoRepeat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(lambda :self.drone.fly_no_duration(roll=0, pitch=0, yaw=-50, vertical_movement=0))
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(180, 180, 75, 23))
        self.pushButton_9.setAutoRepeat(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(lambda :self.drone.fly_no_duration(roll=0, pitch=-50, yaw=0, vertical_movement=0))
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(280, 230, 75, 23))
        self.pushButton_10.setAutoRepeat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(lambda: self.drone.safe_land(1))
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "起飞"))
        self.pushButton_2.setText(_translate("MainWindow", "左"))
        self.pushButton_3.setText(_translate("MainWindow", "上"))
        self.pushButton_4.setText(_translate("MainWindow", "右"))
        self.pushButton_5.setText(_translate("MainWindow", "前"))
        self.pushButton_6.setText(_translate("MainWindow", "下"))
        self.pushButton_7.setText(_translate("MainWindow", "右旋"))
        self.pushButton_8.setText(_translate("MainWindow", "左旋"))
        self.pushButton_9.setText(_translate("MainWindow", "后"))
        self.pushButton_10.setText(_translate("MainWindow", "降落"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))

    def mobao(self,n):
        print("hello world {0}".format(n))