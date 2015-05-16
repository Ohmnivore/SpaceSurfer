from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from webwidget import *
from ui_intab import Ui_Form

class InTab(QWidget):
    def __init__(self, tabParent):
        super(InTab, self).__init__(tabParent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.tabs = tabParent

        self.web = WebWidget(tabParent, self)
        self.web.addTo(self.ui.verticalLayout_2)
        self.connectActions()

        self.web.setUrl(QUrl('qrc:/display/assets/display/astro.html'))
        QTimer.singleShot(0, self.ui.urlLine.setFocus)

    def connectActions(self):
        self.ui.urlLine.returnPressed.connect(self.goToUrl)
        self.ui.prevBtn.pressed.connect(self.web.goBack)
        self.ui.nextBtn.pressed.connect(self.web.goNext)
        self.setBtnRefresh()

    def goToUrl(self):
        self.web.setUrl(QUrl(self.ui.urlLine.text()))

    def setTabTitle(self, s):
        index = self.tabs.indexOf(self)
        self.tabs.setTabText(index, s)

    def setTabIcon(self, icon):
        index = self.tabs.indexOf(self)
        self.tabs.setTabIcon(index, icon)

    def setBtnCancel(self):
        self.ui.refreshBtn.setIcon(QIcon(':/icons/assets/images/dark/appbar.close.png'))
        self.ui.refreshBtn.pressed.disconnect(self.web.refresh)
        self.ui.refreshBtn.pressed.connect(self.web.stop)

    def setBtnRefresh(self):
        self.ui.refreshBtn.setIcon(QIcon(':/icons/assets/images/dark/appbar.refresh.png'))
        if self.ui.refreshBtn.receivers(self.ui.refreshBtn.pressed) > 0:
            self.ui.refreshBtn.pressed.disconnect(self.web.stop)
        self.ui.refreshBtn.pressed.connect(self.web.refresh)
