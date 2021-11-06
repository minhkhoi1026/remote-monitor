import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from ServerGui import Ui_MainWindow
from server_socket import SocketServer, get_all_avail_host
from streaming import StreamingServer

class ServerWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        _translate = QtCore.QCoreApplication.translate
        self.main_win.setWindowTitle(_translate("MainWindow", "Server"))
        self.main_win.setWindowIcon(QIcon("image\\icon_window.png"))

        self.socket = SocketServer()
        self.stream_socket = StreamingServer()
        self.uic.button_start.clicked.connect(self.start)
        self.uic.button_stop.clicked.connect(self.stop)
        self.uic.button_stop.hide()
        self.add_item_IP()

    def show(self):
        self.main_win.show()

    def add_item_IP(self):
        self.uic.comboBox_IP.addItems(get_all_avail_host())

    def start(self):
        IP = self.uic.comboBox_IP.currentText()
        print(IP)
        self.socket.start_server(IP, 26100)
        self.stream_socket.start_server(IP, 9999)
        self.uic.comboBox_IP.setEnabled(False)
        self.uic.button_start.hide()
        self.uic.button_stop.show()

    def stop(self):
        self.socket.stop_server()
        self.stream_socket.stop_server()
        self.uic.comboBox_IP.setEnabled(True)
        self.uic.button_start.show()
        self.uic.button_stop.hide()


if __name__ == "__main__":
    # if not admin.isUserAdmin():
    #     admin.runAsAdmin()
    app = QApplication(sys.argv)
    main_win = ServerWindow()
    main_win.show()
    sys.exit(app.exec())

    
