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

from io import TextIOWrapper
from modules.models.file import File

class Group:
    """Represents a group of files."""
    same_lines_percent_level = 60
    __to_filter = ["}", "{", "\n", "\r", " ", "\t", "break", ";"]

    def __init__(self, file: File) -> None:
        """
        This function takes a file as an argument and creates a list of files
        
        :param file: File
        :type file: File
        """
        self.__files = [file]
        self.__group_same_max = 0.0
    
    @property
    def has_copies(self) -> bool:
        """
        If the length of the files list is greater than or equal to 2, return True, otherwise return
        False
        :return: a boolean value.
        """
        return len(self.__files) >= 2

    @property
    def return_files(self) -> list[str]:
        """
        It returns a list of strings, each string being the name and path of a file
        :return: A list of strings.
        """
        concat = list()
        for file in self.__files:
            concat.append(f"{file.name} ; {file.path}")
        return concat

    @property
    def same_max(self) -> int | float:
        """
        This function returns the maximum value of the same values in the list
        :return: The value of the attribute __group_same_max
        """
        return self.__group_same_max

    @property
    def same_lines_percent(self) -> int:
        """
        This function returns the percentage of lines that are the same in the two files
        :return: The same_lines_percent_level
        """
        return Group.same_lines_percent_level

    @same_lines_percent.setter
    def same_lines_percent(self, level: float) -> None:
        """
        This function takes in a level and sets the same_lines_percent_level to that level
        
        :param level: The minimun percentage to consider if is a copy
        :type level: float
        """
        Group._same_lines_percent_level = level

    def __filter_line(self, line: str) -> str:
        """
        It takes a string, and removes all the characters in the list "to_filter" from the string
        
        :param line: str - the line of code to filter
        :type line: str
        :return: the line after it has been filtered.
        """
        for filter in self.__to_filter:
            line = line.replace(filter, '')
        return line

    def __filter_and_append_line(self, list_lines: list[str], file: TextIOWrapper) -> None:
        """
        It takes a list of strings and a file, and for each line in the file, it filters the line, and
        if the line is longer than 3 characters and doesn't contain the string "#include", it appends
        the line to the list
        
        :param list_lines: list[str]
        :type list_lines: list[str]
        :param file: TextIOWrapper
        :type file: TextIOWrapper
        """
        for line in file:
            line = self.__filter_line(line)
            if len(line) > 3 and (not ("#include" in line)):
                list_lines.append(line)

    def file_belong(self, file: File) -> bool:
        """
        It compares the lines of two files and returns true if the percentage of lines in common is
        greater than a certain threshold
        
        :param file: File
        :type file: File
        :return: The return value is a boolean value.
        """
        same_percent_max = 0
        for f_in_group in self.__files:
            lines1 = []
            lines2 = []
            with open(f_in_group.path, 'r', encoding="utf-8", errors="replace") as file1:
                with open(file.path, 'r', encoding="utf-8", errors="replace") as file2:

                    self.__filter_and_append_line(lines1, file1)
                    self.__filter_and_append_line(lines2, file2)

                    same = set(lines1).intersection(lines2)
                    same_percent = (len(same) / float(len(lines2))) * 100.0 if lines2 else 0

                    if same_percent > same_percent_max:
                        same_percent_max = same_percent

        if same_percent_max >= Group.same_lines_percent_level:
            if (not (file in self.__files)) and same_percent_max > self.__group_same_max:
                self.__group_same_max = same_percent_max
            return True
        else:
            return False

    def append_file(self, actual_file: File) -> None:
        """
        It appends a file to a list of files if the file is not already in the list
        
        :param actual_file: File
        :type actual_file: File
        """
        if not (actual_file in self.__files):
            self.__files.append(actual_file)

    def print_files(self) -> None:
        """
        It prints the name and path of each file in the list of files
        """
        for file in self.__files:
            print(f"Name:{file.name}\t\tPath:{file.path}\n")
