class File:
    """Represents a file to check in a group of files"""
    def __init__(self, path: str, size: int | float, name: str) -> None:
        self.__path = path
        self.__size = size
        self.__name = name

    @property
    def size(self) -> int | float:
        """
        It returns the size of the list.
        :return: The size of the list.
        """
        return self.__size

    @property
    def path(self) -> str:
        """
        It returns the path of the file.
        :return: The path of the file.
        """
        return self.__path

    @property
    def name(self) -> str:
        """
        It returns the name of the object.
        :return: The name of the person
        """
        return self.__name
