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

from test.models.test_config_manager import (
    test_is_bool, test_dml_update, test_config_db, test_config_manager,
    test_config_percentage, test_ddl_create, test_ddl_drop, test_dml_insert,
    test_dml_delete, test_dml_select, test_is_df, test_is_list
)

from test.models.test_data_handler import (
    test_is_dataframe
)