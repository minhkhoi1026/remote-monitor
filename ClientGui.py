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
        MainWindow.resize(920, 552)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 171, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout_list_button = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_list_button.setContentsMargins(0, 0, 0, 0)
        self.layout_list_button.setObjectName("layout_list_button")
        self.button_connection = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_connection.setFont(font)
        self.button_connection.setObjectName("button_connection")
        self.layout_list_button.addWidget(self.button_connection)
        self.button_screen_stream = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_screen_stream.setFont(font)
        self.button_screen_stream.setObjectName("button_screen_stream")
        self.layout_list_button.addWidget(self.button_screen_stream)
        self.button_address = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_address.setFont(font)
        self.button_address.setObjectName("button_address")
        self.layout_list_button.addWidget(self.button_address)
        self.button_task_manager = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_task_manager.setFont(font)
        self.button_task_manager.setObjectName("button_task_manager")
        self.layout_list_button.addWidget(self.button_task_manager)
        self.button_file_explorer = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_file_explorer.setFont(font)
        self.button_file_explorer.setObjectName("button_file_explorer")
        self.layout_list_button.addWidget(self.button_file_explorer)
        self.button_control_input = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_control_input.setFont(font)
        self.button_control_input.setObjectName("button_control_input")
        self.layout_list_button.addWidget(self.button_control_input)
        self.button_logout_n_shutdown = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_logout_n_shutdown.setFont(font)
        self.button_logout_n_shutdown.setObjectName("button_logout_n_shutdown")
        self.layout_list_button.addWidget(self.button_logout_n_shutdown)
        self.widget_screen_stream = QtWidgets.QWidget(self.centralwidget)
        self.widget_screen_stream.setGeometry(QtCore.QRect(180, 60, 631, 481))
        self.widget_screen_stream.setAutoFillBackground(False)
        self.widget_screen_stream.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.widget_screen_stream.setObjectName("widget_screen_stream")
        self.label_7 = QtWidgets.QLabel(self.widget_screen_stream)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_screen = QtWidgets.QLabel(self.widget_screen_stream)
        self.label_screen.setGeometry(QtCore.QRect(20, 50, 691, 411))
        self.label_screen.setMouseTracking(True)
        self.label_screen.setStyleSheet("")
        self.label_screen.setText("")
        self.label_screen.setScaledContents(True)
        self.label_screen.setObjectName("label_screen")
        self.widget_address = QtWidgets.QWidget(self.centralwidget)
        self.widget_address.setGeometry(QtCore.QRect(200, 50, 631, 481))
        self.widget_address.setAutoFillBackground(False)
        self.widget_address.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.widget_address.setObjectName("widget_address")
        self.label_6 = QtWidgets.QLabel(self.widget_address)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_address_info = QtWidgets.QLabel(self.widget_address)
        self.label_address_info.setGeometry(QtCore.QRect(30, 70, 481, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_address_info.setFont(font)
        self.label_address_info.setStyleSheet("")
        self.label_address_info.setText("")
        self.label_address_info.setObjectName("label_address_info")
        self.treeViewAddress = QtWidgets.QTreeView(self.widget_address)
        self.treeViewAddress.setGeometry(QtCore.QRect(70, 90, 491, 331))
        self.treeViewAddress.setObjectName("treeViewAddress")
        self.widget_control_input = QtWidgets.QWidget(self.centralwidget)
        self.widget_control_input.setGeometry(QtCore.QRect(260, 20, 631, 481))
        self.widget_control_input.setAutoFillBackground(False)
        self.widget_control_input.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.widget_control_input.setObjectName("widget_control_input")
        self.label_3 = QtWidgets.QLabel(self.widget_control_input)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.button_lock_input = QtWidgets.QPushButton(self.widget_control_input)
        self.button_lock_input.setGeometry(QtCore.QRect(20, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_lock_input.setFont(font)
        self.button_lock_input.setObjectName("button_lock_input")
        self.button_start_keylogger = QtWidgets.QPushButton(self.widget_control_input)
        self.button_start_keylogger.setGeometry(QtCore.QRect(20, 110, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_start_keylogger.setFont(font)
        self.button_start_keylogger.setObjectName("button_start_keylogger")
        self.button_stop_keylogger = QtWidgets.QPushButton(self.widget_control_input)
        self.button_stop_keylogger.setGeometry(QtCore.QRect(20, 150, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_stop_keylogger.setFont(font)
        self.button_stop_keylogger.setObjectName("button_stop_keylogger")
        self.button_save_keylog = QtWidgets.QPushButton(self.widget_control_input)
        self.button_save_keylog.setGeometry(QtCore.QRect(20, 190, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_save_keylog.setFont(font)
        self.button_save_keylog.setObjectName("button_save_keylog")
        self.text_keylogger = QtWidgets.QTextEdit(self.widget_control_input)
        self.text_keylogger.setGeometry(QtCore.QRect(120, 110, 491, 361))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_keylogger.setFont(font)
        self.text_keylogger.setObjectName("text_keylogger")
        self.label_9 = QtWidgets.QLabel(self.widget_control_input)
        self.label_9.setGeometry(QtCore.QRect(130, 100, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.button_unlock_input = QtWidgets.QPushButton(self.widget_control_input)
        self.button_unlock_input.setGeometry(QtCore.QRect(20, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_unlock_input.setFont(font)
        self.button_unlock_input.setObjectName("button_unlock_input")
        self.button_unlock_input.raise_()
        self.button_lock_input.raise_()
        self.text_keylogger.raise_()
        self.label_3.raise_()
        self.button_start_keylogger.raise_()
        self.button_stop_keylogger.raise_()
        self.button_save_keylog.raise_()
        self.label_9.raise_()
        self.widget_logout_n_shutdown = QtWidgets.QWidget(self.centralwidget)
        self.widget_logout_n_shutdown.setGeometry(QtCore.QRect(280, 10, 631, 481))
        self.widget_logout_n_shutdown.setAutoFillBackground(False)
        self.widget_logout_n_shutdown.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.widget_logout_n_shutdown.setObjectName("widget_logout_n_shutdown")
        self.label_2 = QtWidgets.QLabel(self.widget_logout_n_shutdown)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_shutdown_icon = QtWidgets.QLabel(self.widget_logout_n_shutdown)
        self.label_shutdown_icon.setGeometry(QtCore.QRect(210, 160, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_shutdown_icon.setFont(font)
        self.label_shutdown_icon.setStyleSheet("image: url(:/image/image/icon_fail.png);")
        self.label_shutdown_icon.setText("")
        self.label_shutdown_icon.setObjectName("label_shutdown_icon")
        self.button_logout = QtWidgets.QPushButton(self.widget_logout_n_shutdown)
        self.button_logout.setGeometry(QtCore.QRect(250, 160, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_logout.setFont(font)
        self.button_logout.setObjectName("button_logout")
        self.label_shutdown_icon_2 = QtWidgets.QLabel(self.widget_logout_n_shutdown)
        self.label_shutdown_icon_2.setGeometry(QtCore.QRect(210, 250, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_shutdown_icon_2.setFont(font)
        self.label_shutdown_icon_2.setStyleSheet("image: url(:/image/image/icon_success.png);")
        self.label_shutdown_icon_2.setText("")
        self.label_shutdown_icon_2.setObjectName("label_shutdown_icon_2")
        self.button_shutdown = QtWidgets.QPushButton(self.widget_logout_n_shutdown)
        self.button_shutdown.setGeometry(QtCore.QRect(250, 250, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_shutdown.setFont(font)
        self.button_shutdown.setObjectName("button_shutdown")
        self.widget_connection = QtWidgets.QWidget(self.centralwidget)
        self.widget_connection.setGeometry(QtCore.QRect(160, 70, 631, 481))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.widget_connection.setFont(font)
        self.widget_connection.setAutoFillBackground(False)
        self.widget_connection.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.widget_connection.setObjectName("widget_connection")
        self.label = QtWidgets.QLabel(self.widget_connection)
        self.label.setGeometry(QtCore.QRect(10, 10, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.edit_IP = QtWidgets.QLineEdit(self.widget_connection)
        self.edit_IP.setEnabled(True)
        self.edit_IP.setGeometry(QtCore.QRect(230, 130, 171, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.edit_IP.setFont(font)
        self.edit_IP.setObjectName("edit_IP")
        self.button_connect = QtWidgets.QPushButton(self.widget_connection)
        self.button_connect.setGeometry(QtCore.QRect(230, 170, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_connect.setFont(font)
        self.button_connect.setObjectName("button_connect")
        self.label_8 = QtWidgets.QLabel(self.widget_connection)
        self.label_8.setGeometry(QtCore.QRect(150, 130, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_connect_icon = QtWidgets.QLabel(self.widget_connection)
        self.label_connect_icon.setGeometry(QtCore.QRect(230, 290, 31, 31))
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
        self.label_connect_note.setGeometry(QtCore.QRect(270, 290, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_connect_note.setFont(font)
        self.label_connect_note.setStyleSheet("")
        self.label_connect_note.setObjectName("label_connect_note")
        self.button_disconnect = QtWidgets.QPushButton(self.widget_connection)
        self.button_disconnect.setGeometry(QtCore.QRect(230, 170, 171, 31))
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
        self.edit_IP.raise_()
        self.label_8.raise_()
        self.label_connect_icon.raise_()
        self.label_connect_note.raise_()
        self.button_connect.raise_()
        self.widget_task_manager = QtWidgets.QWidget(self.centralwidget)
        self.widget_task_manager.setGeometry(QtCore.QRect(220, 40, 631, 481))
        self.widget_task_manager.setAutoFillBackground(False)
        self.widget_task_manager.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.widget_task_manager.setObjectName("widget_task_manager")
        self.label_10 = QtWidgets.QLabel(self.widget_task_manager)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.widget_task_manager)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(60, 90, 531, 381))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeViewProcess = QtWidgets.QTreeView(self.verticalLayoutWidget_2)
        self.treeViewProcess.setObjectName("treeViewProcess")
        self.verticalLayout.addWidget(self.treeViewProcess)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget_task_manager)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 40, 561, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonKill = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonKill.setObjectName("buttonKill")
        self.horizontalLayout.addWidget(self.buttonKill)
        self.buttonSee = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonSee.setObjectName("buttonSee")
        self.horizontalLayout.addWidget(self.buttonSee)
        self.buttonDelete = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonDelete.setObjectName("buttonDelete")
        self.horizontalLayout.addWidget(self.buttonDelete)
        self.buttonStart = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonStart.setObjectName("buttonStart")
        self.horizontalLayout.addWidget(self.buttonStart)
        self.buttonApp = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.buttonApp.setObjectName("buttonApp")
        self.horizontalLayout.addWidget(self.buttonApp)
        self.widget_file_explorer = QtWidgets.QWidget(self.centralwidget)
        self.widget_file_explorer.setGeometry(QtCore.QRect(240, 30, 631, 481))
        self.widget_file_explorer.setAutoFillBackground(False)
        self.widget_file_explorer.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.widget_file_explorer.setObjectName("widget_file_explorer")
        self.label_4 = QtWidgets.QLabel(self.widget_file_explorer)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.frame = QtWidgets.QFrame(self.widget_file_explorer)
        self.frame.setGeometry(QtCore.QRect(30, 80, 351, 351))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.FileServer = QtWidgets.QTreeView(self.frame)
        self.FileServer.setGeometry(QtCore.QRect(40, 10, 301, 341))
        self.FileServer.setObjectName("FileServer")
        self.frame_2 = QtWidgets.QFrame(self.widget_file_explorer)
        self.frame_2.setGeometry(QtCore.QRect(360, 20, 261, 421))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(20, 60, 241, 351))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.FileClient = QtWidgets.QTreeView(self.frame_3)
        self.FileClient.setGeometry(QtCore.QRect(10, 10, 201, 341))
        self.FileClient.setObjectName("FileClient")
        self.back = QtWidgets.QPushButton(self.frame_2)
        self.back.setGeometry(QtCore.QRect(30, 40, 61, 28))
        self.back.setObjectName("back")
        self.widget_connection.raise_()
        self.widget_screen_stream.raise_()
        self.verticalLayoutWidget.raise_()
        self.widget_file_explorer.raise_()
        self.widget_control_input.raise_()
        self.widget_logout_n_shutdown.raise_()
        self.widget_task_manager.raise_()
        self.widget_address.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_connection.setText(_translate("MainWindow", "Connection"))
        self.button_screen_stream.setText(_translate("MainWindow", "Screen Stream"))
        self.button_address.setText(_translate("MainWindow", "Address"))
        self.button_task_manager.setText(_translate("MainWindow", "Task Manager"))
        self.button_file_explorer.setText(_translate("MainWindow", "File Explorer"))
        self.button_control_input.setText(_translate("MainWindow", "Control Input"))
        self.button_logout_n_shutdown.setText(_translate("MainWindow", "Logout and Shutdown"))
        self.label_7.setText(_translate("MainWindow", "Screen Stream"))
        self.label_6.setText(_translate("MainWindow", "Address"))
        self.label_3.setText(_translate("MainWindow", "Control Input"))
        self.button_lock_input.setText(_translate("MainWindow", "Lock Input"))
        self.button_start_keylogger.setText(_translate("MainWindow", "Start"))
        self.button_stop_keylogger.setText(_translate("MainWindow", "Stop"))
        self.button_save_keylog.setText(_translate("MainWindow", "Save"))
        self.label_9.setText(_translate("MainWindow", "  Keylogger"))
        self.button_unlock_input.setText(_translate("MainWindow", "Unlock Input"))
        self.label_2.setText(_translate("MainWindow", "Logout and Shutdown"))
        self.button_logout.setText(_translate("MainWindow", "Logout"))
        self.button_shutdown.setText(_translate("MainWindow", "Shutdown"))
        self.label.setText(_translate("MainWindow", "Connection"))
        self.button_connect.setText(_translate("MainWindow", "Connect"))
        self.label_8.setText(_translate("MainWindow", "IP address:"))
        self.label_connect_note.setText(_translate("MainWindow", "Successful Connection"))
        self.button_disconnect.setText(_translate("MainWindow", "Disconnect"))
        self.label_10.setText(_translate("MainWindow", "Task Manager"))
        self.buttonKill.setText(_translate("MainWindow", "Kill"))
        self.buttonSee.setText(_translate("MainWindow", "See"))
        self.buttonDelete.setText(_translate("MainWindow", "Delete"))
        self.buttonStart.setText(_translate("MainWindow", "Start"))
        self.buttonApp.setText(_translate("MainWindow", "App"))
        self.label_4.setText(_translate("MainWindow", "File Explorer"))
        self.back.setText(_translate("MainWindow", "Back"))
import picture_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
