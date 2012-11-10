# -*- coding: utf-8 -*-
'''
    пример загрузки и отображения формы (на форме display)
'''

import sys
from PyQt4.QtGui import *
import log                 #импортируем нужную форму
from PyQt4 import QtCore
#app = QApplication(sys.argv)
#w = QMainWindow()
uw = log.Ui_MainWindow()    #сюда подставляем нужное название формы
#uw.setupUi(w)
uw.Run()
uw.destroy()
#w.show()
#sys.exit(app.exec_())
