from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sip
from ui_mainwindow import Ui_MainWindow
from intab import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tabWidget.tabBar().setDrawBase(False)

        self.addNewTabButton()
        self.connectActions()
        self.closeTab(0)
        self.newTab()
        # ui.menuBar.hide();

    def addNewTabButton(self):
        tb = QPushButton()
        tb.setObjectName('addTabBtn')
        tb.setIcon(QIcon(':/icons/assets/images/dark/appbar.add.png'))
        self.ui.tabWidget.setCornerWidget(tb)

    def connectActions(self):
        # QShortcut *sh = new QShortcut(QKeySequence(tr("Ctrl+N", "File|Open")), this);
        # QObject::connect(sh, SIGNAL(activated()), this, SLOT(newTab()));
        # Base UI
        self.ui.tabWidget.tabCloseRequested.connect(self.closeTab)
        self.ui.tabWidget.cornerWidget().pressed.connect(self.newTab)

        # Actions
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionNew_Tab.triggered.connect(self.newTab)

    def newTab(self):
        index = self.ui.tabWidget.addTab(InTab(self.ui.tabWidget), "New Tab")
        self.ui.tabWidget.setCurrentIndex(index)

    def closeTab(self, index):
        child = self.ui.tabWidget.widget(index)
        self.ui.tabWidget.removeTab(index)
        sip.delete(child)
        child = None
