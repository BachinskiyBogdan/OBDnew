# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View\login.ui'
#
# Created: Fri Oct 05 22:00:04 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!
'''
    username - строка ввода имени пользователя  
    password - строка ввода пароля пользователя
    login_btn - кнопка подтверждения ввода
'''
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        LoginWindow.setObjectName(_fromUtf8("LoginWindow"))
        LoginWindow.setEnabled(True)
        LoginWindow.resize(613, 337)
        LoginWindow.setMinimumSize(QtCore.QSize(613, 337))
        LoginWindow.setMaximumSize(QtCore.QSize(613, 337))
        self.centralwidget = QtGui.QWidget(LoginWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.username = QtGui.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(150, 120, 113, 20))
        self.username.setMaxLength(30)
        self.username.setObjectName(_fromUtf8("username"))
        self.password = QtGui.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(360, 120, 113, 20))
        self.password.setInputMask(_fromUtf8(""))
        self.password.setText(_fromUtf8(""))
        self.password.setMaxLength(20)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.password.setObjectName(_fromUtf8("password"))
        self.login_btn = QtGui.QPushButton(self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(270, 170, 75, 23))
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 100, 46, 13))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 100, 61, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 613, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(LoginWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QtGui.QApplication.translate("LoginWindow", "Login", "авторизация", QtGui.QApplication.UnicodeUTF8))
        self.login_btn.setText(QtGui.QApplication.translate("LoginWindow", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("LoginWindow", "Логин", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("LoginWindow", "Пароль", None, QtGui.QApplication.UnicodeUTF8))

