# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View\forms\Insert.ui'
#
# Created: Fri Oct 05 22:07:17 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!


'''
    Origin_line_Edit -  строка ввода первого поля базы данных
    AirportID_line_Edit - строка ввода второго поля базы данных
    City_MarketID_line_Edit - строка ввода третьего поля базы данных
    State_line_Edit - строка ввода четвертого поля базы данных
    State_Name_line_Edit - строка ввода пятого поля базы данных
    Distance_line_Edit - строка ввода шестого поля базы данных

    OK_btn - подтверждение вставки нового элеметна базы данных
    Cancel_btn - отмена вставки
    
'''


from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(510, 434)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Origin_line_Edit = QtGui.QLineEdit(self.centralwidget)
        self.Origin_line_Edit.setGeometry(QtCore.QRect(300, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.Origin_line_Edit.setFont(font)
        self.Origin_line_Edit.setMaxLength(3)
        self.Origin_line_Edit.setAlignment(QtCore.Qt.AlignCenter)
        self.Origin_line_Edit.setObjectName(_fromUtf8("Origin_line_Edit"))
        self.AirportID_line_Edit = QtGui.QLineEdit(self.centralwidget)
        self.AirportID_line_Edit.setGeometry(QtCore.QRect(300, 80, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.AirportID_line_Edit.setFont(font)
        self.AirportID_line_Edit.setMaxLength(5)
        self.AirportID_line_Edit.setAlignment(QtCore.Qt.AlignCenter)
        self.AirportID_line_Edit.setObjectName(_fromUtf8("AirportID_line_Edit"))
        self.City_MarketID_line_Edit = QtGui.QLineEdit(self.centralwidget)
        self.City_MarketID_line_Edit.setGeometry(QtCore.QRect(300, 130, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.City_MarketID_line_Edit.setFont(font)
        self.City_MarketID_line_Edit.setMaxLength(5)
        self.City_MarketID_line_Edit.setAlignment(QtCore.Qt.AlignCenter)
        self.City_MarketID_line_Edit.setObjectName(_fromUtf8("City_MarketID_line_Edit"))
        self.Distance_line_Edit = QtGui.QLineEdit(self.centralwidget)
        self.Distance_line_Edit.setGeometry(QtCore.QRect(300, 280, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.Distance_line_Edit.setFont(font)
        self.Distance_line_Edit.setMaxLength(5)
        self.Distance_line_Edit.setAlignment(QtCore.Qt.AlignCenter)
        self.Distance_line_Edit.setObjectName(_fromUtf8("Distance_line_Edit"))
        self.State_line_Edit = QtGui.QLineEdit(self.centralwidget)
        self.State_line_Edit.setGeometry(QtCore.QRect(300, 180, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.State_line_Edit.setFont(font)
        self.State_line_Edit.setMaxLength(2)
        self.State_line_Edit.setAlignment(QtCore.Qt.AlignCenter)
        self.State_line_Edit.setObjectName(_fromUtf8("State_line_Edit"))
        self.State_Name_line_Edit = QtGui.QLineEdit(self.centralwidget)
        self.State_Name_line_Edit.setGeometry(QtCore.QRect(300, 230, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.State_Name_line_Edit.setFont(font)
        self.State_Name_line_Edit.setMaxLength(20)
        self.State_Name_line_Edit.setAlignment(QtCore.Qt.AlignCenter)
        self.State_Name_line_Edit.setObjectName(_fromUtf8("State_Name_line_Edit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 180, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 130, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 280, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 230, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.OK_btn = QtGui.QPushButton(self.centralwidget)
        self.OK_btn.setGeometry(QtCore.QRect(160, 350, 71, 31))
        self.OK_btn.setObjectName(_fromUtf8("OK_btn"))
        self.Cancel_btn = QtGui.QPushButton(self.centralwidget)
        self.Cancel_btn.setGeometry(QtCore.QRect(280, 350, 71, 31))
        self.Cancel_btn.setObjectName(_fromUtf8("Cancel_btn"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Insert", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Origin", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "OriginAirportID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "OriginState", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "OriginCityMarketID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Distance", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "OriginStateName", None, QtGui.QApplication.UnicodeUTF8))
        self.OK_btn.setText(QtGui.QApplication.translate("MainWindow", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.Cancel_btn.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

