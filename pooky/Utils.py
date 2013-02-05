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

import logging
from Enums import Color

logging.basicConfig(format='[%(asctime)s] %(message)s')
logger = logging.getLogger('Pooky')

# TODO: support other effects
def BBSToRaw(bbsStr):

    result = []
    front = Color.F_WHITE
    back = Color.B_BLACK

    try:
        idx, lim = 0, len(bbsStr)
        while idx < lim:

            if bbsStr[idx] != '\033':
                result.append((ord(bbsStr[idx]), front, back))
                idx += 1

            else:
                st = idx + 2 # skip '['
                ed = bbsStr.find('m', st)
                if ed < 0:
                    raise RuntimeError("Color code not ended.")

                isLight = False
                front = Color.F_WHITE
                back = Color.B_BLACK
                for code in map(int, filter(str.isdigit, bbsStr[st:ed].split(';'))):
                    if code == Color.E_LIGHT:
                        isLight = True
                    elif code == Color.E_RESET:
                        isLight = False
                        front = Color.F_WHITE
                        back = Color.B_BLACK
                    elif Color.isFrontColor(code):
                        front = code
                    elif Color.isBackColor(code):
                        back = code
                    else:
                        logger.warning('Unknown color code. May be unsupport effect?')
                # XXX: ugly
                if isLight:
                    front += 100
                
                idx = ed + 1

    except Exception as e:
        logger.error(e)

    return result

# TODO: optimize
def RawToBBS(datas):

    result = ''
    front = Color.F_WHITE
    back = Color.B_BLACK

    for data in datas:

        if data[1] != front or data[2] != back:

            codes = ['1'] if data[1] > 100 else ['0']
            if data[1] % 100 != Color.F_WHITE:
                codes.append(str(data[1] % 100))
            if data[2] != Color.B_BLACK:
                codes.append(str(data[2]))

            result += '\033[' + ';'.join(codes) + 'm'
            front, back = data[1], data[2]

        result += chr(data[0])

    return result

