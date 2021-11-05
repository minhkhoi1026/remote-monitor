
from PyQt5 import QtCore, QtGui, QtWidgets

class ClAddress:
    def __init__(self, socket,ui):
        self.ui=ui
        self.socket=socket
        self.addressModel = QtGui.QStandardItemModel()
        self.addressModel.setHorizontalHeaderLabels(["Name", "IP", "Subnet mask","MAC"])
        self.ui.treeViewAddress.setModel(self.addressModel)
        self.ui.treeViewAddress.setColumnWidth(0, 250)
        self.ui.treeViewAddress.setStyleSheet("background-color: white")
        self.ui.treeViewAddress.expandAll()

    def clearAddress(self):
        self.addressModel.clear()
        self.addressModel.setHorizontalHeaderLabels(["Name", "IP", "Subnet mask","MAC"])
        self.ui.treeViewAddress.setColumnWidth(0, 250)

    def seeAddress(self):        
        self.clearAddress()
        data=self.socket.request_mac()
        root = self.addressModel.invisibleRootItem()
        for value in data:
            a=QtGui.QStandardItem(value['Name'])
            a.setEditable(False)
            b=QtGui.QStandardItem(value['IP'])
            b.setEditable(False)
            c=QtGui.QStandardItem(value['Subnet mask'])
            c.setEditable(False)
            d=QtGui.QStandardItem(value['MAC'])
            d.setEditable(False)
            root.appendRow([
                QtGui.QStandardItem(a),
                QtGui.QStandardItem(b),
                QtGui.QStandardItem(c),
                QtGui.QStandardItem(d)
                ])
        for i in range(0, len(data),2):
            self.addressModel.setData(self.addressModel.index(i, 0), QtGui.QBrush(QtGui.QColor(221, 221, 221)), QtCore.Qt.BackgroundRole)
            self.addressModel.setData(self.addressModel.index(i, 1), QtGui.QBrush(QtGui.QColor(221, 221, 221)), QtCore.Qt.BackgroundRole)
            self.addressModel.setData(self.addressModel.index(i, 2), QtGui.QBrush(QtGui.QColor(221, 221, 221)), QtCore.Qt.BackgroundRole)
            self.addressModel.setData(self.addressModel.index(i, 3), QtGui.QBrush(QtGui.QColor(221, 221, 221)), QtCore.Qt.BackgroundRole)
