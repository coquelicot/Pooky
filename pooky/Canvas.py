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

class Canvas:
    pass

class CanvasInterface:

    # should be implemented

    def __init__(self, canvas):
        self.canvas = canvas

    def countLine(self):
        raise NotImplementedError("Not implement yet XD")

    def getCanvas(self):
        return self.canvas

    # don't need to implement

    def getRawData(self, st, ed):
        """ Get the raw data from positino st to position ed """
        raise NotImplementedError("Abstract method.")

    def paste(pos, datas):
        """ Paste datas at the position pos """
        raise NotImplementedError("Abstract method.")

    def modifyColor(self, st, ed, front, back):
        """
        Modify blocks' color at the same time.
        Both front and back should be a tuple indicating the origin color and object color.
        """
        raise NotImplementedError("Abstract method.")

    def erase(self, st, ed):
        """ Delete a block of data """
        raise NotImplementedError("Abstract method.")

    def insert(self, pos, data):
        """ Insert datas at the position pos """
        raise NotImplementedError("Abstract method.")

    def replace(self, pos, data):
        """ Replace datas at the position pos """
        raise NotImplementedError("Abstract method.")

class TextInterface(CanvasInterface):
    pass

class GraphicInterface(ConvasInterface):
    pass
