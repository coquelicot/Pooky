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

import yaml, os
from utils.Logger import logger

class Config:

    version = 0.1
    configDir = os.path.join(os.path.dirname(__file__), 'resources', 'config')

    def __init__(self, configFile='config.yaml'):
        self.load(configFile)

    def load(self, fileName):

        try:
            config = Config.loadConfigFile('config.yaml')
        except:
            logger.warning("Can't load `{0}', using `defaultConfig.yaml' instead.".format(fileName))
            config = Config.loadConfigFile('defaultConfig.yaml')

        self.__dict__ = config if config is not None else dict()

    @classmethod
    def loadConfigFile(cls, fileName):

        filePath = os.path.join(cls.configDir, fileName)
        with open(filePath, 'r') as fin:
            return yaml.load(fin)

config = Config()
