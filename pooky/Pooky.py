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
        self.newAction = self.addActionToMenu('New', 'New', 'New file', self.newFile, fileMenu)
        self.openAction = self.addActionToMenu('Open', 'Open', 'Open file', self.openFile, fileMenu)
        self.saveAction = self.addActionToMenu('Save', 'Save', 'Save file', self.saveFile, fileMenu)
        self.closeAction = self.addActionToMenu('Close', 'Close Tab', 'Close tab', self.closeTab, fileMenu)
        fileMenu.addSeparator()
        self.exitAction = self.addActionToMenu('Exit', 'Exit', 'Exit Pooky', self.close, fileMenu)
        self.saveAction.setDisabled(True)
        self.closeAction.setDisabled(True)

        editMenu = self.menuBar().addMenu('&Edit')
        self.copyAction = self.addActionToMenu('Copy', 'Copy', 'Copy selected region', self.copy, editMenu)
        self.pasteAction = self.addActionToMenu('Paste', 'Paste', 'Paste the copied data', self.paste, editMenu)
        editMenu.addSeparator()
        self.preferenceAction = self.addActionToMenu('Preference', 'Preference', 'Open the setting panel', self.showPreferencePanel, editMenu)
        self.copyAction.setDisabled(True)
        self.pasteAction.setDisabled(True)

        toolMenu = self.menuBar().addMenu('&Tool')

        helpMenu = self.menuBar().addMenu('&Help')
        self.aboutAction = self.addActionToMenu('About', 'About Pooky', 'Show the about page of Pooky', self.showAbout, helpMenu)

    def addActionToMenu(self, name, label, tip, bind, menu):
        action = QtGui.QAction(QtGui.QIcon(name + '.png'), label, self)
        if name in config.shortCuts:
            action.setShortcut(config.shortCuts[name])
        action.setStatusTip(tip)
        action.triggered.connect(bind)
        menu.addAction(action)
        return action

    # handlers

    def newFile(self):
        raise NotImplementedError('newFile not yet implement')

    def openFile(self):
        raise NotImplementedError('openFile not yet implement')

    def saveFile(self):
        raise NotImplementedError('saveFile not yet implement')

    def closeTab(self):
        raise NotImplementedError('closeTab not yet implement')

    def copy(self):
        raise NotImplementedError('copy not yet implement')
    
    def paste(self):
        raise NotImplementedError('paste not yet implement')

    def showPreferencePanel(self):
        raise NotImplementedError('showPreferencePanel not yet implement')

    def showAbout(self):
        raise NotImplementedError('showAbout not yet implement')

def main():

    app = QtGui.QApplication(sys.argv)
    pooky = Pooky()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
