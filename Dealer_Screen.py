# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dealer_Screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DealerWindow(object):
    def setupUi(self, DealerWindow):
        DealerWindow.setObjectName("DealerWindow")
        DealerWindow.resize(610, 603)
        DealerWindow.setStyleSheet("background-color: rgb(169, 171, 255);")
        self.centralwidget = QtWidgets.QWidget(DealerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.list_Client = QtWidgets.QListWidget(self.centralwidget)
        self.list_Client.setGeometry(QtCore.QRect(20, 320, 561, 221))
        self.list_Client.setStyleSheet("border: 3px Solid rgb(48, 252, 255);\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px")
        self.list_Client.setObjectName("list_Client")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 260, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        # self.label_3 = QtWidgets.QLabel(self.centralwidget)
        # self.label_3.setGeometry(QtCore.QRect(20, 110, 111, 41))
        # font = QtGui.QFont()
        # font.setPointSize(13)
        # self.label_3.setFont(font)
        # self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        # self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
#         self.Client = QtWidgets.QLineEdit(self.centralwidget)
#         self.Client.setGeometry(QtCore.QRect(110, 100, 321, 71))
#         font = QtGui.QFont()
#         font.setPointSize(16)
#         self.Client.setFont(font)
#         self.Client.setStyleSheet("\n"
# "\n"
# "background-color: rgb(255, 255, 255);\n"
# "border: 3px Solid rgb(48, 252, 255);\n"
# "border-radius: 18px;\n"
# " ")
#         self.Client.setText("")
#         self.Client.setPlaceholderText("")
#         self.Client.setObjectName("Client")
        self.Product = QtWidgets.QLineEdit(self.centralwidget)
        self.Product.setGeometry(QtCore.QRect(110, 120, 321, 120))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Product.setFont(font)
        self.Product.setStyleSheet("\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px Solid rgb(48, 252, 255);\n"
"border-radius: 18px;\n"
" ")
        self.Product.setText("")
        self.Product.setPlaceholderText("")
        self.Product.setObjectName("Product")
        self.Search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Search_btn.setGeometry(QtCore.QRect(450, 100, 141, 161))
        self.Search_btn.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Search_btn.setFont(font)
        self.Search_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Search_btn.setStyleSheet("#Search_btn{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 18px;\n"
"background-color: rgb(60, 255, 39);\n"
"border: 3px Solid rgb(1, 134, 1);\n"
"\n"
"}\n"
"#Search_btn:hover:pressed{\n"
"background-color: rgb(126, 255, 103);\n"
"}")
        self.Search_btn.setObjectName("Search_btn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 271, 51))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 0, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        DealerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DealerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 610, 29))
        self.menubar.setObjectName("menubar")
        DealerWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DealerWindow)
        self.statusbar.setObjectName("statusbar")
        DealerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DealerWindow)
        QtCore.QMetaObject.connectSlotsByName(DealerWindow)

    def retranslateUi(self, DealerWindow):
        _translate = QtCore.QCoreApplication.translate
        DealerWindow.setWindowTitle(_translate("DealerWindow", "MainWindow"))
        self.label.setText(_translate("DealerWindow", "List of Customers and their Products :"))
        # self.label_3.setText(_translate("DealerWindow", "Client :"))
        self.label_4.setText(_translate("DealerWindow", "Produt :"))
        self.Search_btn.setText(_translate("DealerWindow", "Search "))
        self.label_5.setText(_translate("DealerWindow", "Dealer Screen"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     DealerWindow = QtWidgets.QMainWindow()
#     ui = Ui_DealerWindow()
#     ui.setupUi(DealerWindow)
#     DealerWindow.show()
#     sys.exit(app.exec_())
