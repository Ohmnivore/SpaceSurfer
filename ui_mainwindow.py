# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 311)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/assets/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QPushButton, QTabBar::tab, QMenu, QTabBar QToolButton {\n"
"    background-color: #1d1d1d;\n"
"    color: white;\n"
"    border: none;\n"
"    \n"
"    font-family: \"Gisha\";\n"
"    font-weight: bold;\n"
"    font-size:14px;\n"
"}\n"
"QPushButton:hover, QTabBar::tab:hover, QTabBar QToolButton::hover {\n"
"    background-color: #2d2d2d;\n"
"}\n"
"QPushButton:pressed, QTabBar::tab:selected, QMenu:selected, QTabBar QToolButton::selected {\n"
"    background-color: #7d6aad;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    padding-left: 8px;\n"
"    width: 180px;\n"
"    height: 32px;\n"
"}\n"
"QPushButton {\n"
"    height: 32px;\n"
"}\n"
"\n"
"QMenu {\n"
"    border: none;\n"
"}\n"
"QMenu::item, QMenu::item::icon {\n"
"    padding: 2px 20px 2px 20px;\n"
"    height: 32px;\n"
"    border: none;\n"
"}\n"
"\n"
"QMainWindow, QFrame, QTabWidget, QWebView {\n"
"    background-color: #1d1d1d;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid #1d1d1d;\n"
"    border-top: 0px;\n"
"    border-right: 0px;\n"
"    border-left: 0px;\n"
"    margin-top: 0px;\n"
"    height: 31px;\n"
"    \n"
"    font-family: \"Gisha\";\n"
"    font-weight: bold;\n"
"    font-size:14px;\n"
"}\n"
"\n"
"QPushButton#prevBtn, QPushButton#nextBtn {\n"
"    width: 45px;\n"
"}\n"
"\n"
"QTabWidget QWidget#addTabBtn, QTabBar QToolButton {\n"
"    height: 32px;\n"
"    width: 36px;\n"
"}\n"
"QTabBar::scroller {\n"
"    height: 32px;\n"
"    width: 36px;\n"
"}\n"
"QTabBar QToolButton::right-arrow { \n"
"    image: url(assets/images/dark/appbar.chevron.right.png);\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow {\n"
"    image: url(assets/images/dark/appbar.chevron.left.png);\n"
"}\n"
"")
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AnimatedDocks)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(80, 110, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Gisha")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menuBar.setDefaultUp(False)
        self.menuBar.setNativeMenuBar(False)
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setTearOffEnabled(False)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/assets/images/dark/appbar.close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setObjectName("actionExit")
        self.actionNew_Tab = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/assets/images/dark/appbar.add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Tab.setIcon(icon2)
        self.actionNew_Tab.setObjectName("actionNew_Tab")
        self.menuFile.addAction(self.actionNew_Tab)
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Space Surfer, yo"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "123456789 10 11 12 13"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionNew_Tab.setText(_translate("MainWindow", "New Tab"))
        self.actionNew_Tab.setShortcut(_translate("MainWindow", "Ctrl+T"))

import gui_rc
