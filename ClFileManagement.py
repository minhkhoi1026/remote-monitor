
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pickle
from PIL.ImageQt import ImageQt
class ClFileManagement:
    def __init__(self, socket,ui):
        self.ui=ui
        self.socket=socket
        self.select=None
        self.pathClient=None
        self.ClCopied=None
        self.FClientModel = QtWidgets.QFileSystemModel()
        self.FClientModel.setRootPath((QtCore.QDir.rootPath()))
        self.ui.FileClient.setModel(self.FClientModel)
        self.ui.FileClient.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.FileClient.customContextMenuRequested.connect(self.context_menu_client)
        self.ui.back.clicked.connect(self.FBackClient)
        self.ui.FileClient.doubleClicked.connect(self.open_folderClient)
        self.ui.FileClient.setColumnWidth(1, 70)
        self.ui.FileClient.setColumnWidth(0, 150)
        self.ui.FileClient.setStyleSheet("background-color: white")
        self.populate()

        self.pathServer=None
        self.SvCopied=None
        self.FServerModel = QtGui.QStandardItemModel()
        self.FServerModel.setHorizontalHeaderLabels(["Filename","Filesize" , "Filetype","Last modified"])
        self.ui.FileServer.setModel(self.FServerModel)
        self.ui.FileServer.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.FileServer.customContextMenuRequested.connect(self.context_menu_server)
        self.ui.FileServer.doubleClicked.connect(self.open_folderServer)
        self.ui.FileServer.setStyleSheet("background-color: white")
        #----- Client File -----
    def FBackClient(self):
        if self.pathClient!=None:
            self.pathClient=self.get_parent_dir(self.pathClient)
            self.populate()
    def populate(self):
        path=self.pathClient
        self.ui.FileClient.setRootIndex(self.FClientModel.index(path))
        self.pathClient=path
        self.ui.FileClient.setSortingEnabled(True)

    def context_menu_client(self):
        menu = QtWidgets.QMenu()
        menuCopy = menu.addAction("Copy")
        menuPaste = menu.addAction("Paste")
        menuCopy.triggered.connect(self.Action_ClCopy)
        menuPaste.triggered.connect(self.Action_ClPaste)
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())
    def open_folderClient(self):
        if self.ui.FileClient.selectedIndexes()[2].data()=='File Folder':
            index = self.ui.FileClient.currentIndex()
            self.pathClient = self.FClientModel.filePath(index)
            self.populate()
    	#----- Server File-----
    def context_menu_server(self):
        menu = QtWidgets.QMenu()
        menuDelete = menu.addAction("Delete")
        menuCopy = menu.addAction("Copy")
        menuPaste = menu.addAction("Paste")
        menuDelete.triggered.connect(self.Action_SvDelete)
        menuCopy.triggered.connect(self.Action_SvCopy)
        menuPaste.triggered.connect(self.Action_SvPaste)
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos()) 
    def Action_SvDelete(self):
        row=self.ui.FileServer.selectedIndexes()
        if row[0].data()!='[...]' and row[2].data()!='<DIR>':
            file_path=self.pathServer
            if self.pathServer[-1]!='\\':
                file_path+='\\'
            file_path+=row[0].data()
            self.socket.del_file(file_path)
            self.importData()
    def Action_SvCopy(self):
        row=self.ui.FileServer.selectedIndexes()
        if row[0].data()!='[...]' and row[2].data()!='<DIR>':
            file_path=self.pathServer
            if self.pathServer[-1]!='\\':
                file_path+='\\'
            file_path+=row[0].data()
            self.SvCopied=[file_path,row[0].data()]
    def Action_SvPaste(self):
        dicts=self.socket.request_listdir(self.pathServer)['content']
        exist = next((item for item in dicts if item["Filename"] == self.ClCopied[1]), None) != None
        if exist:
            self.show_popup()
            if self.select=='&No':
                return
        name = self.pathServer
        if self.pathServer[-1]!='\\':
            name += '\\'
        self.socket.send_file(self.ClCopied[0],name+self.ClCopied[1])
        self.importData()
    def Action_ClCopy(self):
        if self.ui.FileClient.selectedIndexes()[2].data()!='File Folder':
            index = self.ui.FileClient.currentIndex()
            file_path = self.FClientModel.filePath(index)
            self.ClCopied=[file_path.replace('/','\\'),index.data()]
    def Action_ClPaste(self):
        if not self.pathClient:
            return 
        exist= os.path.exists(self.pathClient.replace('/','\\')+'\\'+self.SvCopied[1])
        if exist:
            self.show_popup()
            if self.select=='&No':
                return
        self.socket.get_file(self.pathClient.replace('/','\\')+'\\'+self.SvCopied[1],self.SvCopied[0])
    def Clear(self):
        self.FServerModel.clear()
        self.FServerModel.setHorizontalHeaderLabels(["Filename","Filesize" , "Filetype","Last modified"])
        self.ui.FileServer.setColumnWidth(1, 50)
        self.ui.FileServer.setColumnWidth(0, 150)
    def importData(self):
        self.Clear()
        data=self.socket.request_listdir(self.pathServer)
        root = self.FServerModel.invisibleRootItem()
        if self.pathServer != None:
            root.appendRow([QtGui.QStandardItem('[...]')])
        for value in data['content']:
            image_icon = ImageQt(pickle.loads(value['Icon']))
            pixmap_icon = QtGui.QPixmap.fromImage(image_icon)
            a=QtGui.QStandardItem(QtGui.QIcon(pixmap_icon),value['Filename'])
            a.setEditable(False)
            b=QtGui.QStandardItem(value['Filesize'])
            b.setEditable(False)
            c=QtGui.QStandardItem(value['Filetype'])
            c.setEditable(False)
            d=QtGui.QStandardItem(value['Last modified'])
            d.setEditable(False)
            root.appendRow([
                QtGui.QStandardItem(a),
                QtGui.QStandardItem(b),
                QtGui.QStandardItem(c),
                QtGui.QStandardItem(d),
                ])
    def open_folderServer(self):
        if (self.ui.FileServer.selectedIndexes()[0].data()=='[...]'):
            self.pathServer=self.get_parent_dir(self.pathServer)
        elif self.ui.FileServer.selectedIndexes()[2].data()!='<DIR>':
            return    
        else:
            if self.pathServer==None:
                self.pathServer=self.ui.FileServer.selectedIndexes()[0].data().replace('/','\\')
            else:
                if self.pathServer[-1]!='\\':
                    self.pathServer+='\\'
                self.pathServer+=self.ui.FileServer.selectedIndexes()[0].data()
        self.Clear()
        self.importData()
    def get_parent_dir(self,path):
        if path is None:
            return None
        if os.path.dirname(path) == path:
            return None
        return os.path.dirname(path)
    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Confirm")
        msg.setText("File already exists.\nDo you want to replace it?")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        msg.buttonClicked.connect(self.popup_button)
        self.select='&No'
        x = msg.exec_()
    def popup_button(self, i):
        self.select=i.text()
    
