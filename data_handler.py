import pandas as pd
from group import Group

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
                self.__columns[2]: [file.split(';')[0] for file in self.__groups[i].return_files], 
                self.__columns[3]: [file.split(';')[1] for file in self.__groups[i].return_files], 
                self.__columns[4]: round(self.__groups[i].same_max, 2)
            }
            
            df = pd.DataFrame(data=data)
            self.__dataframe = pd.concat([self.__dataframe, df], ignore_index=True, axis=0)
    
    def print_df(self) -> None:
        """
        It prints the dataframe
        """
        print(self.__dataframe)

    def df_to_csv(self) -> None:
        """
        It takes a dataframe and saves it as a csv file
        """
        self.__dataframe.to_csv(self.__filename, sep=',', index=False)