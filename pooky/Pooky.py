#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import environ
from PyQt4 import QtGui, QtCore

class Pooky(QtGui.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):

        self.resize(640, 480)
        self.setWindowTitle('Pooky {0}'.format(environ.version))
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

        self.statusBar() # create statusBar
        self.initMenuBar()

        self.show()

    def initMenuBar(self):

        fileMenu = self.menuBar().addMenu('&File')
        self.addActionToMenu('New', 'New', 'New file', self.newFile, fileMenu)
        self.addActionToMenu('Open', 'Open', 'Open file', self.openFile, fileMenu)
        self.addActionToMenu('Save', 'Save', 'Save file', self.saveFile, fileMenu)
        self.addActionToMenu('Close', 'Close Tab', 'Close Tab', self.closeTab, fileMenu)
        fileMenu.addSeparator()
        self.addActionToMenu('Exit', 'Exit', 'Exit Pooky', self.close, fileMenu)

    def addActionToMenu(self, name, label, tip, bind, menu):
        action = QtGui.QAction(QtGui.QIcon(name + '.png'), label, self)
        if name in environ.config['shortCuts']:
            action.setShortcut(environ.config['shortCuts'][name])
        action.setStatusTip(tip)
        action.triggered.connect(bind)
        menu.addAction(action)

    # handlers

    def newFile(self):
        raise NotImplementedError('newFile not yet implement')

    def openFile(self):
        raise NotImplementedError('openFile not yet implement')

    def saveFile(self):
        raise NotImplementedError('saveFile not yet implement')

    def closeTab(self):
        raise NotImplementedError('closeTab not yet implement')

def main():
    app = QtGui.QApplication(sys.argv)
    pooky = Pooky()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
