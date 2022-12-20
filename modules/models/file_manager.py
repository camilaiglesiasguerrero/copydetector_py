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


from modules.models.config_manager import ConfigManager as CoMa

class FileManager:
    """Represents the file manager class that is in charge of handle the config json file."""

    def __init__(self, config_manager: CoMa) -> None:
        """
        This function is a constructor for the class. It takes a config_manager object as a parameter
        and assigns it to the self.__configs variable
        
        :param config_manager: CoMa
        :type config_manager: CoMa
        """
        self.__configs = config_manager

    @property
    def percentage(self) -> float:
        """
        It returns the percentage of the configs.
        :return: The percentage of the total amount of money that the user wants to invest.
        """
        return float(self.__configs.script_percentage)

    @property
    def output_file_path(self) -> str:
        """
        It returns the value of the key "filename_output" in the dictionary "__configs"
        :return: The output file path.
        """
        return self.__configs.script_file_output

    @property
    def sort_by_percentage(self) -> bool:
        """
        It returns a boolean value that is the value of the key "sort_by_percent_desc" in the dictionary
        "__configs"
        :return: The value of the key "sort_by_percent_desc" in the dictionary "__configs"
        """
        return self.__configs.script_sort_desc

    @property
    def files_sufix(self) -> list[str]:
        """
        It returns a list of strings, which are the sufixes of the files that the program will look for
        :return: A list of strings.
        """
        return self.__configs.script_sufixes
    
    @property
    def excluded_files(self) -> list[str]:
        """
        This function returns a list of strings that are excluded files
        :return: A list of strings.
        """
        return self.__configs.script_excluded_files
