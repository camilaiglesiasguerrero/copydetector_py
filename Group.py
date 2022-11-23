from file import File


class Group:
    """Represents a group of files."""
    __bytes_delta = 100
    __same_lines_percent_level = 60

    def __init__(self, file: File) -> None:
        """
        This function takes a file as an argument and creates a list of files
        
        :param file: File
        :type file: File
        """
        self.__files = [file]
        self.__group_same_max = 0.0

    def __filter_line(self, line: str)  -> str:
        """
        It takes a string, and removes all the characters in the list "to_filter" from the string
        
        :param line: str - the line of code to filter
        :type line: str
        :return: the line after it has been filtered.
        """
        to_filter = ["}", "{", "\n", "\r", " ", "\t", "break", ";"]
        for filter in to_filter:
            line = line.replace(filter, '')
        return line

    @property
    def has_copies(self) -> bool:
        """
        If the length of the files list is greater than or equal to 2, return True, otherwise return
        False
        :return: a boolean value.
        """
        return len(self.__files) >= 2

    @property
    def return_files(self) -> list[str]:
        """
        It returns a list of strings, each string being the name and path of a file
        :return: A list of strings.
        """
        concat = list()
        for file in self.__files:
            concat.append(f"{file.name} ; {file.path}")
        return concat

    @property
    def same_max(self) -> int | float:
        """
        This function returns the maximum value of the same values in the list
        :return: The value of the attribute __group_same_max
        """
        return self.__group_same_max

    @property
    def same_lines_percent(self) -> int:
        """
        This function returns the percentage of lines that are the same in the two files
        :return: The same_lines_percent_level
        """
        return self.__same_lines_percent_level
    
    @same_lines_percent.setter
    def same_lines_percent(self, level: int) -> None:
        """
        This function takes in a level and sets the same_lines_percent_level to that level
        
        :param level: The level of the logger
        :type level: int
        """
        self.__same_lines_percent_level = level

    def file_belong(self, file: File) -> bool:
        """
        It compares the lines of two files and returns true if the percentage of lines in common is
        greater than a certain threshold
        
        :param file: File
        :type file: File
        :return: The return value is a boolean value.
        """
        # comparo el archivo que vino con todos los de este grupo
        # y me quedo con el % de similitud maximo
        same_percent_max = 0
        for f_in_group in self.__files:
            lines1 = []
            lines2 = []
            with open(f_in_group.path, 'r', encoding="utf-8", errors="replace") as file1:
                with open(file.path, 'r', encoding="utf-8", errors="replace") as file2:

                    for line in file1:
                        line = self.__filter_line(line)
                        if len(line) > 3 and (not ("#include" in line)):
                            lines1.append(line)

                    for line in file2:
                        line = self.__filter_line(line)
                        if len(line) > 3 and (not ("#include" in line)):
                            lines2.append(line)

                    same = set(lines1).intersection(lines2)
                    same_percent = (float(len(same)) /
                                    float(len(lines2))) * 100.0 if lines2 else 0

                    if same_percent > same_percent_max:
                        same_percent_max = same_percent

            #print("Comparo {} con {}...".format(file.get_path(),f_in_group.get_path()))
            #print("Lineas en comun:%.1f %%:" % (same_percent) )
            # for line in same:
            #    print(line)
            # print("__________________________________________")
        # _______________________________________________________

        if same_percent_max >= Group.__same_lines_percent_level:
            # me guardo el maximo de similitud para este grupo
            if (not (file in self.__files)) and same_percent_max > self.__group_same_max:
                self.__group_same_max = same_percent_max
            return True
        else:
            return False

    def append_file(self, actual_file: File) -> None:
        """
        It appends a file to a list of files if the file is not already in the list
        
        :param actual_file: File
        :type actual_file: File
        """
        # lo agrego solo si no es el mismo archivo
        if not (actual_file in self.__files):
            self.__files.append(actual_file)

    def print_files(self) -> None:
        """
        It prints the name and path of each file in the list of files
        """
        for file in self.__files:
            print(f"Name:{file.name}\t\tPath:{file.path}\n")
