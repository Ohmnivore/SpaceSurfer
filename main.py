from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import *

from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWebKit import *

from mainwindow import *
from db import *

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    QNetworkProxyFactory.setUseSystemConfiguration(True)
    QWebSettings.enablePersistentStorage("storage")
    DB('appstorage/spacesurfer.db')

    w = MainWindow()
    w.showMaximized()

    sys.exit(app.exec_())
