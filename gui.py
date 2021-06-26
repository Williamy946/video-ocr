# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VideoOCR(object):
    def setupUi(self, VideoOCR):
        VideoOCR.setObjectName("VideoOCR")
        VideoOCR.resize(1013, 579)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        VideoOCR.setFont(font)
        self.centralwidget = QtWidgets.QWidget(VideoOCR)
        self.centralwidget.setObjectName("centralwidget")
        self.genTime = QtWidgets.QPushButton(self.centralwidget)
        self.genTime.setGeometry(QtCore.QRect(809, 429, 110, 32))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.genTime.setFont(font)
        self.genTime.setObjectName("genTime")
        self.genSub = QtWidgets.QPushButton(self.centralwidget)
        self.genSub.setGeometry(QtCore.QRect(340, 429, 110, 32))
        self.genSub.setObjectName("genSub")
        self.saveFrames = QtWidgets.QCheckBox(self.centralwidget)
        self.saveFrames.setGeometry(QtCore.QRect(699, 425, 101, 41))
        self.saveFrames.setObjectName("saveFrames")
        self.ocrMethod = QtWidgets.QComboBox(self.centralwidget)
        self.ocrMethod.setGeometry(QtCore.QRect(140, 430, 87, 30))
        self.ocrMethod.setObjectName("ocrMethod")
        self.ocrMethod.addItem("")
        self.ocrMethod.addItem("")
        self.ocrMethod.addItem("")
        self.minValue = QtWidgets.QLineEdit(self.centralwidget)
        self.minValue.setGeometry(QtCore.QRect(809, 290, 110, 21))
        self.minValue.setObjectName("minValue")
        self.segMethod = QtWidgets.QComboBox(self.centralwidget)
        self.segMethod.setGeometry(QtCore.QRect(709, 201, 87, 30))
        self.segMethod.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.segMethod.setObjectName("segMethod")
        self.segMethod.addItem("")
        self.segMethod.addItem("")
        self.isSrt = QtWidgets.QLabel(self.centralwidget)
        self.isSrt.setGeometry(QtCore.QRect(709, 140, 201, 21))
        self.isSrt.setAlignment(QtCore.Qt.AlignCenter)
        self.isSrt.setObjectName("isSrt")
        self.srtLabel = QtWidgets.QLabel(self.centralwidget)
        self.srtLabel.setGeometry(QtCore.QRect(719, 330, 72, 15))
        self.srtLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.srtLabel.setObjectName("srtLabel")
        self.chgLabel = QtWidgets.QLabel(self.centralwidget)
        self.chgLabel.setGeometry(QtCore.QRect(710, 370, 81, 20))
        self.chgLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.chgLabel.setObjectName("chgLabel")
        self.srtThres = QtWidgets.QLineEdit(self.centralwidget)
        self.srtThres.setGeometry(QtCore.QRect(809, 330, 110, 21))
        self.srtThres.setAlignment(QtCore.Qt.AlignCenter)
        self.srtThres.setObjectName("srtThres")
        self.chgThres = QtWidgets.QLineEdit(self.centralwidget)
        self.chgThres.setGeometry(QtCore.QRect(809, 370, 110, 21))
        self.chgThres.setAlignment(QtCore.Qt.AlignCenter)
        self.chgThres.setObjectName("chgThres")
        self.videoBar = QtWidgets.QSlider(self.centralwidget)
        self.videoBar.setGeometry(QtCore.QRect(20, 370, 560, 22))
        self.videoBar.setOrientation(QtCore.Qt.Horizontal)
        self.videoBar.setObjectName("videoBar")
        self.maxValue = QtWidgets.QLineEdit(self.centralwidget)
        self.maxValue.setGeometry(QtCore.QRect(809, 250, 110, 21))
        self.maxValue.setObjectName("maxValue")
        self.testButton = QtWidgets.QPushButton(self.centralwidget)
        self.testButton.setGeometry(QtCore.QRect(809, 200, 110, 32))
        self.testButton.setObjectName("testButton")
        self.maxLabel = QtWidgets.QLabel(self.centralwidget)
        self.maxLabel.setGeometry(QtCore.QRect(719, 250, 72, 20))
        self.maxLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.maxLabel.setObjectName("maxLabel")
        self.minLabel = QtWidgets.QLabel(self.centralwidget)
        self.minLabel.setGeometry(QtCore.QRect(710, 290, 81, 20))
        self.minLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.minLabel.setObjectName("minLabel")
        self.videoView = QtWidgets.QGraphicsView(self.centralwidget)
        self.videoView.setGeometry(QtCore.QRect(20, 30, 560, 325))
        self.videoView.setObjectName("videoView")
        self.clipView = QtWidgets.QGraphicsView(self.centralwidget)
        self.clipView.setGeometry(QtCore.QRect(625, 30, 371, 100))
        self.clipView.setObjectName("clipView")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(140, 480, 791, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.langBox = QtWidgets.QComboBox(self.centralwidget)
        self.langBox.setGeometry(QtCore.QRect(240, 430, 87, 30))
        self.langBox.setObjectName("langBox")
        self.langBox.addItem("")
        self.langBox.addItem("")
        self.langBox.addItem("")
        VideoOCR.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VideoOCR)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1013, 26))
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
        self.saveFrames.setText(_translate("VideoOCR", "保存字幕帧"))
        self.ocrMethod.setItemText(0, _translate("VideoOCR", "paddle"))
        self.ocrMethod.setItemText(1, _translate("VideoOCR", "easy"))
        self.ocrMethod.setItemText(2, _translate("VideoOCR", "online"))
        self.minValue.setText(_translate("VideoOCR", "150,150,150"))
        self.segMethod.setItemText(0, _translate("VideoOCR", "RGB"))
        self.segMethod.setItemText(1, _translate("VideoOCR", "HSV"))
        self.isSrt.setText(_translate("VideoOCR", "检测结果: 该帧不包含字幕"))
        self.srtLabel.setText(_translate("VideoOCR", "字幕阈值"))
        self.chgLabel.setText(_translate("VideoOCR", "新字幕阈值"))
        self.srtThres.setText(_translate("VideoOCR", "1.0"))
        self.chgThres.setText(_translate("VideoOCR", "5.0"))
        self.maxValue.setText(_translate("VideoOCR", "255,255,255"))
        self.testButton.setText(_translate("VideoOCR", "测试参数"))
        self.maxLabel.setText(_translate("VideoOCR", "颜色上界"))
        self.minLabel.setText(_translate("VideoOCR", "颜色下界"))
        self.langBox.setItemText(0, _translate("VideoOCR", "ch_sim"))
        self.langBox.setItemText(1, _translate("VideoOCR", "en"))
        self.langBox.setItemText(2, _translate("VideoOCR", "dual"))
        self.menu.setTitle(_translate("VideoOCR", "文件"))
        self.openFile.setText(_translate("VideoOCR", "打开视频"))
