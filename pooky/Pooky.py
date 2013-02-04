#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import environ
from PyQt4 import QtGui

class Pooky(QtGui.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle('Pooky {0}'.format(environ.version))
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    pooky = Pooky()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
