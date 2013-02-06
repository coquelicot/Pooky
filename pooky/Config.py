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

from PyQt4 import QtCore
import yaml, os
from Utils import logger

class Config(QtCore.QObject):

    version = 0.1
    configDir = os.path.join(os.path.dirname(__file__), 'resources', 'config')

    reloaded = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        try:
            config = Config.loadConfigFile('config.yaml')
        except:
            logger.warning("Can't load `config.yaml', using `defaultConfig.yaml' instead.")
            config = Config.loadConfigFile('defaultConfig.yaml')
        finally:
            self.__dict__ = config if config is not None else dict()

    def reload(self, fileName):
        try:
            config = Config.loadConfigFile(fileName)
            self.__dict__ = config if config is not None else dict()
            self.reloaded.emit()
        except:
            logger.warning("Can't reload from file `{0}'.".format(fileName))

    def save(self, fileName):
        filePath = os.path.join(cls.configDir, fileName)
        with open(filePath, 'w') as fout:
            yaml.dump(self.__dict__, fout)

    @classmethod
    def loadConfigFile(cls, fileName):
        filePath = os.path.join(cls.configDir, fileName)
        with open(filePath, 'r') as fin:
            return yaml.load(fin)

config = Config()
