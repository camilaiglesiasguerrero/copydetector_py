import os
import csv
import sys
from file import File
from group import Group

Group.same_lines_percent = 60 # Seteo porcentaje de lineas en comun entre archivos

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

print(f"{len(filesToAnalize)} files detected.")
for file in filesToAnalize:
	print(file.path)

# Analisis
groups = list[Group]()

flagOnce=True
for file in filesToAnalize:
    if flagOnce:
        flagOnce=False #solo entro la primera vez
        groups.append(Group(file))

    #pregunto si el archivo pertecene a los grupos
    flagBelong=False
    for group in groups:
        if group.file_belong(file):
            group.append_file(file) #si pertecene a un grupo existente lo agrego
            flagBelong=True
    
    #si no pertenece a ninguno, lo agrego a uno nuevo
    if flagBelong==False:
        groups.append(Group(file))

#Resultados
to_print = [str]
print(f"{len(groups)} groups.")
with open('posiblesCopias.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	for group in groups:
		writer.writerow("POSIBLES COPIAS")
		if group.has_copies:		
			to_print = group.return_files
			for p in to_print:
				writer.writerow(p)
			print(f"Posibles Copias (similitud: {round(group.same_max, 2)}%):")		
			group.print_files()
			print("________________________________\n")