# GNU General Public License V3
#
# Copyright (C) <2022>  <Facundo Falcone>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from modules.common.color import Color
from modules.models.group import Group
from modules.models.config_manager import ConfigManager as CoMa
from modules.models.copy_manager import CopyManager
from modules.database.db_manager import DAOManager
from modules.models.data_handler import DataHandler
from modules.models.file_manager import FileManager

class CopyDetectorManager:
    """Represents the manager that is in charge of analize the files and detect copies, 
    create the dataframes & csv file, then insert into the db the registers found."""

    def __init__(self, config_manager: CoMa) -> None:
        self.__config_manager = config_manager

    def start_checking_copies(self):
        """
        It checks for copies in a folder and outputs the results in a csv file, the saves
        the results into the DB.
        """
        file_manager = FileManager(self.__config_manager)
        dao_manager = DAOManager(self.__config_manager)
        OUTPUT_FILE = file_manager.output_file_path

        # Sets the common lines percentage between files
        Group.same_lines_percent_level = file_manager.percentage
        copy_manager = CopyManager(self.__config_manager.script_analize_path, file_manager)
        groups = copy_manager.groups_analyzed

        print(f"\n{Color._B_BLUE.value}{Color._F_WHITE.value}>>> System: A total of {len(groups)} groups have been found.{Color._NO_COLOR.value}")
        copies = list[Group](filter(lambda x: x.has_copies, groups))
        print(f"{Color._B_RED.value}{Color._F_WHITE.value}>>> System: {len(copies)} groups with possible copies.{Color._NO_COLOR.value}")

        d_handler = DataHandler(self.__config_manager.script_columns, OUTPUT_FILE, copies)
        d_handler.config_dataframe()
        d_handler.print_df()
        d_handler.df_to_csv(file_manager.sort_by_percentage)
        dao_manager.create_table()
        dao_manager.insert_table(d_handler.dataframe)

        print(
            f'{Color._B_GREEN.value}{Color._F_WHITE.value}>>> System: Finished.{Color._NO_COLOR.value}',
            f'{Color._B_BLUE.value}{Color._F_WHITE.value}>>> System: Thanks for using {self.__config_manager.app_name} v{self.__config_manager.version}{Color._NO_COLOR.value}',
            sep='\n')
