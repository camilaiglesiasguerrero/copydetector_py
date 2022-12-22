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
from modules import CoMa

INIT_TESTS_CMD = 'pytest -v'
con = CoMa('./modules/configs.json')

def test_config_manager():
    """
    This function tests the configuration manager
    """
    assert con.script_analize_path == './Repositories'
    
def test_config_percentage():
    """
    This function tests the script_percentage variable in the config.py file
    """
    assert con.script_percentage == 60

def test_is_bool():
    """
    It tests that the type of the `script_sort_desc` attribute of the `con` object is a boolean
    """
    assert type(con.script_sort_desc) == bool

def test_is_list():
    """
    It asserts that the type of the variable `con.script_sufixes` is a list
    """
    assert type(con.script_sufixes) == list

def test_is_df():
    assert con.version == '[V3.0.0.1]'

def test_config_db():
    """
    The function tests the configuration dictionary of the manager
    """
    db_dict = {
        "name": "copies_db",
        "table_name": "students_copies",
        "delete_before_insert": True,
        "paths": {
            "db_file": "./modules/database/copies_db.db",
            "DDL": {
                "create": "./modules/database/queries/DDL/create.sql",
                "drop": "./modules/database/queries/DDL/drop.sql"
            },
            "DML": {
                "insert": "./modules/database/queries/DML/insert.sql",
                "delete": "./modules/database/queries/DML/delete.sql",
                "update": "./modules/database/queries/DML/update.sql",
                "select": "./modules/database/queries/DML/select.sql"
            }
        }
    }
    assert con.cd_config_db == db_dict

def test_ddl_create():
    """
    It tests that the value of the `con.db_ddl_create` attribute is equal to the string
    `./modules/database/queries/DDL/create.sql`
    """
    assert con.db_ddl_create == './modules/database/queries/DDL/create.sql'

def test_ddl_drop():
    """
    This function tests the value of the variable `con.db_ddl_drop` to ensure it is equal to the string
    `./modules/database/queries/DDL/drop.sql`
    """
    assert con.db_ddl_drop == './modules/database/queries/DDL/drop.sql'

def test_dml_insert():
    """
    This function tests the value of the variable `con.db_dml_insert` to ensure it is equal to the
    string `./modules/database/queries/DML/insert.sql`
    """
    assert con.db_dml_insert == './modules/database/queries/DML/insert.sql'

def test_dml_delete():
    """
    This function tests the value of the variable `con.db_dml_delete` to ensure it is equal to the
    string `./modules/database/queries/DML/delete.sql`
    """
    assert con.db_dml_delete == './modules/database/queries/DML/delete.sql'

def test_dml_update():
    """
    This function tests the value of the variable `con.db_dml_update` to ensure it is equal to the
    string `./modules/database/queries/DML/update.sql`
    """
    assert con.db_dml_update == './modules/database/queries/DML/update.sql'

def test_dml_select():
    """
    This function tests the value of the variable `con.db_dml_select` to ensure it is equal to the
    string `./modules/database/queries/DML/select.sql`
    """
    assert con.db_dml_select == './modules/database/queries/DML/select.sql'
