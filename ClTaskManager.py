from ClstartTask import AppView
from PyQt5 import QtCore, QtGui, QtWidgets

class ClTaskManager:
    def __init__(self, socket,ui):
        self.ui=ui
        self.socket=socket
        self.TMmodel = QtGui.QStandardItemModel()
        self.TMmodel.setHorizontalHeaderLabels(["Name", "PID", "Thread Count"])
        self.ui.treeViewProcess.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.treeViewProcess.customContextMenuRequested.connect(self.context_menu_task)
        self.ui.treeViewProcess.setModel(self.TMmodel)
        self.ui.treeViewProcess.setColumnWidth(0, 250)
        self.ui.treeViewProcess.expandAll()

        self.ui.buttonDelete.clicked.connect(self.BtDelete)
        self.ui.buttonStartApp.clicked.connect(self.BtStart)
        self.ui.buttonSee.clicked.connect(self.BtSee)
        self.ui.buttonApp.clicked.connect(self.BtApp)
        self.ui.buttonKill.clicked.connect(self.BtKill)
        

    def BtApp(self):
        self.BtDelete()
    def BtKill(self):
        if self.ui.treeViewProcess.selectedIndexes() !=None:
            pid=self.ui.treeViewProcess.selectedIndexes()[1].data()
            self.socket.kill_process(int(pid))
            self.BtSee()
    def BtStart(self):
        self.dialog=AppView(self.socket)
        self.dialog.show()

    def BtDelete(self):
        self.TMmodel.clear()
        self.TMmodel.setHorizontalHeaderLabels(["Name", "PID", "Thread Count"])
        self.ui.treeViewProcess.setColumnWidth(0, 250)

    def BtSee(self):        
        self.BtDelete()
        data=self.socket.request_list_process()
        root = self.TMmodel.invisibleRootItem()
        for value in data:
            if value['is_app']==self.ui.buttonApp.isChecked():
                a=QtGui.QStandardItem(value['Name'])
                a.setEditable(False)
                b=QtGui.QStandardItem(value['PID'])
                b.setEditable(False)
                c=QtGui.QStandardItem(value['Thread Count'])
                c.setEditable(False)
                root.appendRow([
                    QtGui.QStandardItem(a),
                    QtGui.QStandardItem(b),
                    QtGui.QStandardItem(c),
                    ])
    def context_menu_task(self):
        menu = QtWidgets.QMenu()
        menuDelete = menu.addAction("Delete")
        menuDelete.triggered.connect(self.BtKill)
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())