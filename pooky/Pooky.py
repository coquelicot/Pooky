#!/usr/bin/python3
# -*- coding: utf-8 -*-

# This file is part of Pooky.
# Copyright (C) 2013 Fcrh <coquelicot1117@gmail.com>
#
# Pooky is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pooky is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pooky.  If not, see <http://www.gnu.org/licenses/>.

import sys
from Config import config
from PyQt4 import QtGui, QtCore

class Pooky(QtGui.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):

        self.resize(640, 480)
        self.setWindowTitle('Pooky {0}'.format(config.version))
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
        if name in config.shortCuts:
            action.setShortcut(config.shortCuts[name])
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
