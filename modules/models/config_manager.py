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

import pandas as pd

class ConfigManager:
    """Represents the class in charge of init the configs of the script"""
    def __init__(self, file_path: str) -> None:
        self.__file_path = file_path
        self.__main_configs = self.__open_file()
        self.__app_info = self.__main_configs["app_info"]
        self.__cd_configs_full = self.__main_configs["copy_detector"]
    
    def __open_file(self):
        """
        It opens a file, reads it, and then loads the contents of the file into a variable
        """
        return pd.read_json(self.__file_path, orient='records')
    
    # #* BASIC CONFIG
    @property
    def version(self) -> str:
        """
        It returns the version of the app
        :return: The version of the app.
        """
        return self.__app_info["version"]
    
    @property
    def app_name(self) -> str:
        """
        This function returns the name of the app
        :return: The app_name key from the app_info dictionary.
        """
        return self.__app_info["app_name"]
    
    #* COPY DETECTOR CONFIG
    @property
    def cd_config(self) -> dict:
        """
        It returns a dictionary of the configuration of the current environment
        :return: The dictionary of the class.
        """
        return self.__cd_configs_full['configs']
    
    @property
    def cd_config_script(self) -> dict:
        """
        It returns the value of the key 'script' in the dictionary that is the value of the key
        'configs' in the dictionary that is the value of the key 'cd_configs' in the object 'self'
        :return: The value of the key 'script' in the dictionary 'configs' in the dictionary
        'cd_configs'
        """
        return self.__cd_configs_full['configs']['script']
    
    @property
    def script_columns(self) -> list[str]:
        """
        It returns the column names of the dataframe that is stored in the cd_config_script variable
        :return: The columns_name of the cd_config_script
        """
        return self.cd_config_script['columns_name']
    
    @property
    def script_analize_path(self) -> str:
        """
        It returns the path to the folder that contains the files to be analyzed
        :return: The path to the directory to be analyzed.
        """
        return self.cd_config_script['path_to_analize']
    
    @property
    def script_file_output(self) -> str:
        """
        It returns the value of the key 'filename_output' from the dictionary 'cd_config_script'
        :return: The filename_output value from the cd_config_script dictionary.
        """
        return self.cd_config_script['filename_output']
    
    @property
    def script_sort_desc(self) -> bool:
        """
        The function returns a boolean value based on the value of the 'sort_by_percent_desc' key in the
        'cd_config_script' dictionary
        :return: The value of the key 'sort_by_percent_desc' in the dictionary 'cd_config_script'
        """
        return self.cd_config_script['sort_by_percent_desc']
    
    @property
    def script_percentage(self) -> int:
        """
        This function returns the percentage of the script that has been completed
        :return: The percentage of the script.
        """
        return self.cd_config_script['percentage']
    
    @property
    def script_sufixes(self) -> list[str]:
        """
        It returns a list of strings
        :return: The list of files sufix.
        """
        return self.cd_config_script['files_sufix']
    
    @property
    def script_excluded_files(self) -> list[str]:
        """
        This function returns a list of strings that are the excluded files from the config script
        :return: The excluded_files list from the cd_config_script dictionary.
        """
        return self.cd_config_script['excluded_files']
    
    #* DB CONFIGS
    @property
    def cd_config_db(self) -> dict:
        """
        It returns the value of the key 'database' in the dictionary 'configs' in the dictionary
        'cd_configs_full' in the class 'cd_configs'
        :return: The dictionary of the database configuration.
        """
        return self.__cd_configs_full['configs']['database']
    
    @property
    def db_name(self) -> str:
        """
        It returns the name of the database
        :return: The name of the database.
        """
        return self.cd_config_db['name']

    @property
    def db_tablename(self) -> str:
        """
        It returns the table name from the config file
        :return: The table name from the config file.
        """
        return self.cd_config_db['table_name']
    
    @property
    def db_delete_then_insert(self) -> str:
        """
        If the value of the key 'delete_before_insert' in the dictionary 'cd_config_db' is 'True', then
        return the value of the key 'delete_before_insert' in the dictionary 'cd_config_db'
        :return: The value of the key 'delete_before_insert' in the dictionary 'cd_config_db'
        """
        return self.cd_config_db['delete_before_insert']
    
    @property
    def db_path_db_file(self) -> str:
        """
        It returns the path to the database file
        :return: The path to the database file.
        """
        return self.cd_config_db['paths']['db_file']
    
    @property
    def db_ddl_create(self) -> str:
        """
        It returns the path to the DDL create file
        :return: The value of the key 'create' in the dictionary 'DDL' in the dictionary 'paths' in the
        dictionary 'cd_config_db'
        """
        return self.cd_config_db['paths']['DDL']['create']
    
    @property
    def db_ddl_drop(self) -> str:
        """
        It returns the path to the drop DDL file
        :return: The value of the key 'drop' in the dictionary 'DDL' in the dictionary 'paths' in the
        dictionary 'cd_config_db' in the object 'self'.
        """
        return self.cd_config_db['paths']['DDL']['drop']
    
    @property
    def db_dml_delete(self) -> str:
        """
        It returns the path to the DML delete file
        :return: The value of the key 'delete' in the dictionary 'DML' in the dictionary 'paths' in the
        dictionary 'cd_config_db'
        """
        return self.cd_config_db['paths']['DML']['delete']
    
    @property
    def db_dml_insert(self) -> str:
        """
        It returns the path to the DML insert file
        :return: The value of the key 'insert' in the dictionary 'DML' in the dictionary 'paths' in the
        dictionary 'cd_config_db'
        """
        return self.cd_config_db['paths']['DML']['insert']
    
    @property
    def db_dml_update(self) -> str:
        """
        It returns the path to the DML update file
        :return: The value of the key 'update' in the dictionary 'DML' in the dictionary 'paths' in the
        dictionary 'cd_config_db'
        """
        return self.cd_config_db['paths']['DML']['update']
    
    @property
    def db_dml_select(self) -> str:
        """
        It returns the path to the DML select file
        :return: The value of the key 'select' in the dictionary 'DML' in the dictionary 'paths' in the
        dictionary 'cd_config_db'
        """
        return self.cd_config_db['paths']['DML']['select']
