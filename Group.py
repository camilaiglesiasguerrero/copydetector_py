class Group:
    bytes_delta=100
	
    def __init__(self,f):
        self.files=[f]
        self.size=f.get_size() # el size del grupo es el del primer file

    def file_belong(self,file):
        delta =  file.get_size() - self.size
        if(delta<0):
            delta=delta*(-1) # lo hago siempre positivo
        if delta <= Group.bytes_delta:
            #el archivo pertenece a este grupo
            return True

        return False

    def append_file(self,file):
        self.files.append(file)

    def has_copies(self):
        if len(self.files)>=2:
            return True
        return False   


    def print_files(self):
        for f in self.files:
            print("Name:{0}\t\tPath:{1}\t\tSize:{2}\n".format(f.get_name(),f.get_path(),f.get_size()))         
	
	
    def return_files(self):
        concat = []
        for f in self.files:
            concat.append("{0} ; {1} ; {2}".format(f.get_name(),f.get_path(),f.get_size()))        
        return concat