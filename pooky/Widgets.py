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

from PyQt4 import QtGui

class SingletonWidget(QtGui.QWidget):

    __instance = None

    def __init__(self, *args):
        super().__init__(*args)

        if self.__class__.__instance is not None:
            raise RuntimeError("Singleton check failed.")
        else:
            self.__class__.__instance = self

class Palette(SingletonWidget):

    def __init__(self, *args):
        super().__init__(*args)

class Preference(SingletonWidget):

    def __init__(self, *args):
        super().__init__(*args)
        QtGui.QLabel('Almost Empty XD.', self)

        self.resize(640, 480)
        self.setWindowTitle('Preference')

class About(SingletonWidget):

    def __init__(self, *args):
        super().__init__(*args)

        mainlayout = QtGui.QVBoxLayout()
        mainlayout.addWidget(self.initContent(), True)
        mainlayout.addLayout(self.initButtonLayout(), True)

        self.setLayout(mainlayout)
        self.setWindowTitle('About Pooky')
        self.adjustSize()

    def initButtonLayout(self):

        btnlayout = QtGui.QHBoxLayout()

        licenseBtn = QtGui.QPushButton('License')
        def licenseCallBack():
            raise RuntimeError("Not implement yet.")
        licenseBtn.pressed.connect(licenseCallBack)
        btnlayout.addWidget(licenseBtn)

        closeBtn = QtGui.QPushButton('Close')
        def closeCallBack():
            self.lower()
            self.hide()
        closeBtn.pressed.connect(closeCallBack)
        btnlayout.addWidget(closeBtn)

        return btnlayout

    def initContent(self):
        return QtGui.QWidget()

