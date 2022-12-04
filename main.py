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

import sys
from modules.common.color import Color
from modules.models.group import Group
from modules.models.copy_manager import CopyManager
from modules.models.data_handler import DataHandler
from modules.models.file_manager import FileManager
from modules.database.db_manager import DAOManager


if __name__ == '__main__':
    CONFIG_FILE = './configs.json'
    file_manager = FileManager(CONFIG_FILE)
    dao_manager = DAOManager(CONFIG_FILE)
    OUTPUT_FILE = file_manager.output_file_path

    # Seteo porcentaje de lineas en comun entre archivos
    Group.same_lines_percent_level = file_manager.percentage
    # Leo de los argumentos de la consola el directorio a analizar
    try:
        analize_path = sys.argv[1]
    except Exception as e:
        print(f"{Color._B_RED.value}{Color._F_WHITE.value}>>> System: Path not specified. Using current directory...{Color._NO_COLOR.value}")
        analize_path = "."
    
    copy_manager = CopyManager(analize_path)
    groups = copy_manager.groups_analyzed

    print(f"\n{Color._B_BLUE.value}{Color._F_WHITE.value}>>> System: A total of {len(groups)} groups have been found.{Color._NO_COLOR.value}")
    copies = list[Group](filter(lambda x: x.has_copies, groups))
    print(f"{Color._B_RED.value}{Color._F_WHITE.value}>>> System: {len(copies)} groups with possible copies.{Color._NO_COLOR.value}")

    d_handler = DataHandler(OUTPUT_FILE, copies)
    d_handler.config_dataframe()
    d_handler.print_df()
    d_handler.df_to_csv(file_manager.sort_by_percentage)
    dao_manager.create_table()
    dao_manager.insert_table(d_handler.dataframe)
