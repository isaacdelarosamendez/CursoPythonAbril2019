alumnos = ["Isaac", "Humberto"]

#Funcion que devuelve si una cadena
#es mayor a 5
def strIsMayor5(cadena):
	return len(cadena)>5


#Se itera cada elemto del listado
for alumno in alumnos:
	print("Procesando el nombre: "+alumno)
	#Si el nombre es mayor a 5 digitos
	if strIsMayor5(alumno):
		print("El nombre del alumno es correcto")
	else:
		print("El nombre del alumno es muy corto")