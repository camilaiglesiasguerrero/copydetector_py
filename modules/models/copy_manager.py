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

import os
from modules.models.file import File
from modules.models.group import Group
from modules.models.file_manager import FileManager

class CopyManager:
    """Represents the class CopyManager that is in charge of handle the creation of groups of files that have possible copies"""

    def __init__(self, analyze_path: str, files_manager: FileManager) -> None:
        """
        This function takes a path to a directory and creates a list of files to analyze and a list of
        groups analyzed
        
        :param analyze_path: The path to the directory that contains the files to be analyzed
        :type analyze_path: str
        """
        self.__analyze_path = analyze_path
        self.__files_to_analyze = list[File]()
        self.__groups_analyzed = list[Group]()
        self.__files_sufix = files_manager.files_sufix
        self.__excluded_files = files_manager.excluded_files
    
    @property
    def groups_analyzed(self) -> list[Group]:
        """
        This function takes a list of files and returns a list of groups
        :return: A list of groups
        """
        self.__make_files_to_analyze()
        self.__make_groups()
        return self.__groups_analyzed

    def __print_files_path(self) -> None:
        """
        This function prints the path of each file in the list of files to analyze
        """
        for file in self.__files_to_analyze:
            print(file.path)

    def __make_groups(self) -> None:
        """
        It takes a list of files and returns a list of groups of files
        
        :param files_to_analyze: list[str]
        :type files_to_analyze: list[str]
        :return: A list of groups.
        """
        flag_once = True
        for file in self.__files_to_analyze:
            if flag_once:
                flag_once = False  # only enters the first time
                self.__groups_analyzed.append(Group(file))

            # check if the file belongs to a group
            flag_belong = False
            for group in self.__groups_analyzed:
                if group.file_belong(file):
                    # if the file belongs to an existent group, add its
                    group.append_file(file)
                    flag_belong = True

            # if file not belongs to an existent group, create a new one
            if not flag_belong:
                self.__groups_analyzed.append(Group(file))
    
    def __add_files(self, filename: str, index: str) -> None:
        """
        It takes a filename and an index, and if the filename is not in the excluded files list, it adds
        the file to the files to analyze list
        
        :param filename: str = The name of the file
        :type filename: str
        :param index: tuple
        :type index: str
        """
        if not (filename in self.__excluded_files):
            file_path = os.path.join(index[0], filename)
            file_stats = os.stat(file_path).st_size
            self.__files_to_analyze.append(File(file_path, file_stats, filename))
    
    def __check_filenames(self, index: str, files: list[str]) -> None:
        """
        It takes a list of filenames and adds them to the files to analyze list
        
        :param index: str
        :type index: str
        :param files: list[str]
        :type files: list[str]
        """
        if files:
            for filename in files:
                self.__add_files(filename, index)
    
    def __filter_directories(self, sufix: str, index: str) -> None:
        """
        It filters the files in a directory and checks if the file names are valid
        
        :param sufix: str = '.c'
        :type sufix: str
        :param index: a tuple of 3 elements:
        :type index: str
        """
        if index[2]:
            files = list[str](filter(lambda file: str(file).endswith(sufix), index[2]))
            self.__check_filenames(index, files)

    def __make_files_to_analyze(self) -> None:
        """
        It walks through a directory and returns a list of files that end with .c and are not named specs.c
        or spec.c
        :return: A list of File objects.
        """
        directories = list[str](filter(lambda file: 'Repositories' in file[0], os.walk(self.__analyze_path, topdown=False)))
        for sufix in self.__files_sufix:
            for index in directories:
                self.__filter_directories(sufix, index)

        print(f"{len(self.__files_to_analyze)} files detected.")
        self.__print_files_path()
