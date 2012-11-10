# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View\Delete.ui'
#
# Created: Fri Oct 05 22:01:11 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!


'''
    Yes_btn - подтверждение удаления элемента
    No_btn - отказ удаления
    
'''


from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(555, 245)
        MainWindow.setMinimumSize(QtCore.QSize(555, 245))
        MainWindow.setMaximumSize(QtCore.QSize(555, 245))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 351, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.Yes_btn = QtGui.QPushButton(self.centralwidget)
        self.Yes_btn.setGeometry(QtCore.QRect(140, 170, 71, 41))
        self.Yes_btn.setObjectName(_fromUtf8("Yes_btn"))
        self.No_btn = QtGui.QPushButton(self.centralwidget)
        self.No_btn.setGeometry(QtCore.QRect(350, 170, 71, 41))
        self.No_btn.setObjectName(_fromUtf8("No_btn"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 555, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        QtCore.QObject.connect(self.Yes_btn, QtCore.SIGNAL("clicked()"), self.OK)
        QtCore.QObject.connect(self.No_btn, QtCore.SIGNAL("clicked()"), self.Cancel)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Вы действительно хотите удалить этот элемент?</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.Yes_btn.setText(QtGui.QApplication.translate("MainWindow", "Yes", None, QtGui.QApplication.UnicodeUTF8))
        self.No_btn.setText(QtGui.QApplication.translate("MainWindow", "No", None, QtGui.QApplication.UnicodeUTF8))

    def OK (self)
        i = 1
        #действия, когда подтреждено удаление

    def Cancel (self)
        i = 1
        #действия, при отмене удаления

    

