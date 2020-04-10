# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np 
import pyautogui
import cv2
import os
import pygetwindow as gw 
import time
import threading


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 167)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(-10, 0, 861, 51))

        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setStyleSheet("background-color: black")
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 80, 221, 31))
        self.pushButton.setStyleSheet("font: 75 10pt \"Consolas\";")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 80, 181, 31))
        self.pushButton_2.setStyleSheet("font: 75 10pt \"Consolas\";")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 80, 201, 31))
        self.pushButton_3.setStyleSheet("\n""font: 75 10pt \"Consolas\";")
        self.pushButton_3.setObjectName("pushButton_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Screen Capture V-0.1</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Start screen Recording"))
        self.pushButton.clicked.connect(self.screen_record)

        self.pushButton_2.setText(_translate("MainWindow", "Take a Screenshot"))
        self.pushButton_2.clicked.connect(self.screen_shot)

        self.pushButton_3.setText(_translate("MainWindow", "Stop Screen Recording"))
        self.pushButton_3.clicked.connect(self.screen_stop)


    def screen_record(self):
        self.flag = 0

        self.tomin = gw.getWindowsWithTitle('MainWindow')[0]
        self.tomin.minimize()
        time.sleep(1)

        self.SCREEN_SIZE = pyautogui.size()
        fourcc = cv2.VideoWriter_fourcc(*"XVID")

        self.path_1 = os.path.dirname(os.path.abspath(__file__))
        self.store_1 = os.path.join(self.path_1,"ScreenRecording")
        j = 0
        if os.path.isdir(self.store_1):
            while os.path.exists(self.store_1 + "\\output%s.avi" % j):
                j+=1
            self.out = cv2.VideoWriter(self.store_1 + "\\output%s.avi" %j, fourcc, 24.0, (self.SCREEN_SIZE))
        else:
            os.mkdir(self.store_1)
            self.out = cv2.VideoWriter(self.store_1 + "\\output%s.avi" %j, fourcc, 24.0, (self.SCREEN_SIZE))
        
        self.x = threading.Thread(target=self.do_work, args=(1,))
        self.x.start()

    def do_work(self,name):
        while True:
            i = pyautogui.screenshot()
            frame = np.array(i)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.out.write(frame)
            if  self.flag==1:
                cv2.destroyAllWindows()
                self.out.release()
                break
                


    def screen_stop(self):
        # self.pushButton_3.setEnabled(True)
        self.flag = 1
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Task Completed")
        msg.setText("Recording Completed")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setStandardButtons(QtWidgets.QMessageBox.Close)
        self.x = msg.exec_()
    

    def screen_shot(self):
        self.tomin = gw.getWindowsWithTitle('MainWindow')[0]
        self.tomin.minimize()
        time.sleep(1)
        self.shot = pyautogui.screenshot()
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.store = os.path.join(self.path,"ScreenShot")
        i=0
        if os.path.isdir(self.store):
            while os.path.exists(self.store + "\\picture%s.png" % i):
                i+=1
            self.shot.save(self.store + "\\picture%s.png" %i)
        else:
             os.mkdir(self.store)
             self.shot.save(self.store + "\\picture%s.png" %i)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
