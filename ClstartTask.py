from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QListView, QVBoxLayout, QLineEdit, QMessageBox, qApp
import os
import sys

class startApp(QWidget):

    def __init__(self,socket, parent=None):
        super(startApp, self).__init__(parent)
        self.resize(400, 400)
        self.socket=socket
        self.data=self.socket.request_list_app()
        self.ShowItemsList()

        

    def ShowItemsList(self):
        self.setWindowTitle("ListApp")

        self.listview = QListView(self)
        self.listview.doubleClicked.connect(self.confirm)
        self.searchEditText= QLineEdit(self)
        self.searchEditText.returnPressed.connect(self.searchItem)
        verticalLayout = QVBoxLayout(self)
        verticalLayout.addWidget(self.searchEditText)
        verticalLayout.addWidget(self.listview)
        self.model = QtGui.QStandardItemModel(self.listview)
        items=self.data
        for line in items:
            item = QtGui.QStandardItem(line['Name'])
            item.setEditable(False)
            self.model.appendRow(item)

        self.listview.setModel(self.model)
        self.listview.show()

    def searchItem(self):
        search_string = self.searchEditText.text() 
        items = self.model.findItems(search_string, QtCore.Qt.MatchStartsWith)
        if len(items) > 0:
            for item in items:
                if search_string:
                    self.model.takeRow(item.row()) 
                    self.model.insertRow(0, item)  
            ix = self.model.index(0,0)
            self.listview.clearSelection()
            self.listview.selectionModel().setCurrentIndex(ix,QtCore.QItemSelectionModel.SelectCurrent)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Notification")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("App name not found")
            x = msg.exec_()

    def confirm(self):
        name=self.listview.selectedIndexes()[0].data()
        id=next((sub for sub in self.data if sub['Name'] == name), None)['AppID']
        self.socket.start_app(id)
        self.close()

class startProcess(QWidget):

    def __init__(self,socket, parent=None):
        super(startProcess, self).__init__(parent)
        self.socket=socket
        self.Show()


        

    def Show(self):
        self.resize(326, 123)
        self.setWindowTitle("ListProcess")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 281, 22))
        self.lineEdit.returnPressed.connect(self.startPS)
        self.buttonOK = QtWidgets.QPushButton(self)
        self.buttonOK.setGeometry(QtCore.QRect(210, 80, 91, 28))
        self.buttonOK.setText('OK')
        self.buttonOK.clicked.connect(self.startPS)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 10, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setText('Name process')

    def startPS(self):
        self.socket.start_process(self.lineEdit.text())