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

import json
import re
import sqlite3 as db
from pandas import DataFrame

class DAOManager:
    "Represents the DAO Manager, using SQLite"
    def __init__(self, file_path: str) -> None:
        self.__file_path = file_path
        self.__db_configs = self.__open_config_file()
        self.__db_name: str = self.__db_configs['name']
        self.__insert_deleting_before = self.__db_configs['delete_before_insert']
        self.__table: str = self.__db_configs['table_name']
        self.__db_output_file: str = self.__db_configs['paths']['db_file']
        self.__ddl_paths: dict = self.__db_configs['paths']['DDL']
        self.__dml_paths: dict = self.__db_configs['paths']['DML']


    def __open_config_file(self) -> dict:
        """
        It opens a json file, reads it, and returns a dictionary
        :return: A dictionary
        """
        with open(self.__file_path, 'r') as db_config:
            return json.load(db_config)["configs"]['database']
    
    def __open_query_file(self, query_path: str) -> str:
        """
        It opens a file, reads it, and returns the contents of the file
        
        :param query_path: The path to the query file
        :type query_path: str
        :return: The query file is being returned.
        """
        with open(query_path, 'r') as db_config:
            return db_config.read()

    def __execute_query(self, query: str, error_msg: str):
        """
        It connects to a database, executes a query and returns the result
        
        :param query: str - the query to be executed
        :type query: str
        :param error_msg: str = 'Error while processing data'
        :type error_msg: str
        :return: The result of the query.
        """
        with db.connect(f'{self.__db_output_file}') as conection:
            try:
                result = conection.execute(query)
                if result:
                    print('New data processed')
                return result
            except db.OperationalError as oe:
                print(error_msg, oe)
    
    def __execute_multiple_queries(self, queries: list[str], error_msg: str):
        """
        It executes a list of queries and returns the result of the last query.
        
        :param queries: list[str]
        :type queries: list[str]
        :param error_msg: str = 'Error while processing new data'
        :type error_msg: str
        :return: The result of the last query executed.
        """
        with db.connect(f'{self.__db_output_file}') as conection:
            try:
                for query in queries:
                    result = conection.execute(query)
                conection.commit()
                if result:
                    print('New data processed')
                return result
            except db.OperationalError as oe:
                print(error_msg, oe)

    def __replace_table_name(self, query: str) -> str:
        """
        It takes a query string and replaces the string 'T_NAME' with the name of the table
        
        :param query: The query to be executed
        :type query: str
        :return: The query is being returned with the table name replaced.
        """
        return query.replace('T_NAME', self.__table)

    def create_table(self):
        """
        It opens a file, reads the contents, replaces a string in the contents, and then executes the
        query creating the table if not exists.
        """
        query = self.__replace_table_name(self.__open_query_file(self.__ddl_paths['create']))
        self.__execute_query(query, 'Table already exists')
    
    def insert(self, dataframe: DataFrame):
        """
        It takes a dataframe, creates a list of tuples from the dataframe, then creates a list of
        queries from the tuples, then executes the queries.
        
        :param dataframe: DataFrame
        :type dataframe: DataFrame
        """
        if self.__insert_deleting_before:
            self.delete()
        query = self.__replace_table_name(self.__open_query_file(self.__dml_paths['insert']))
        to_replace = re.findall("1_.", query)
        tuples_list = dataframe.itertuples(index=False, name=None)
        queries = list[str]()
        for l_tuple in tuples_list:
            for i in range(len(l_tuple)):
                query_replaced = query.replace(to_replace[i], f'{l_tuple[i]}')
            queries.append(query_replaced)
        self.__execute_multiple_queries(queries, 'Error adding the rows')
    
    def delete(self):
        """
        It opens a file, reads the contents of the file, replaces the table name in the file with the
        table name provided by the user, executes the query and prints a message
        """
        query = self.__replace_table_name(self.__open_query_file(self.__dml_paths['delete']))
        self.__execute_query(query, 'Table deleted successfully')
        
