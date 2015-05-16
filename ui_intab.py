# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'intab.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.prevBtn = QtWidgets.QPushButton(Form)
        self.prevBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/assets/images/dark/appbar.chevron.left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prevBtn.setIcon(icon)
        self.prevBtn.setIconSize(QtCore.QSize(32, 32))
        self.prevBtn.setObjectName("prevBtn")
        self.horizontalLayout.addWidget(self.prevBtn)
        self.nextBtn = QtWidgets.QPushButton(Form)
        self.nextBtn.setStyleSheet("")
        self.nextBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/assets/images/dark/appbar.chevron.right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextBtn.setIcon(icon1)
        self.nextBtn.setIconSize(QtCore.QSize(32, 32))
        self.nextBtn.setObjectName("nextBtn")
        self.horizontalLayout.addWidget(self.nextBtn)
        self.urlLine = QtWidgets.QLineEdit(Form)
        self.urlLine.setDragEnabled(False)
        self.urlLine.setPlaceholderText("")
        self.urlLine.setObjectName("urlLine")
        self.horizontalLayout.addWidget(self.urlLine)
        self.refreshBtn = QtWidgets.QPushButton(Form)
        self.refreshBtn.setEnabled(True)
        self.refreshBtn.setStyleSheet("")
        self.refreshBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/assets/images/dark/appbar.refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshBtn.setIcon(icon2)
        self.refreshBtn.setIconSize(QtCore.QSize(32, 32))
        self.refreshBtn.setObjectName("refreshBtn")
        self.horizontalLayout.addWidget(self.refreshBtn)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/assets/images/dark/appbar.star.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/assets/images/dark/appbar.rocket.rotated.45.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

import gui_rc
