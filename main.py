# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/AELION/AppData/Local/Temp/untitledhwOmpb.ui',
# licensing of 'C:/Users/AELION/AppData/Local/Temp/untitledhwOmpb.ui' applies.
#
# Created: Thu Jul 18 09:13:24 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PySide2.QtWidgets import (QApplication, QMainWindow)
from PySide2 import QtCore, QtWidgets
from PySide2.QtMultimediaWidgets import QVideoWidget
from PySide2.QtCore import QUrl
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent

def convertMillis(millis):
    seconds=(millis/1000)%60
    minutes=(millis/(1000*60))%60
    hours=(millis/(1000*60*60))%24

    return f'{int(hours):02}:{int(minutes):02}:{int(seconds):02}'

class Form(QMainWindow):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setObjectName("MainWindow")
        self.resize(804, 559)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.wVideo = QVideoWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wVideo.sizePolicy().hasHeightForWidth())
        self.wVideo.setSizePolicy(sizePolicy)
        self.wVideo.setObjectName("wVideo")
        self.verticalLayout.addWidget(self.wVideo)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lStartTime = QtWidgets.QLabel(self.centralwidget)
        self.lStartTime.setObjectName("lStartTime")
        self.horizontalLayout_2.addWidget(self.lStartTime)
        self.sProgression = QtWidgets.QSlider(self.centralwidget)
        self.sProgression.setOrientation(QtCore.Qt.Horizontal)
        self.sProgression.setObjectName("sProgression")
        self.horizontalLayout_2.addWidget(self.sProgression)
        self.lEndTime = QtWidgets.QLabel(self.centralwidget)
        self.lEndTime.setObjectName("lEndTime")
        self.horizontalLayout_2.addWidget(self.lEndTime)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lBoutons = QtWidgets.QHBoxLayout()
        self.lBoutons.setObjectName("lBoutons")
        self.pbLecture = QtWidgets.QPushButton(self.centralwidget)
        self.pbLecture.setObjectName("pbLecture")
        self.lBoutons.addWidget(self.pbLecture)
        self.pbPause = QtWidgets.QPushButton(self.centralwidget)
        self.pbPause.setObjectName("pbPause")
        self.lBoutons.addWidget(self.pbPause)
        self.pbStop = QtWidgets.QPushButton(self.centralwidget)
        self.pbStop.setObjectName("pbStop")
        self.lBoutons.addWidget(self.pbStop)
        self.pbSuivant = QtWidgets.QPushButton(self.centralwidget)
        self.pbSuivant.setObjectName("pbSuivant")
        self.lBoutons.addWidget(self.pbSuivant)
        self.pbPrecedent = QtWidgets.QPushButton(self.centralwidget)
        self.pbPrecedent.setObjectName("pbPrecedent")
        self.lBoutons.addWidget(self.pbPrecedent)
        self.verticalLayout.addLayout(self.lBoutons)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setBaseSize(QtCore.QSize(0, 0))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        spacerItem = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pbVolumePlus = QtWidgets.QPushButton(self.centralwidget)
        self.pbVolumePlus.setObjectName("pbVolumePlus")
        self.horizontalLayout_3.addWidget(self.pbVolumePlus)
        self.pbVolumeMoins = QtWidgets.QPushButton(self.centralwidget)
        self.pbVolumeMoins.setObjectName("pbVolumeMoins")
        self.horizontalLayout_3.addWidget(self.pbVolumeMoins)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.dVolume = QtWidgets.QDial(self.centralwidget)
        self.dVolume.setObjectName("dVolume")
        self.horizontalLayout_4.addWidget(self.dVolume)
        self.lPourcentVolume = QtWidgets.QLabel(self.centralwidget)
        self.lPourcentVolume.setObjectName("lPourcentVolume")
        self.horizontalLayout_4.addWidget(self.lPourcentVolume)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.mediaPlayer = QMediaPlayer()
        self.mediaPlayer.setVideoOutput(self.wVideo)

        self.pbLecture.clicked.connect(self.lectureClic)
        self.pbPause.clicked.connect(self.pauseClic)
        self.pbStop.clicked.connect(self.stopClic)
        self.pbSuivant.clicked.connect(self.suivantClic)
        self.pbPrecedent.clicked.connect(self.precedentClic)
        self.dVolume.valueChanged.connect(self.volumeChange)
        self.mediaPlayer.positionChanged.connect(self.progressionChange)
        self.sProgression.sliderMoved.connect(self.progressionDeplace)

        self.dVolume.setMaximum(100)
        self.dVolume.setWrapping(False)

        self.lEndTime.setText("")
        self.lStartTime.setText("")
        self.lPourcentVolume.setText("")
        self.dVolume.setValue(31)

    def progressionDeplace(self):
        self.mediaPlayer.setPosition(self.sProgression.value())

    def progressionChange(self):
        self.lEndTime.setText(convertMillis(self.mediaPlayer.duration()))
        self.lStartTime.setText(str(convertMillis(self.mediaPlayer.position())))
        self.sProgression.setRange(0, self.mediaPlayer.duration())
        self.sProgression.setValue(self.mediaPlayer.position())

    def lectureClic(self):
        mediaContent = QMediaContent(QUrl.fromLocalFile("big_buck_bunny.avi"))
        self.mediaPlayer.setMedia(mediaContent)
        self.mediaPlayer.play()

    def pauseClic(self):
        print("Pause")
        if self.mediaPlayer.state() == QMediaPlayer.PausedState:
            self.mediaPlayer.play()
        else:
            self.mediaPlayer.pause()

    def stopClic(self):
        self.mediaPlayer.stop()

    def suivantClic(self):
        print("Suivant")

    def precedentClic(self):
        print("Précédent")

    def volumeChange(self):
        self.lPourcentVolume.setText(str(self.dVolume.value()))
        self.mediaPlayer.setVolume(self.dVolume.value())

    def retranslateUi(self, MainWindow):
        self.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.lStartTime.setText(QtWidgets.QApplication.translate("MainWindow", "$start_time", None, -1))
        self.lEndTime.setText(QtWidgets.QApplication.translate("MainWindow", "$end_time", None, -1))
        self.pbLecture.setText(QtWidgets.QApplication.translate("MainWindow", "Lecture", None, -1))
        self.pbPause.setText(QtWidgets.QApplication.translate("MainWindow", "Pause", None, -1))
        self.pbStop.setText(QtWidgets.QApplication.translate("MainWindow", "Stop", None, -1))
        self.pbSuivant.setText(QtWidgets.QApplication.translate("MainWindow", "Suivant", None, -1))
        self.pbPrecedent.setText(QtWidgets.QApplication.translate("MainWindow", "Précédent", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Liste de lecture :", None, -1))
        self.pbVolumePlus.setText(QtWidgets.QApplication.translate("MainWindow", "+", None, -1))
        self.pbVolumeMoins.setText(QtWidgets.QApplication.translate("MainWindow", "-", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Volume :", None, -1))
        self.lPourcentVolume.setText(QtWidgets.QApplication.translate("MainWindow", "$volume", None, -1))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())
