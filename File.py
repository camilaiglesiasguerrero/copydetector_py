class File:


    def __init__(self,path,size,name):
        self.path=path
        self.size = size
        self.name = name


    def get_size(self):
        return self.size

    def get_path(self):
        return self.path
		
    def get_name(self):
        return self.name