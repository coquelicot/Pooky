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

class Color:

    ALL = -1
    NONE = -2

    E_RESET = 0
    # XXX: In fact, it's bold.
    E_LIGHT = 1
    # XXX: not in standard?
    E_BLINK = 5

    F_BLACK  = 30
    F_RED    = 31
    F_GREEN  = 32
    F_YELLOW = 33
    F_BLUE   = 34
    F_PURPLE = 35
    F_CYAN   = 36
    F_WHITE  = 37

    # XXX: a bit ugly
    F_LBLACK  = 130
    F_LRED    = 131
    F_LGREEN  = 132
    F_LYELLOW = 133
    F_LBLUE   = 134
    F_LPURPLE = 135
    F_LCYAN   = 136
    F_LWHITE  = 137

    B_BLACK  = 40
    B_RED    = 41
    B_GREEN  = 42
    B_YELLOW = 43
    B_BLUE   = 44
    B_PURPLE = 45
    B_CYAN   = 46
    B_WHITE  = 47

    # There're severl codes in standard,
    # But pcman don't seems to support them.?

    @classmethod
    def isFrontColor(cls, color):
        # XXX: should [130, 137] be regard as front color?
        return color >= 30 and color <= 37

    @classmethod
    def isBackColor(cls, color):
        return color >= 40 and color <= 47

