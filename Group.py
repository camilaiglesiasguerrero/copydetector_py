class Group:
    bytes_delta=100
    same_lines_percent_level=60
	
    def __init__(self,f):
        self.files=[f]
        self.group_same_max=0


    def file_belong(self,file):
        #comparo el archivo que vino con todos los de este grupo
        #y me quedo con el % de similitud maximo
        same_percent_max=0
        for f_in_group in self.files:
            lines1=[]
            lines2=[]
            with open(f_in_group.get_path(), 'r',encoding="utf-8") as file1:
                with open(file.get_path(), 'r',encoding="utf-8") as file2:

                    for l in file1:
                        l = self.__filter_line(l)
                        if len(l)>3 and (("#include" in l)==False) :
                            lines1.append(l)
                    
                    for l in file2:
                        l = self.__filter_line(l)
                        if len(l)>3 and (("#include" in l)==False):
                            lines2.append(l)

                    same = set(lines1).intersection(lines2)
                    if len(lines2)>0:
                        same_percent = (float(len(same)) / float(len(lines2))) * 100.0
                    else:
                        same_percent = 0
                        
                    if same_percent > same_percent_max:
                        same_percent_max=same_percent 

            #print("Comparo {} con {}...".format(file.get_path(),f_in_group.get_path()))
            #print("Lineas en comun:%.1f %%:" % (same_percent) )
            #for line in same:
            #    print(line)
            #print("__________________________________________")
        #_______________________________________________________


        if same_percent_max >= Group.same_lines_percent_level:
            #me guardo el maximo de similitud para este grupo
            if ((file in self.files)==False) and same_percent_max > self.group_same_max:
                self.group_same_max = same_percent_max

            return True
        else:
            return False 



    def append_file(self,file):
        #lo agrego solo si no es el mismo archivo
        if (file in self.files) == False:
            self.files.append(file)


    def has_copies(self):
        if len(self.files)>=2:
            return True
        return False   


    def print_files(self):
        for f in self.files:
            print("Name:{0}\t\tPath:{1}\n".format(f.get_name(),f.get_path()))         
	
	
    def return_files(self):
        concat = []
        for f in self.files:
            concat.append("{0} ; {1}".format(f.get_name(),f.get_path()))        
        return concat

    def get_same_max(self):
        return self.group_same_max


    def __filter_line(self,l):
        l = l.replace("}","")
        l = l.replace("{","")
        l = l.replace("\n","")
        l = l.replace("\r","")
        l = l.replace(" ","")
        l = l.replace("\t","")
        l = l.replace("break","")
        l = l.replace(";","")
        return l