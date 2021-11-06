#install pyqt5:
#                       pip install pyqt5
#                       pip install pyqt5-tools

#command make python file:
#                       pyuic5 -x Client.ui -o ClientGui.py
#                       pyuic5 -x Server.ui -o ServerGui.py
#                       pyrcc5 picture.qrc -o picture_rc.py

#run app:
#                       python ClientGui.py
#                       python main.py
#        & C:/Users/Dell/AppData/Local/Microsoft/WindowsApps/python3.10.exe
#        & C:/Users/Dell/AppData/Local/Microsoft/WindowsApps/pip3.10.exe install

#run server
# & C:/Users/Dell/AppData/Local/Microsoft/WindowsApps/python3.10.exe d:/Subject/nam2_hk2/Mang_may_tinh/cuoiki_socket/mybotnet/server_socket.py
#run client
# & C:/Users/Dell/AppData/Local/Microsoft/WindowsApps/python3.10.exe d:/Subject/nam2_hk2/Mang_may_tinh/cuoiki_socket/mybotnet/client_socket.py

#open Designer:
#               C:\Users\Dell\AppData\Roaming\Python\Python37\site-packages\qt5_applications\Qt\bin


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel, QSizePolicy
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from ServerGui import Ui_MainWindow
from server_socket import SocketServer
from streaming import StreamingServer
import admin

class ServerWindow:
    def __init__(self, socket):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.socket = SocketServer()
        self.stream_socket = StreamingServer()
        self.uic.button_start.clicked.connect(self.start)
        self.uic.button_stop.clicked.connect(self.stop)
        self.uic.button_stop.setEnabled(False)

    def show(self):
        self.main_win.show()

    def start(self):
        self.socket.start_server('127.0.0.1', 26100)
        self.stream_socket.start_server('127.0.0.1', 9999)
        self.uic.button_start.setEnabled(False)
        self.uic.button_stop.setEnabled(True)

    def stop(self):
        self.socket.stop_server()
        self.stream_socket.stop_server()
        self.uic.button_start.setEnabled(True)
        self.uic.button_stop.setEnabled(False)


if __name__ == "__main__":
    if not admin.isUserAdmin():
        admin.runAsAdmin()
    app = QApplication(sys.argv)
    main_win = ServerWindow(None)
    main_win.show()
    sys.exit(app.exec())

    



