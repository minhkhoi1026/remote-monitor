
from PyQt5 import QtCore, QtGui, QtWidgets

class ClAddress:
    def __init__(self, socket,ui):
        self.ui=ui
        self.socket=socket
        self.TMmodel = QtGui.QStandardItemModel()
        self.TMmodel.setHorizontalHeaderLabels(["Name", "IP", "Subnet mask","MAC"])
        self.ui.treeViewAddress.setModel(self.TMmodel)
        self.ui.treeViewAddress.setColumnWidth(0, 250)
        self.ui.treeViewAddress.expandAll()

    def clearAddress(self):
        self.TMmodel.clear()
        self.TMmodel.setHorizontalHeaderLabels(["Name", "IP", "Subnet mask","MAC"])
        self.ui.treeViewAddress.setColumnWidth(0, 250)

    def seeAddress(self):        
        self.clearAddress()
        data=self.socket.request_mac()
        root = self.TMmodel.invisibleRootItem()
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
