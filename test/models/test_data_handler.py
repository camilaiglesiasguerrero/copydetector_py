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
import pandas as pd

from modules import (
    CoMa, DataHandler, File, Group
)

INIT_TESTS_CMD = 'pytest -v'

con = CoMa('./modules/configs.json')
g_1 = Group(File('here', 10, 'my_file'))
g_1.append_file(File('here', 10, 'my_file'))
dhan = DataHandler(con.script_columns, con.script_file_output, [g_1])

def test_is_dataframe():
    """Test if the type is dataframe"""
    assert type(dhan.dataframe) == pd.DataFrame

def test_config_df():
    """Test if can make the proper dataframe configuration"""
    assert dhan.config_dataframe()

def test_can_create_csv_file():
    """Test if the script can create a csv file without errors"""
    assert dhan.df_to_csv()

if __name__ == '__main__':
    os.system(INIT_TESTS_CMD)