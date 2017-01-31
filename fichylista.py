#!/usr/bin/python3
fich = open("/etc/passwd","r");
maquinas = fich.readlines();

for usuarios in maquinas:
	separado = usuarios.split(":");
	print(separado[0] + " su shell es: " + separado[-1])

print("El numero de maquinas es: " + str(len(maquinas)));
	
fich.close();

