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

import pandas as pd
from modules.models.group import Group


class DataHandler:
    def __init__(self, filename: str, groups: list[Group]) -> None:
        self.__filename = filename
        self.__groups = groups
        self.__columns = ["Is Copy?", "Groups", "Files", "Path", "Percentage"]
        self.__dataframe: pd.DataFrame = pd.DataFrame(columns=self.__columns)

    @property
    def dataframe(self) -> pd.DataFrame:
        """
        It returns the dataframe.
        :return: The dataframe
        """
        return self.__dataframe

    def config_dataframe(self) -> None:
        """
        It takes a list of groups, each group has a list of files, each file has a name and a similarity
        score. 
        
        The function creates a dataframe with the following columns: 
        
        - Is Copy?
        - Groups
        - Files
        - Path
        - Percentage
        
        The function iterates through the list of groups, and for each group, it creates a dataframe
        with the following data: 
        
        - Is Copy?: f'POSIBLE COPIA {i+1}'
        - Groups: f'Group {i+1}'
        - Files: [file.split(';')[0] for file in self.__groups[i].return_files]
        - Path: [file.split(';')[1] for file in self.__groups[i].return_files]
        - Percentage: round(self.__groups[i].same_max, 2)
        """
        for i in range(len(self.__groups)):
            data = {
                self.__columns[0]: f'POSIBLE COPIA {i+1}',
                self.__columns[1]: f'Group {i+1}',
                self.__columns[2]: list[str](map(lambda x: x.strip(), [file.split(';')[0] for file in self.__groups[i].return_files])),
                self.__columns[3]: list[str](map(lambda x: x.strip(), [file.split(';')[1] for file in self.__groups[i].return_files])),
                self.__columns[4]: round(self.__groups[i].same_max, 2)
            }

            df = pd.DataFrame(data=data)
            self.__dataframe = pd.concat(
                [self.__dataframe, df], ignore_index=True, axis=0)

    def print_df(self) -> None:
        """
        It prints the dataframe
        """
        print(self.__dataframe)

    def df_to_csv(self, sort_by_percentaje_desc: bool = False) -> None:
        """
        It takes a dataframe and saves it as a csv file
        """
        if sort_by_percentaje_desc:
            self.__dataframe =\
                self.__dataframe.sort_values(
                    self.__columns[4], ascending=False)
        self.__dataframe.to_csv(self.__filename, sep=',', index=False)
