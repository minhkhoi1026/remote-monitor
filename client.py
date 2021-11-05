
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel, QSizePolicy
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from ClientGui import Ui_MainWindow
from client_socket import SocketClient
from streaming import StreamingClient
from ClTaskManager import ClTaskManager
from ClFileManagement import ClFileManagement
from ClAddress import ClAddress


class ClientWindow:
    def __init__(self, socket):
        # --- create window ---
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.hide_widgets()
        self.connection()

        # --- create socket ---
        self.socket = SocketClient()
        self.WidgetTaskManager=ClTaskManager(self.socket,self.uic)
        self.WidgetFileManagemnet=ClFileManagement(self.socket,self.uic)
        self.WidgetAddress=ClAddress(self.socket,self.uic)

        # --- create connection between button and widget ---
        self.uic.button_connection.clicked.connect(self.connection)
        self.uic.button_connect.clicked.connect(self.connect)
        self.uic.button_disconnect.clicked.connect(self.disconnect)

        self.uic.button_screen_stream.clicked.connect(self.screen_stream)
        self.uic.button_address.clicked.connect(self.address)
        self.uic.button_task_manager.clicked.connect(self.task_manager)
        self.uic.button_file_explorer.clicked.connect(self.file_explorer)
        


        self.uic.button_control_input.clicked.connect(self.control_input)
        self.uic.button_lock_input.clicked.connect(self.lock_input)
        self.uic.button_unlock_input.clicked.connect(self.unlock_input)
        self.uic.button_start_keylogger.clicked.connect(self.start_keylogger)
        self.uic.button_stop_keylogger.clicked.connect(self.stop_keylogger)
        self.uic.button_save_keylog.clicked.connect(self.save_keylog)

        self.uic.button_logout_n_shutdown.clicked.connect(self.logout_n_shutdown)
        self.uic.button_logout.clicked.connect(self.logout)
        self.uic.button_shutdown.clicked.connect(self.shutdown)

        # --- other ---
        self.uic.label_connect_icon.hide()
        self.uic.label_connect_note.hide()
        self.uic.button_disconnect.hide()
        self.uic.button_unlock_input.hide()
 
    def show(self):
        self.main_win.show()

    def hide_widgets(self):
        self.uic.widget_connection.hide()
        self.uic.widget_screen_stream.hide()
        self.uic.widget_address.hide()
        self.uic.widget_task_manager.hide()
        self.uic.widget_file_explorer.hide()
        self.uic.widget_control_input.hide()
        self.uic.widget_logout_n_shutdown.hide()
        pass

    #----- Code Area -----
    def connection(self):
        self.hide_widgets()
        self.uic.widget_connection.show()
    def connect(self):
        IP = self.uic.edit_IP.text().strip()
        cn1 = self.socket.connect(IP,26100)

        self.uic.label_connect_icon.show()
        self.uic.label_connect_note.show()
        
        if cn1:
        #connect successfully
            self.uic.edit_IP.setEnabled(False)
            self.uic.button_connect.hide()
            self.uic.button_disconnect.show()
            self.uic.label_connect_icon.setStyleSheet("image: url(:/image/image/icon_success.png);")
            self.uic.label_connect_note.setText("Successful Connection")

            self.screen_start_stream()
        else:
        #connect failed
            self.uic.label_connect_icon.setStyleSheet("image: url(:/image/image/icon_fail.png);")
            self.uic.label_connect_note.setText("Connection Failed")
    def disconnect(self):
        self.socket.disconnect()
        self.uic.edit_IP.setEnabled(True)
        self.uic.button_connect.show()
        self.uic.button_disconnect.hide()
        self.uic.label_connect_icon.hide()
        self.uic.label_connect_note.hide()


    #----- Code Area -----
    def screen_stream(self):
        self.hide_widgets()
        self.uic.widget_screen_stream.show()
    def screen_start_stream(self):
        self.uic.label_screen
    def screen_stop_stream(self):
        pass
    

    #----- Code Area -----
    def address(self):
        self.hide_widgets()
        self.uic.widget_address.show()
        self.WidgetAddress.seeAddress()
    

    #----- Code Area -----
    def task_manager(self):
        self.hide_widgets()
        self.uic.widget_task_manager.show()

    

    #----- Code Area -----
    def file_explorer(self):
        self.hide_widgets()
        self.uic.widget_file_explorer.show()
        self.WidgetFileManagemnet.importData()

    

    #----- Code Area -----
    def control_input(self):
        self.hide_widgets()
        self.uic.widget_control_input.show()
    def lock_input(self):
        self.socket.control_input(True)
        self.uic.button_lock_input.hide()
        self.uic.button_unlock_input.show()
        self.uic.button_start_keylogger.setEnabled(False)
        self.uic.button_stop_keylogger.setEnabled(False)
        self.hide_widgets()
        self.uic.widget_control_input.show()
    def unlock_input(self):
        self.socket.control_input(True)
        self.uic.button_lock_input.hide()
        self.uic.button_unlock_input.show()
        self.uic.button_start_keylogger.setEnabled(False)
        self.uic.button_stop_keylogger.setEnabled(False)
    def start_keylogger(self):
        self.socket.start_keyhook()
        self.uic.button_start_keylogger.setText("Stop Keylogger")
    def stop_keylogger(self):
        self.socket.stop_keyhook()
        self.uic.button_start_keylogger.setText("Start Keylogger")
    def save_keylog(self):
        pass


    #----- Code Area -----
    def logout_n_shutdown(self):
        self.hide_widgets()
        self.uic.widget_logout_n_shutdown.show()
    def logout(self):
        self.socket.logout()
    def shutdown(self):
        self.socket.shutdown()

    





if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = ClientWindow(None)
    main_win.show()
    sys.exit(app.exec())

    