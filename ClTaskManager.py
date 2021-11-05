from ClstartTask import startApp,startProcess
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
        self.ui.treeViewProcess.setStyleSheet("background-color: white")
        self.ui.treeViewProcess.expandAll()

        self.ui.buttonDelete.clicked.connect(self.BtDelete)
        self.ui.buttonStartApp.clicked.connect(self.BtStartApp)
        self.ui.buttonStartProcess.clicked.connect(self.BtStartProcess)
        self.ui.buttonSee.clicked.connect(self.BtSee)
        self.ui.buttonApp.clicked.connect(self.BtApp)

    def BtApp(self):
        self.BtDelete()
        self.BtSee()
    def BtKill(self):
        if self.ui.treeViewProcess.selectedIndexes() !=None:
            pid=self.ui.treeViewProcess.selectedIndexes()[1].data()
            self.socket.kill_process(int(pid))
            self.BtSee()
    def BtStartApp(self):
        self.dialog1=startApp(self.socket)
        self.dialog1.show()

    def BtStartProcess(self):
        self.dialog2=startProcess(self.socket)
        self.dialog2.show()

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
        for i in range(0, len(data),2):
            self.TMmodel.setData(self.TMmodel.index(i, 0), QtGui.QBrush(QtGui.QColor(221, 221, 221)), QtCore.Qt.BackgroundRole)
            self.TMmodel.setData(self.TMmodel.index(i, 1), QtGui.QBrush(QtGui.QColor(221, 221, 221)), QtCore.Qt.BackgroundRole)
            self.TMmodel.setData(self.TMmodel.index(i, 2), QtGui.QBrush(QtGui.QColor(221, 221, 221)), QtCore.Qt.BackgroundRole)
            self.TMmodel.setData(self.TMmodel.index(i, 3), QtGui.QBrush(QtGui.QColor(221, 221, 221)), QtCore.Qt.BackgroundRole)
    def context_menu_task(self):
        menu = QtWidgets.QMenu()
        menuDelete = menu.addAction("Kill")
        menuDelete.triggered.connect(self.BtKill)
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())
