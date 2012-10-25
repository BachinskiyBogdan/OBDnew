# -*- coding: utf-8 -*-
'''
    пример загрузки и отображения формы (на форме display)
'''

import sys
from PyQt4.QtGui import *
import display                 #импортируем нужную форму
from PyQt4 import QtCore
app = QApplication(sys.argv)
w = QMainWindow()
w = QMainWindow()
uw = display.Ui_MainWindow()    #сюда подставляем нужное название формы
uw.setupUi(w)
w.show()
sys.exit(app.exec_())
