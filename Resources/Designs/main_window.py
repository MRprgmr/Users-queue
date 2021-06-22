# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/UI/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(562, 622)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mw_icons/mw_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tw = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tw.setFont(font)
        self.tw.setStyleSheet("")
        self.tw.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tw.setTabKeyNavigation(True)
        self.tw.setProperty("showDropIndicator", True)
        self.tw.setDragEnabled(False)
        self.tw.setAlternatingRowColors(True)
        self.tw.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tw.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tw.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tw.setRowCount(0)
        self.tw.setColumnCount(5)
        self.tw.setObjectName("tw")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(11)
        item.setFont(font)
        self.tw.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(11)
        item.setFont(font)
        self.tw.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(11)
        item.setFont(font)
        self.tw.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(11)
        item.setFont(font)
        self.tw.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(11)
        item.setFont(font)
        self.tw.setHorizontalHeaderItem(4, item)
        self.tw.horizontalHeader().setMinimumSectionSize(40)
        self.tw.horizontalHeader().setStretchLastSection(True)
        self.tw.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tw, 0, 0, 1, 1)
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.add_button.setFont(font)
        self.add_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_button.setStyleSheet("QPushButton{\n"
"background-color: white;\n"
"border: 2px solid #02ACE5;\n"
"min-width: 80px;\n"
"min-height: 24px;\n"
"color: #0096C7;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #02ACE5;\n"
"border: 2px solid #02ACE5;\n"
"min-width: 80px;\n"
"color: white;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #09A2D4;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/mw_icons/add_user.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.add_button.setIcon(icon1)
        self.add_button.setIconSize(QtCore.QSize(24, 24))
        self.add_button.setObjectName("add_button")
        self.gridLayout.addWidget(self.add_button, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 562, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/mw_icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionExit.setIcon(icon2)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Users Queue"))
        item = self.tw.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tw.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tw.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Course"))
        item = self.tw.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Phone Number"))
        item = self.tw.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Age"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())