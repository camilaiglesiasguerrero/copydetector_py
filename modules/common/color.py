# Copy detector
# Copyright (C) <2020>  <Ernesto Gigliotti>
# Copyright (C) <2020>  <Camila Iglesias>
# Copyright (C) <2022>  <Facundo Falcone> - Improvements

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import enum

class Color(enum.Enum):
    """Enumeration"""
    _B_RED: str = '\033[41m'
    _B_GREEN: str = '\033[42m'
    _B_BLUE: str = '\033[44m'
    _B_WHITE: str = '\033[47m'
    _F_RED: str = '\033[1;31m'
    _F_BLACK: str = '\033[30m'
    _F_WHITE: str = '\033[37m'
    _NO_COLOR: str = '\033[0m'