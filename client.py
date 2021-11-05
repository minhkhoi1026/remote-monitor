import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from ClientGui import Ui_MainWindow
from datetime import datetime

from client_socket import *
from streaming import StreamingClient
from file_management import *

from ClTaskManager import ClTaskManager
from ClFileManagement import ClFileManagement
from ClAddress import ClAddress

def addText(widget, new_text):
    widget.setText(widget.text() + new_text)

class ClientWindow:
    def __init__(self, socket):
        # --- create window ---
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.hide_widgets()
        self.connection()
        self.change_status_buttons(False)

        # --- create socket ---
        self.socket = SocketClient()
        self.stream_socket = StreamingClient(self.uic.label_screen)

        # --- setup function window ---
        self.connection_setup()
        self.screen_stream_setup()
        self.control_input_setup()
        self.logout_n_shutdown_setup()
        
        self.uic.button_address.clicked.connect(self.address)
        self.uic.button_task_manager.clicked.connect(self.task_manager)
        self.uic.button_file_explorer.clicked.connect(self.file_explorer)
        self.WidgetTaskManager=ClTaskManager(self.socket,self.uic)
        self.WidgetFileManagemnet=ClFileManagement(self.socket,self.uic)
        self.WidgetAddress=ClAddress(self.socket,self.uic)

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
    def change_status_buttons(self, is_enabled):
        self.uic.button_screen_stream.setEnabled(is_enabled)
        self.uic.button_address.setEnabled(is_enabled)
        self.uic.button_task_manager.setEnabled(is_enabled)
        self.uic.button_file_explorer.setEnabled(is_enabled)
        self.uic.button_control_input.setEnabled(is_enabled)
        self.uic.button_logout_n_shutdown.setEnabled(is_enabled)

    #----- Code Area -----
    def connection_setup(self):
        self.uic.button_connection.clicked.connect(self.connection)
        self.uic.button_connect.clicked.connect(self.connect)
        self.uic.button_disconnect.clicked.connect(self.disconnect)
        #self.uic.edit_IP.enterEvent.connect(self.connect)
        self.uic.label_connect_icon.hide()
        self.uic.label_connect_note.hide()
        self.uic.button_disconnect.hide()
    def connection(self):
        self.hide_widgets()
        self.uic.widget_connection.show()
    def connect(self):
        self.server_IP = self.uic.text_IP.text().strip()
        cn1 = self.socket.connect(self.server_IP,26100)

        self.uic.label_connect_icon.show()
        self.uic.label_connect_note.show()
        
        if cn1:
        #connect successfully
            self.stream_socket.start_stream(self.server_IP,9999)
            self.uic.text_IP.setEnabled(False)
            self.uic.button_connect.hide()
            self.uic.button_disconnect.show()
            self.uic.label_connect_icon.setStyleSheet("image: url(:/image/image/icon_success.png);")
            self.uic.label_connect_note.setText("Successful Connection")
            self.change_status_buttons(True)
        else:
        #connect failed
            self.uic.label_connect_icon.setStyleSheet("image: url(:/image/image/icon_fail.png);")
            self.uic.label_connect_note.setText("Connection Failed")
    def disconnect(self):
        self.socket.disconnect()
        self.stream_socket.stop_stream()
        self.stop_keylogger()

        self.uic.text_IP.setEnabled(True)
        self.uic.button_connect.show()
        self.uic.button_disconnect.hide()
        self.uic.label_connect_icon.hide()
        self.uic.label_connect_note.hide()
        self.change_status_buttons(False)


    #----- Code Area -----
    def screen_stream_setup(self):
        self.uic.button_screen_stream.clicked.connect(self.screen_stream)
        self.uic.button_screenshot.clicked.connect(self.screenshot)
        self.uic.button_browser_screen.clicked.connect(self.browser_screen)
        self.uic.text_location_screen.setText(get_document_path())
    def screen_stream(self):
        self.hide_widgets()
        self.uic.widget_screen_stream.show()
    def screenshot(self):
        location = self.uic.text_location_screen.text().strip()
        filename = self.uic.text_filename_screen.text().strip()
        if location == "":
            self.uic.text_location_screen.setText(get_document_path())
            return self.screenshot()
        if filename == "":
            filename = self.server_IP
        filename += datetime.now().strftime("_d%d.%m.%Y_t%H.%M.%S") + ".png"

        filepath = os.path.join(location, filename)
        self.stream_socket.save_screenshot(filepath)
    def browser_screen(self):
        path = QFileDialog.getSaveFileName()[0]
        if path != "":
            items = path.split("/")
            print(items)
            filename = items[-1]
            location = "/".join(items[:len(items)-1])
            self.uic.text_location_screen.setText(location)
            self.uic.text_filename_screen.setText(filename)
    

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
    def control_input_setup(self):
        self.uic.button_control_input.clicked.connect(self.control_input)
        self.uic.button_lock_input.clicked.connect(self.lock_input)
        self.uic.button_unlock_input.clicked.connect(self.unlock_input)
        self.uic.button_start_keylogger.clicked.connect(self.start_keylogger)
        self.uic.button_stop_keylogger.clicked.connect(self.stop_keylogger)
        self.uic.button_save_keylog.clicked.connect(self.save_keylog)
        self.uic.button_delete_keylog.clicked.connect(self.delete_keylog)
        self.uic.button_browser_keylog.clicked.connect(self.browser_keylog)
        self.uic.button_unlock_input.hide()
        self.uic.button_stop_keylogger.setEnabled(False)
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
        self.uic.button_lock_input.show()
        self.uic.button_unlock_input.hide()
        self.uic.button_start_keylogger.setEnabled(False)
        self.uic.button_stop_keylogger.setEnabled(False)
    def start_keylogger(self):
        self.socket.start_keyhook(self.uic.keylog)
        self.uic.button_start_keylogger.setEnabled(False)
        self.uic.button_stop_keylogger.setEnabled(True)
    def stop_keylogger(self):
        self.socket.stop_keyhook()
        self.socket.stop_keyhook()
        self.uic.button_start_keylogger.setEnabled(True)
        self.uic.button_stop_keylogger.setEnabled(False)
    def delete_keylog(self):
        self.uic.keylog.setText("")
    def save_keylog(self):
        location = self.uic.text_location_keylog.text().strip()
        filename = self.uic.text_filename_keylog.text().strip()
        if location == "" or filename == "":
            return self.browser_keylog()
        filepath = os.path.join(location, filename)
        text = self.uic.keylog.text()
        fwrite = open(filepath,"w")
        fwrite.write(text)
    def browser_keylog(self):
        path = QFileDialog.getSaveFileName()[0]
        if path != "":
            items = path.split("/")
            filename = items[-1]
            if '.' not in filename:
                filename += ".txt"
            location = "/".join(items[:len(items)-1])
            self.uic.text_location_keylog.setText(location)
            self.uic.text_filename_keylog.setText(filename)


    #----- Code Area -----
    def logout_n_shutdown_setup(self):
        self.uic.button_logout_n_shutdown.clicked.connect(self.logout_n_shutdown)
        self.uic.button_logout.clicked.connect(self.logout)
        self.uic.button_shutdown.clicked.connect(self.shutdown)
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