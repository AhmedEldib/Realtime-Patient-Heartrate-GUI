# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DSPV4.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1093, 828)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.EmptyButton = QtWidgets.QPushButton(self.centralwidget)
        self.EmptyButton.setObjectName("EmptyButton")
        self.gridLayout.addWidget(self.EmptyButton, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setMaximumSize(QtCore.QSize(28, 33))
        self.StartButton.setStyleSheet("")
        self.StartButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images.png/images.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StartButton.setIcon(icon)
        self.StartButton.setIconSize(QtCore.QSize(92, 78))
        self.StartButton.setObjectName("StartButton")
        self.verticalLayout.addWidget(self.StartButton)
        self.StopButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopButton.setMaximumSize(QtCore.QSize(28, 33))
        self.StopButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images.png/download.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StopButton.setIcon(icon1)
        self.StopButton.setIconSize(QtCore.QSize(88, 78))
        self.StopButton.setObjectName("StopButton")
        self.verticalLayout.addWidget(self.StopButton)
        self.gridLayout.addLayout(self.verticalLayout, 1, 3, 1, 1)
        self.HideButton = QtWidgets.QPushButton(self.centralwidget)
        self.HideButton.setObjectName("HideButton")
        self.gridLayout.addWidget(self.HideButton, 0, 2, 1, 1)
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setMaximumSize(QtCore.QSize(25, 25))
        self.ExitButton.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69))")
        self.ExitButton.setIconSize(QtCore.QSize(0, 0))
        self.ExitButton.setObjectName("ExitButton")
        self.gridLayout.addWidget(self.ExitButton, 0, 3, 1, 1)
        self.ImportButton = QtWidgets.QPushButton(self.centralwidget)
        self.ImportButton.setObjectName("ImportButton")
        self.gridLayout.addWidget(self.ImportButton, 0, 0, 1, 1)
        self.GraphicsView = PlotWidget(self.centralwidget)
        self.GraphicsView.setObjectName("GraphicsView")
        self.gridLayout.addWidget(self.GraphicsView, 1, 0, 1, 3)
        self.ImportButton.raise_()
        self.HideButton.raise_()
        self.EmptyButton.raise_()
        self.GraphicsView.raise_()
        self.ExitButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.EmptyButton.setText(_translate("MainWindow", "Empty Graph"))
        self.HideButton.setText(_translate("MainWindow", "Hide Graph"))
        self.ExitButton.setText(_translate("MainWindow", "Exit"))
        self.ImportButton.setText(_translate("MainWindow", "Browse"))
from pyqtgraph import PlotWidget
import UIAdditions_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
