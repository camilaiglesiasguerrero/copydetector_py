import os
import csv
import sys
from File import File
from Group import Group

Group.same_lines_percent_level = 60 # Seteo porcentaje de lineas en comun entre archivos

# Leo de los argumentos de la consola el directorio a analizar
try:
	analize_path = sys.argv[1]
except Exception as e:
	print("Path no specified. Using current directory...")
	analize_path="."


#cargo archivos a analizar
filesToAnalize = []

for root, dirs, files in os.walk(analize_path, topdown=False):
	for name in files:
		if name.endswith(".c") and name != "specs.c" and name != "spec.c":
			file_path = os.path.join(root, name)
			file_stats = os.stat(file_path).st_size
			filesToAnalize.append(File(file_path,file_stats,name))

print("{0} files detected.".format(len(filesToAnalize)))
for f in filesToAnalize:
	print(f.get_path())

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
print("{0} groups.".format(len(groups)))
with open('posiblesCopias.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	for g in groups:
		writer.writerow("POSIBLES COPIAS")
		if g.has_copies():		
			toPrint = g.return_files()
			for p in toPrint:
				writer.writerow(p)
			print("Posibles Copias (%% similitud:%.1f):" % (g.get_same_max()))		
			g.print_files()
			print("________________________________\n")