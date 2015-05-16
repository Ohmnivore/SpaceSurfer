from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKitWidgets import *

class WebWidget(QObject):
    def __init__(self, tabsParent, inTab):
        super(WebWidget, self).__init__()
        self.tabs = tabsParent
        self.inTab = inTab
        self.isWebEngine = False

        if (self.isWebEngine):
            pass
        else:
            self.webK = QWebView(self.inTab)
            self.web = self.webK

        self.connectActions()

    def connectActions(self):
        self.web.titleChanged.connect(self.adjustTitle)
        self.web.loadProgress.connect(self.setProgress)
        self.web.loadStarted.connect(self.startLoading)
        self.web.loadFinished.connect(self.finishLoading)

    def addTo(self, layout):
        layout.addWidget(self.web)

    # Browser ops
    def parseUrl(self, url):
        if url.scheme() == '':
            url.setScheme('http')
        return url

    def setUrl(self, url):
        self.web.setUrl(self.parseUrl(url))

    def getUrl(self):
        return self.web.url()

    def getIcon(self):
        return self.web.icon()

    def goBack(self):
        self.web.history().back()

    def goNext(self):
        self.web.history().forward()

    def refresh(self):
        self.setUrl(self.getUrl())

    def stop(self):
        self.web.stop()

    def getTitle(self):
        return self.web.title()

    # Loading slots
    def setProgress(self, progress):
        if progress > 20: # Give the tab widget enough time to switch to the new one
            self.inTab.setTabTitle('   ' + str(progress) + '% ' + self.getTitle())

    def adjustTitle(self):
        self.inTab.setTabTitle('   ' + self.getTitle())

    def startLoading(self):
        self.inTab.setBtnCancel()

    def finishLoading(self, successful):
        self.adjustTitle()
        self.inTab.setBtnRefresh()
        self.inTab.setTabIcon(self.getIcon())
        self.inTab.ui.urlLine.setText(self.getUrl().toString())
