# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from lib.utils import MyGraphicsView


class Ui_VideoOCR(object):
    def setupUi(self, VideoOCR):
        VideoOCR.setObjectName("VideoOCR")
        VideoOCR.resize(981, 579)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        VideoOCR.setFont(font)
        self.centralwidget = QtWidgets.QWidget(VideoOCR)
        self.centralwidget.setObjectName("centralwidget")
        self.genTime = QtWidgets.QPushButton(self.centralwidget)
        self.genTime.setGeometry(QtCore.QRect(840, 230, 100, 32))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.genTime.setFont(font)
        self.genTime.setObjectName("genTime")
        self.genSub = QtWidgets.QPushButton(self.centralwidget)
        self.genSub.setGeometry(QtCore.QRect(840, 320, 100, 32))
        self.genSub.setObjectName("genSub")
        self.saveFrames = QtWidgets.QCheckBox(self.centralwidget)
        self.saveFrames.setGeometry(QtCore.QRect(630, 225, 71, 40))
        self.saveFrames.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.saveFrames.setObjectName("saveFrames")
        self.ocrMethod = QtWidgets.QComboBox(self.centralwidget)
        self.ocrMethod.setGeometry(QtCore.QRect(720, 320, 100, 30))
        self.ocrMethod.setObjectName("ocrMethod")
        self.ocrMethod.addItem("")
        self.ocrMethod.addItem("")
        self.ocrMethod.addItem("")
        self.minValue = QtWidgets.QLineEdit(self.centralwidget)
        self.minValue.setGeometry(QtCore.QRect(720, 111, 100, 21))
        self.minValue.setAlignment(QtCore.Qt.AlignCenter)
        self.minValue.setObjectName("minValue")
        self.segMethod = QtWidgets.QComboBox(self.centralwidget)
        self.segMethod.setGeometry(QtCore.QRect(720, 30, 100, 30))
        self.segMethod.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.segMethod.setObjectName("segMethod")
        self.segMethod.addItem("")
        self.segMethod.addItem("")
        self.isSrt = QtWidgets.QLabel(self.centralwidget)
        self.isSrt.setGeometry(QtCore.QRect(400, 500, 200, 21))
        self.isSrt.setAlignment(QtCore.Qt.AlignCenter)
        self.isSrt.setObjectName("isSrt")
        self.srtLabel = QtWidgets.QLabel(self.centralwidget)
        self.srtLabel.setGeometry(QtCore.QRect(620, 151, 72, 15))
        self.srtLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.srtLabel.setObjectName("srtLabel")
        self.chgLabel = QtWidgets.QLabel(self.centralwidget)
        self.chgLabel.setGeometry(QtCore.QRect(610, 191, 81, 20))
        self.chgLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.chgLabel.setObjectName("chgLabel")
        self.srtThres = QtWidgets.QLineEdit(self.centralwidget)
        self.srtThres.setGeometry(QtCore.QRect(720, 151, 100, 21))
        self.srtThres.setAlignment(QtCore.Qt.AlignCenter)
        self.srtThres.setObjectName("srtThres")
        self.chgThres = QtWidgets.QLineEdit(self.centralwidget)
        self.chgThres.setGeometry(QtCore.QRect(720, 191, 100, 21))
        self.chgThres.setAlignment(QtCore.Qt.AlignCenter)
        self.chgThres.setObjectName("chgThres")
        self.videoBar = QtWidgets.QSlider(self.centralwidget)
        self.videoBar.setGeometry(QtCore.QRect(20, 350, 560, 22))
        self.videoBar.setOrientation(QtCore.Qt.Horizontal)
        self.videoBar.setObjectName("videoBar")
        self.maxValue = QtWidgets.QLineEdit(self.centralwidget)
        self.maxValue.setGeometry(QtCore.QRect(720, 71, 100, 21))
        self.maxValue.setAlignment(QtCore.Qt.AlignCenter)
        self.maxValue.setObjectName("maxValue")
        self.testButton = QtWidgets.QPushButton(self.centralwidget)
        self.testButton.setGeometry(QtCore.QRect(720, 230, 100, 32))
        self.testButton.setObjectName("testButton")
        self.maxLabel = QtWidgets.QLabel(self.centralwidget)
        self.maxLabel.setGeometry(QtCore.QRect(620, 71, 72, 20))
        self.maxLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.maxLabel.setObjectName("maxLabel")
        self.minLabel = QtWidgets.QLabel(self.centralwidget)
        self.minLabel.setGeometry(QtCore.QRect(610, 111, 81, 20))
        self.minLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.minLabel.setObjectName("minLabel")
        # self.videoView = QtWidgets.QGraphicsView(self.centralwidget)
        self.videoView = MyGraphicsView(self.centralwidget)
        self.videoView.setGeometry(QtCore.QRect(20, 20, 560, 325))
        self.videoView.setObjectName("videoView")
        self.clipView = MyGraphicsView(self.centralwidget)
        self.clipView.setGeometry(QtCore.QRect(20, 390, 931, 100))
        self.clipView.setObjectName("clipView")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(630, 280, 321, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.langBox = QtWidgets.QComboBox(self.centralwidget)
        self.langBox.setGeometry(QtCore.QRect(630, 320, 75, 30))
        self.langBox.setObjectName("langBox")
        self.langBox.addItem("")
        self.langBox.addItem("")
        self.langBox.addItem("")
        self.colorButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.colorButton1.setGeometry(QtCore.QRect(840, 70, 100, 24))
        self.colorButton1.setObjectName("colorButton1")
        self.colorButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.colorButton2.setGeometry(QtCore.QRect(840, 110, 100, 24))
        self.colorButton2.setObjectName("colorButton2")
        VideoOCR.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VideoOCR)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 981, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        VideoOCR.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VideoOCR)
        self.statusbar.setObjectName("statusbar")
        VideoOCR.setStatusBar(self.statusbar)
        self.openFile = QtWidgets.QAction(VideoOCR)
        self.openFile.setObjectName("openFile")
        self.menu.addAction(self.openFile)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(VideoOCR)
        QtCore.QMetaObject.connectSlotsByName(VideoOCR)

    def retranslateUi(self, VideoOCR):
        _translate = QtCore.QCoreApplication.translate
        VideoOCR.setWindowTitle(_translate("VideoOCR", "Video OCR"))
        self.genTime.setText(_translate("VideoOCR", "生成时间轴"))
        self.genSub.setText(_translate("VideoOCR", "生成字幕"))
        self.saveFrames.setText(_translate("VideoOCR", "保存帧"))
        self.ocrMethod.setItemText(0, _translate("VideoOCR", "paddle"))
        self.ocrMethod.setItemText(1, _translate("VideoOCR", "easy"))
        self.ocrMethod.setItemText(2, _translate("VideoOCR", "online"))
        self.minValue.setText(_translate("VideoOCR", "150,150,150"))
        self.segMethod.setItemText(0, _translate("VideoOCR", "RGB"))
        self.segMethod.setItemText(1, _translate("VideoOCR", "HSV"))
        self.isSrt.setText(_translate("VideoOCR", "检测结果: 该帧不包含字幕"))
        self.srtLabel.setText(_translate("VideoOCR", "字幕阈值"))
        self.chgLabel.setText(_translate("VideoOCR", "切换阈值"))
        self.srtThres.setText(_translate("VideoOCR", "1.0"))
        self.chgThres.setText(_translate("VideoOCR", "5.0"))
        self.maxValue.setText(_translate("VideoOCR", "255,255,255"))
        self.testButton.setText(_translate("VideoOCR", "测试参数"))
        self.maxLabel.setText(_translate("VideoOCR", "颜色上界"))
        self.minLabel.setText(_translate("VideoOCR", "颜色下界"))
        self.langBox.setItemText(0, _translate("VideoOCR", "ch_sim"))
        self.langBox.setItemText(1, _translate("VideoOCR", "en"))
        self.langBox.setItemText(2, _translate("VideoOCR", "dual"))
        self.colorButton1.setText(_translate("VideoOCR", "调色板"))
        self.colorButton2.setText(_translate("VideoOCR", "调色板"))
        self.menu.setTitle(_translate("VideoOCR", "文件"))
        self.openFile.setText(_translate("VideoOCR", "打开视频"))
