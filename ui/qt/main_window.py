# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Fri Feb 19 12:21:06 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(574, 396)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_0 = QtGui.QPushButton(self.centralwidget)
        self.button_0.setMaximumSize(QtCore.QSize(48, 48))
        self.button_0.setObjectName("button_0")
        self.horizontalLayout_2.addWidget(self.button_0)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.button_4 = QtGui.QPushButton(self.centralwidget)
        self.button_4.setMaximumSize(QtCore.QSize(48, 48))
        self.button_4.setObjectName("button_4")
        self.horizontalLayout_2.addWidget(self.button_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_1 = QtGui.QPushButton(self.centralwidget)
        self.button_1.setMaximumSize(QtCore.QSize(48, 48))
        self.button_1.setObjectName("button_1")
        self.horizontalLayout_3.addWidget(self.button_1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.button_5 = QtGui.QPushButton(self.centralwidget)
        self.button_5.setMaximumSize(QtCore.QSize(48, 48))
        self.button_5.setObjectName("button_5")
        self.horizontalLayout_3.addWidget(self.button_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.button_2 = QtGui.QPushButton(self.centralwidget)
        self.button_2.setMaximumSize(QtCore.QSize(48, 48))
        self.button_2.setObjectName("button_2")
        self.horizontalLayout_5.addWidget(self.button_2)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.button_6 = QtGui.QPushButton(self.centralwidget)
        self.button_6.setMaximumSize(QtCore.QSize(48, 48))
        self.button_6.setObjectName("button_6")
        self.horizontalLayout_5.addWidget(self.button_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.button_3 = QtGui.QPushButton(self.centralwidget)
        self.button_3.setMaximumSize(QtCore.QSize(48, 48))
        self.button_3.setObjectName("button_3")
        self.horizontalLayout_6.addWidget(self.button_3)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.button_7 = QtGui.QPushButton(self.centralwidget)
        self.button_7.setMaximumSize(QtCore.QSize(48, 48))
        self.button_7.setObjectName("button_7")
        self.horizontalLayout_6.addWidget(self.button_7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 574, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.button_0.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_4.setText(QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.button_1.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.button_5.setText(QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.button_2.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.button_6.setText(QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.button_3.setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.button_7.setText(QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))

