from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QListView, QVBoxLayout, QLineEdit, QMessageBox, qApp
import os
import sys

class AppView(QWidget):

    def __init__(self,socket, parent=None):
        super(AppView, self).__init__(parent)
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
            msg.setWindowTitle("Tutorial on PyQt5")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("This is the main text!")
            x = msg.exec_()

    def confirm(self):
        name=self.listview.selectedIndexes()[0].data()
        id=next((sub for sub in self.data if sub['Name'] == name), None)['AppID']
        self.socket.start_app(id)
        self.close()
