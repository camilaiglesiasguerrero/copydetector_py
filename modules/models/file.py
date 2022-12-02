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

class File:
    """Represents a file to check in a group of files"""

    def __init__(self, path: str, size: int | float, name: str) -> None:
        self.__path = path
        self.__size = size
        self.__name = name

    @property
    def size(self) -> int | float:
        """
        It returns the size of the list.
        :return: The size of the list.
        """
        return self.__size

    @property
    def path(self) -> str:
        """
        It returns the path of the file.
        :return: The path of the file.
        """
        return self.__path

    @property
    def name(self) -> str:
        """
        It returns the name of the object.
        :return: The name of the person
        """
        return self.__name
