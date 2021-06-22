from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QMenu, QAction
from PyQt5.QtWidgets import QTableWidgetItem as ti

from Resources import Designs as ds
from models import *
from .add_user import add_dialog


class MainWindow(QMainWindow, ds.main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.MenuActions()
        self.SetColumnWidth()
        self.LoadData()
        self.buttonEvents()

    def buttonEvents(self):
        self.add_button.pressed.connect(self.open_add_dialog)

    def open_add_dialog(self):
        ad = add_dialog(self)
        ad.accepted.connect(self.LoadData)
        ad.exec_()

    def LoadData(self):
        users = User.select().order_by(-User.id)
        self.tw.setRowCount(0)
        for user in users:
            rp = self.tw.rowCount()
            self.tw.insertRow(rp)
            self.tw.setItem(rp, 0, ti(str(rp + 1)))
            self.tw.setItem(rp, 1, ti(user.Name))
            self.tw.setItem(rp, 2, ti(user.Course))
            self.tw.setItem(rp, 3, ti(user.PhoneNumber))
            self.tw.setItem(rp, 4, ti(str(user.Age)))

    def SetColumnWidth(self):
        self.tw.setColumnWidth(0, 50)
        self.tw.setColumnWidth(1, 140)
        self.tw.setColumnWidth(2, 140)
        self.tw.setColumnWidth(3, 140)
        self.tw.setColumnWidth(4, 0)

    def MenuActions(self):
        self.actionExit.triggered.connect(self.close)

    def close(self):
        ret = QMessageBox.question(self, 'Exit', "Do you want to exit?", QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.No)
        if ret == QMessageBox.Yes:
            super(MainWindow, self).close()

    def contextMenuEvent(self, event):
        item = self.tw.itemAt(event.pos().x(), event.pos().y() - 60)
        if item is not None:
            print()
            menu = QMenu(self)
            delete_action = QAction(QIcon(":/mw_icons/delete.png"), "Delete")
            menu.addAction(delete_action)
            action = menu.exec_(self.mapToGlobal(event.pos()))
            if action == delete_action:
                User.get(User.Name == self.tw.item(item.row(), 1).text()).delete_instance()
                self.LoadData()
