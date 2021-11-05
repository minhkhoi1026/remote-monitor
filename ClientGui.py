# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Client.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1270, 620)
        MainWindow.setMinimumSize(QtCore.QSize(1270, 620))
        MainWindow.setMaximumSize(QtCore.QSize(1270, 620))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_screen_stream = QtWidgets.QWidget(self.centralwidget)
        self.widget_screen_stream.setGeometry(QtCore.QRect(160, 10, 1101, 601))
        self.widget_screen_stream.setAutoFillBackground(False)
        self.widget_screen_stream.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.widget_screen_stream.setObjectName("widget_screen_stream")
        self.label_7 = QtWidgets.QLabel(self.widget_screen_stream)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_screen = QtWidgets.QLabel(self.widget_screen_stream)
        self.label_screen.setGeometry(QtCore.QRect(180, 30, 881, 491))
        self.label_screen.setMouseTracking(True)
        self.label_screen.setStyleSheet("")
        self.label_screen.setText("")
        self.label_screen.setScaledContents(True)
        self.label_screen.setObjectName("label_screen")
        self.text_location_screen = QtWidgets.QLineEdit(self.widget_screen_stream)
        self.text_location_screen.setEnabled(True)
        self.text_location_screen.setGeometry(QtCore.QRect(110, 540, 631, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.text_location_screen.setFont(font)
        self.text_location_screen.setObjectName("text_location_screen")
        self.button_screenshot = QtWidgets.QPushButton(self.widget_screen_stream)
        self.button_screenshot.setGeometry(QtCore.QRect(50, 450, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_screenshot.setFont(font)
        self.button_screenshot.setObjectName("button_screenshot")
        self.label_14 = QtWidgets.QLabel(self.widget_screen_stream)
        self.label_14.setGeometry(QtCore.QRect(50, 540, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.button_browser_screen = QtWidgets.QPushButton(self.widget_screen_stream)
        self.button_browser_screen.setGeometry(QtCore.QRect(50, 490, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_browser_screen.setFont(font)
        self.button_browser_screen.setObjectName("button_browser_screen")
        self.text_filename_screen = QtWidgets.QLineEdit(self.widget_screen_stream)
        self.text_filename_screen.setEnabled(True)
        self.text_filename_screen.setGeometry(QtCore.QRect(840, 540, 141, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.text_filename_screen.setFont(font)
        self.text_filename_screen.setObjectName("text_filename_screen")
        self.label_15 = QtWidgets.QLabel(self.widget_screen_stream)
        self.label_15.setGeometry(QtCore.QRect(770, 540, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.widget_screen_stream)
        self.label_16.setGeometry(QtCore.QRect(980, 540, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.widget_address = QtWidgets.QWidget(self.centralwidget)
        self.widget_address.setGeometry(QtCore.QRect(160, 10, 1101, 601))
        self.widget_address.setAutoFillBackground(False)
        self.widget_address.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.widget_address.setObjectName("widget_address")
        self.label_6 = QtWidgets.QLabel(self.widget_address)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.treeViewAddress = QtWidgets.QTreeView(self.widget_address)
        self.treeViewAddress.setGeometry(QtCore.QRect(90, 70, 921, 461))
        self.treeViewAddress.setObjectName("treeViewAddress")
        self.widget_control_input = QtWidgets.QWidget(self.centralwidget)
        self.widget_control_input.setGeometry(QtCore.QRect(160, 10, 1101, 601))
        self.widget_control_input.setAutoFillBackground(False)
        self.widget_control_input.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.widget_control_input.setObjectName("widget_control_input")
        self.label_3 = QtWidgets.QLabel(self.widget_control_input)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.button_lock_input = QtWidgets.QPushButton(self.widget_control_input)
        self.button_lock_input.setGeometry(QtCore.QRect(50, 60, 101, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_lock_input.setFont(font)
        self.button_lock_input.setObjectName("button_lock_input")
        self.button_start_keylogger = QtWidgets.QPushButton(self.widget_control_input)
        self.button_start_keylogger.setGeometry(QtCore.QRect(50, 140, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_start_keylogger.setFont(font)
        self.button_start_keylogger.setObjectName("button_start_keylogger")
        self.button_stop_keylogger = QtWidgets.QPushButton(self.widget_control_input)
        self.button_stop_keylogger.setGeometry(QtCore.QRect(50, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_stop_keylogger.setFont(font)
        self.button_stop_keylogger.setObjectName("button_stop_keylogger")
        self.button_save_keylog = QtWidgets.QPushButton(self.widget_control_input)
        self.button_save_keylog.setGeometry(QtCore.QRect(50, 440, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_save_keylog.setFont(font)
        self.button_save_keylog.setObjectName("button_save_keylog")
        self.label_9 = QtWidgets.QLabel(self.widget_control_input)
        self.label_9.setGeometry(QtCore.QRect(180, 50, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.button_unlock_input = QtWidgets.QPushButton(self.widget_control_input)
        self.button_unlock_input.setGeometry(QtCore.QRect(50, 60, 101, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_unlock_input.setFont(font)
        self.button_unlock_input.setObjectName("button_unlock_input")
        self.text_location_keylog = QtWidgets.QLineEdit(self.widget_control_input)
        self.text_location_keylog.setEnabled(True)
        self.text_location_keylog.setGeometry(QtCore.QRect(110, 530, 671, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.text_location_keylog.setFont(font)
        self.text_location_keylog.setObjectName("text_location_keylog")
        self.button_browser_keylog = QtWidgets.QPushButton(self.widget_control_input)
        self.button_browser_keylog.setGeometry(QtCore.QRect(50, 480, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_browser_keylog.setFont(font)
        self.button_browser_keylog.setObjectName("button_browser_keylog")
        self.label_11 = QtWidgets.QLabel(self.widget_control_input)
        self.label_11.setGeometry(QtCore.QRect(50, 530, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.text_filename_keylog = QtWidgets.QLineEdit(self.widget_control_input)
        self.text_filename_keylog.setEnabled(True)
        self.text_filename_keylog.setGeometry(QtCore.QRect(880, 530, 161, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.text_filename_keylog.setFont(font)
        self.text_filename_keylog.setObjectName("text_filename_keylog")
        self.label_12 = QtWidgets.QLabel(self.widget_control_input)
        self.label_12.setGeometry(QtCore.QRect(810, 530, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.button_delete_keylog = QtWidgets.QPushButton(self.widget_control_input)
        self.button_delete_keylog.setGeometry(QtCore.QRect(50, 400, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_delete_keylog.setFont(font)
        self.button_delete_keylog.setObjectName("button_delete_keylog")
        self.keylog = QtWidgets.QLabel(self.widget_control_input)
        self.keylog.setGeometry(QtCore.QRect(170, 60, 871, 451))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.keylog.setFont(font)
        self.keylog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.keylog.setFrameShape(QtWidgets.QFrame.Box)
        self.keylog.setText("")
        self.keylog.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.keylog.setObjectName("keylog")
        self.keylog.raise_()
        self.label_12.raise_()
        self.label_11.raise_()
        self.button_unlock_input.raise_()
        self.button_lock_input.raise_()
        self.label_3.raise_()
        self.button_start_keylogger.raise_()
        self.button_stop_keylogger.raise_()
        self.button_save_keylog.raise_()
        self.label_9.raise_()
        self.text_location_keylog.raise_()
        self.button_browser_keylog.raise_()
        self.text_filename_keylog.raise_()
        self.button_delete_keylog.raise_()
        self.widget_logout_n_shutdown = QtWidgets.QWidget(self.centralwidget)
        self.widget_logout_n_shutdown.setGeometry(QtCore.QRect(160, 10, 1101, 601))
        self.widget_logout_n_shutdown.setAutoFillBackground(False)
        self.widget_logout_n_shutdown.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.widget_logout_n_shutdown.setObjectName("widget_logout_n_shutdown")
        self.label_2 = QtWidgets.QLabel(self.widget_logout_n_shutdown)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.button_logout = QtWidgets.QPushButton(self.widget_logout_n_shutdown)
        self.button_logout.setGeometry(QtCore.QRect(470, 200, 151, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_logout.setFont(font)
        self.button_logout.setObjectName("button_logout")
        self.button_shutdown = QtWidgets.QPushButton(self.widget_logout_n_shutdown)
        self.button_shutdown.setGeometry(QtCore.QRect(470, 320, 151, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_shutdown.setFont(font)
        self.button_shutdown.setObjectName("button_shutdown")
        self.widget_connection = QtWidgets.QWidget(self.centralwidget)
        self.widget_connection.setGeometry(QtCore.QRect(160, 10, 1101, 601))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.widget_connection.setFont(font)
        self.widget_connection.setAutoFillBackground(False)
        self.widget_connection.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.widget_connection.setObjectName("widget_connection")
        self.label = QtWidgets.QLabel(self.widget_connection)
        self.label.setGeometry(QtCore.QRect(20, 10, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.text_IP = QtWidgets.QLineEdit(self.widget_connection)
        self.text_IP.setEnabled(True)
        self.text_IP.setGeometry(QtCore.QRect(420, 240, 171, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.text_IP.setFont(font)
        self.text_IP.setAlignment(QtCore.Qt.AlignCenter)
        self.text_IP.setObjectName("text_IP")
        self.button_connect = QtWidgets.QPushButton(self.widget_connection)
        self.button_connect.setGeometry(QtCore.QRect(420, 280, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_connect.setFont(font)
        self.button_connect.setObjectName("button_connect")
        self.label_8 = QtWidgets.QLabel(self.widget_connection)
        self.label_8.setGeometry(QtCore.QRect(340, 240, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_connect_icon = QtWidgets.QLabel(self.widget_connection)
        self.label_connect_icon.setGeometry(QtCore.QRect(420, 400, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_connect_icon.setFont(font)
        self.label_connect_icon.setStyleSheet("image: url(:/image/image/icon_success.png);")
        self.label_connect_icon.setText("")
        self.label_connect_icon.setObjectName("label_connect_icon")
        self.label_connect_note = QtWidgets.QLabel(self.widget_connection)
        self.label_connect_note.setGeometry(QtCore.QRect(460, 400, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_connect_note.setFont(font)
        self.label_connect_note.setStyleSheet("")
        self.label_connect_note.setObjectName("label_connect_note")
        self.button_disconnect = QtWidgets.QPushButton(self.widget_connection)
        self.button_disconnect.setGeometry(QtCore.QRect(420, 280, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_disconnect.setFont(font)
        self.button_disconnect.setStatusTip("")
        self.button_disconnect.setShortcut("")
        self.button_disconnect.setAutoDefault(False)
        self.button_disconnect.setDefault(False)
        self.button_disconnect.setFlat(False)
        self.button_disconnect.setObjectName("button_disconnect")
        self.button_disconnect.raise_()
        self.label.raise_()
        self.text_IP.raise_()
        self.label_8.raise_()
        self.label_connect_icon.raise_()
        self.label_connect_note.raise_()
        self.button_connect.raise_()
        self.widget_task_manager = QtWidgets.QWidget(self.centralwidget)
        self.widget_task_manager.setGeometry(QtCore.QRect(160, 10, 1101, 601))
        self.widget_task_manager.setAutoFillBackground(False)
        self.widget_task_manager.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.widget_task_manager.setObjectName("widget_task_manager")
        self.label_10 = QtWidgets.QLabel(self.widget_task_manager)
        self.label_10.setGeometry(QtCore.QRect(20, 10, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.widget_task_manager)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(120, 100, 851, 451))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeViewProcess = QtWidgets.QTreeView(self.verticalLayoutWidget_2)
        self.treeViewProcess.setObjectName("treeViewProcess")
        self.verticalLayout.addWidget(self.treeViewProcess)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget_task_manager)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(120, 40, 851, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonSee = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonSee.setObjectName("buttonSee")
        self.horizontalLayout.addWidget(self.buttonSee)
        self.buttonDelete = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonDelete.setObjectName("buttonDelete")
        self.horizontalLayout.addWidget(self.buttonDelete)
        self.buttonStartProcess = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonStartProcess.setObjectName("buttonStartProcess")
        self.horizontalLayout.addWidget(self.buttonStartProcess)
        self.buttonStartApp = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonStartApp.setObjectName("buttonStartApp")
        self.horizontalLayout.addWidget(self.buttonStartApp)
        self.buttonApp = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.buttonApp.setObjectName("buttonApp")
        self.horizontalLayout.addWidget(self.buttonApp)
        self.widget_file_explorer = QtWidgets.QWidget(self.centralwidget)
        self.widget_file_explorer.setGeometry(QtCore.QRect(160, 10, 1101, 601))
        self.widget_file_explorer.setAutoFillBackground(False)
        self.widget_file_explorer.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.widget_file_explorer.setObjectName("widget_file_explorer")
        self.label_4 = QtWidgets.QLabel(self.widget_file_explorer)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.frame = QtWidgets.QFrame(self.widget_file_explorer)
        self.frame.setGeometry(QtCore.QRect(10, 40, 531, 551))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.FileServer = QtWidgets.QTreeView(self.frame)
        self.FileServer.setGeometry(QtCore.QRect(20, 70, 501, 461))
        self.FileServer.setObjectName("FileServer")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(240, 20, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.frame_2 = QtWidgets.QFrame(self.widget_file_explorer)
        self.frame_2.setGeometry(QtCore.QRect(550, 40, 541, 551))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(10, 60, 521, 481))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.FileClient = QtWidgets.QTreeView(self.frame_3)
        self.FileClient.setGeometry(QtCore.QRect(10, 10, 501, 461))
        self.FileClient.setObjectName("FileClient")
        self.back = QtWidgets.QPushButton(self.frame_2)
        self.back.setGeometry(QtCore.QRect(20, 20, 71, 28))
        self.back.setObjectName("back")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(240, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.button_connection = QtWidgets.QPushButton(self.centralwidget)
        self.button_connection.setGeometry(QtCore.QRect(10, 10, 139, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_connection.setFont(font)
        self.button_connection.setObjectName("button_connection")
        self.button_screen_stream = QtWidgets.QPushButton(self.centralwidget)
        self.button_screen_stream.setGeometry(QtCore.QRect(10, 90, 139, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_screen_stream.setFont(font)
        self.button_screen_stream.setObjectName("button_screen_stream")
        self.button_address = QtWidgets.QPushButton(self.centralwidget)
        self.button_address.setGeometry(QtCore.QRect(10, 140, 139, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_address.setFont(font)
        self.button_address.setObjectName("button_address")
        self.button_task_manager = QtWidgets.QPushButton(self.centralwidget)
        self.button_task_manager.setGeometry(QtCore.QRect(10, 190, 139, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_task_manager.setFont(font)
        self.button_task_manager.setObjectName("button_task_manager")
        self.button_file_explorer = QtWidgets.QPushButton(self.centralwidget)
        self.button_file_explorer.setGeometry(QtCore.QRect(10, 240, 139, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_file_explorer.setFont(font)
        self.button_file_explorer.setObjectName("button_file_explorer")
        self.button_control_input = QtWidgets.QPushButton(self.centralwidget)
        self.button_control_input.setGeometry(QtCore.QRect(10, 290, 139, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_control_input.setFont(font)
        self.button_control_input.setObjectName("button_control_input")
        self.button_logout_n_shutdown = QtWidgets.QPushButton(self.centralwidget)
        self.button_logout_n_shutdown.setGeometry(QtCore.QRect(10, 340, 139, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_logout_n_shutdown.setFont(font)
        self.button_logout_n_shutdown.setObjectName("button_logout_n_shutdown")
        self.widget_connection.raise_()
        self.widget_screen_stream.raise_()
        self.widget_address.raise_()
        self.widget_task_manager.raise_()
        self.widget_file_explorer.raise_()
        self.widget_control_input.raise_()
        self.widget_logout_n_shutdown.raise_()
        self.button_connection.raise_()
        self.button_screen_stream.raise_()
        self.button_address.raise_()
        self.button_task_manager.raise_()
        self.button_file_explorer.raise_()
        self.button_control_input.raise_()
        self.button_logout_n_shutdown.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "Screen Stream"))
        self.button_screenshot.setText(_translate("MainWindow", "Screenshot"))
        self.label_14.setText(_translate("MainWindow", "Location"))
        self.button_browser_screen.setText(_translate("MainWindow", "Browser"))
        self.label_15.setText(_translate("MainWindow", "Filename"))
        self.label_16.setText(_translate("MainWindow", ".<time>.png"))
        self.label_6.setText(_translate("MainWindow", "Address"))
        self.label_3.setText(_translate("MainWindow", "Control Input"))
        self.button_lock_input.setText(_translate("MainWindow", "Lock Input"))
        self.button_start_keylogger.setText(_translate("MainWindow", "Start"))
        self.button_stop_keylogger.setText(_translate("MainWindow", "Stop"))
        self.button_save_keylog.setText(_translate("MainWindow", "Save"))
        self.label_9.setText(_translate("MainWindow", "Keylog"))
        self.button_unlock_input.setText(_translate("MainWindow", "Unlock Input"))
        self.button_browser_keylog.setText(_translate("MainWindow", "Browser"))
        self.label_11.setText(_translate("MainWindow", "Location"))
        self.label_12.setText(_translate("MainWindow", "Filename"))
        self.button_delete_keylog.setText(_translate("MainWindow", "Delete"))
        self.label_2.setText(_translate("MainWindow", "Logout and Shutdown"))
        self.button_logout.setText(_translate("MainWindow", "Logout"))
        self.button_shutdown.setText(_translate("MainWindow", "Shutdown"))
        self.label.setText(_translate("MainWindow", "Connection"))
        self.button_connect.setText(_translate("MainWindow", "Connect"))
        self.label_8.setText(_translate("MainWindow", "IP address:"))
        self.label_connect_note.setText(_translate("MainWindow", "Successful Connection"))
        self.button_disconnect.setText(_translate("MainWindow", "Disconnect"))
        self.label_10.setText(_translate("MainWindow", "Task Manager"))
        self.buttonSee.setText(_translate("MainWindow", "Refresh"))
        self.buttonDelete.setText(_translate("MainWindow", "Clear"))
        self.buttonStartProcess.setText(_translate("MainWindow", "Start process"))
        self.buttonStartApp.setText(_translate("MainWindow", "Start App"))
        self.buttonApp.setText(_translate("MainWindow", "App"))
        self.label_4.setText(_translate("MainWindow", "File Explorer"))
        self.label_5.setText(_translate("MainWindow", "Server"))
        self.back.setText(_translate("MainWindow", "Back"))
        self.label_13.setText(_translate("MainWindow", "Client"))
        self.button_connection.setText(_translate("MainWindow", "Connection"))
        self.button_screen_stream.setText(_translate("MainWindow", "Screen Stream"))
        self.button_address.setText(_translate("MainWindow", "Address"))
        self.button_task_manager.setText(_translate("MainWindow", "Task Manager"))
        self.button_file_explorer.setText(_translate("MainWindow", "File Explorer"))
        self.button_control_input.setText(_translate("MainWindow", "Control Input"))
        self.button_logout_n_shutdown.setText(_translate("MainWindow", "Logout and Shutdown"))
import picture_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
