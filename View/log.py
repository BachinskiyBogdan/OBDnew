# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log.ui'
#
# Created: Mon Oct 22 21:08:56 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

'''
    username - строка ввода имени пользователя  
    password - строка ввода пароля пользователя
    login_btn - кнопка подтверждения ввода
'''

import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(613, 340)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.password = QtGui.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(360, 120, 113, 20))
        self.password.setInputMask(_fromUtf8(""))
        self.password.setText(_fromUtf8(""))
        self.password.setMaxLength(20)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.password.setObjectName(_fromUtf8("password"))
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
        self.login_btn = QtGui.QPushButton(self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(270, 170, 75, 23))
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
        self.username = QtGui.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(150, 120, 113, 20))
        self.username.setMaxLength(30)
        self.username.setObjectName(_fromUtf8("username"))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 613, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        window = None
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        QtCore.QObject.connect(MainWindow, QtCore.SIGNAL("destroyed()"),QtGui.qApp, QtCore.SLOT('quit()'))
        QtCore.QObject.connect(self.login_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Login)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Пароль", None, QtGui.QApplication.UnicodeUTF8))
        self.login_btn.setText(QtGui.QApplication.translate("MainWindow", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Логин", None, QtGui.QApplication.UnicodeUTF8))

    #obj = 
    
    def Login(self):
        
        user_name = "B"
        pass_word = "1111"
        if (user_name == self.username.text()):
            if (pass_word == self.password.text()):
                import display
                self.username.setText("jjjj")
                app = QApplication(sys.argv)
                w = QMainWindow()
                uw = display.Ui_MainWindow()    #сюда подставляем нужное название формы
                uw.setupUi(w)
                w.show()
                self.emit(QtCore.SIGNAL("destroyed()"))
                sys.exit(app.exec_())
                self.windows.destroy()
        
        # проверка на подленность имени/пароля. нет - error.py, да - display.py
    def Run(self):
        import log
        app = QApplication(sys.argv)
        w = QMainWindow()
        uw = log.Ui_MainWindow()
        self.window = app
        #obj = uw
        uw.setupUi(w)
        w.show()
        sys.exit(app.exec_())
