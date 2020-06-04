import os
import csv
from File import File
from Group import Group

Group.bytes_delta = 200 # seteo nivel de similitud a 200 bytes (aprox 200 caracteres)

#cargo archivos a analizar
filesToAnalize = []
# falta cargar estos archivos barriendo los directorios de los proyectos con os.walk
# files.append(File("archivo1.c",400))
# files.append(File("archivo2.c",800))
# files.append(File("archivo3.c",1500))
# files.append(File("archivo4.c",6900))
# files.append(File("archivo5.c",6850))
# files.append(File("archivo6.c",1800))
# files.append(File("archivo7.c",400))
# files.append(File("archivo8.c",10654))
# files.append(File("archivo9.c",15987))
# files.append(File("archivo10.c",15977))

for root, dirs, files in os.walk(".", topdown=False):
	for name in files:
		if name.endswith(".c") and name != "specs.c" and name != "spec.c":
			file_path = os.path.join(root, name)
			file_stats = os.stat(file_path).st_size
			filesToAnalize.append(File(name,file_stats,file_path))

# Analisis
groups = []

flagOnce=True
for f in filesToAnalize:
    if flagOnce:
        flagOnce=False #solo entro la primera vez
        groups.append(Group(f))

    #pregunto si el archivo pertecene a los grupos
    flagBelong=False
    for g in groups:
        if g.file_belong(f):
            g.append_file(f) #si pertecene a un grupo existente lo agrego
            flagBelong=True
    
    #si no pertenece a ninguno, lo agrego a uno nuevo
    if flagBelong==False:
        groups.append(Group(f))


#Resultados
roPrint = []
print("{0} grupos".format(len(groups)))
with open('posiblesCopias.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	for g in groups:
		writer.writerow("POSIBLES COPIAS")
		if g.has_copies():		
			toPrint = g.return_files()
			for p in toPrint:
				writer.writerow(p)
			print("Posibles Copias:")		
			g.print_files()
			print("________________________________\n")