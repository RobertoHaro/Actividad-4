# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(288, 296)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.out_plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.out_plainTextEdit.setObjectName(u"out_plainTextEdit")

        self.gridLayout_2.addWidget(self.out_plainTextEdit, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.speed_spinBox = QSpinBox(self.groupBox)
        self.speed_spinBox.setObjectName(u"speed_spinBox")
        self.speed_spinBox.setMaximum(10000)
        self.speed_spinBox.setDisplayIntegerBase(10)

        self.gridLayout.addWidget(self.speed_spinBox, 2, 1, 1, 1)

        self.red_spinBox = QSpinBox(self.groupBox)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.red_spinBox, 3, 1, 1, 1)

        self.destinyX_spinBox = QSpinBox(self.groupBox)
        self.destinyX_spinBox.setObjectName(u"destinyX_spinBox")
        self.destinyX_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destinyX_spinBox, 0, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.destinyY_spinBox = QSpinBox(self.groupBox)
        self.destinyY_spinBox.setObjectName(u"destinyY_spinBox")
        self.destinyY_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destinyY_spinBox, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.blue__spinBox = QSpinBox(self.groupBox)
        self.blue__spinBox.setObjectName(u"blue__spinBox")
        self.blue__spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.blue__spinBox, 5, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.green_spinBox = QSpinBox(self.groupBox)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.green_spinBox, 4, 1, 1, 1)

        self.agregar_pushButton = QPushButton(self.groupBox)
        self.agregar_pushButton.setObjectName(u"agregar_pushButton")

        self.gridLayout.addWidget(self.agregar_pushButton, 7, 0, 1, 2)

        self.mostrar_pushButton = QPushButton(self.groupBox)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout.addWidget(self.mostrar_pushButton, 8, 0, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 288, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particula", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Destino x", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Destino y", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.agregar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
    # retranslateUi

