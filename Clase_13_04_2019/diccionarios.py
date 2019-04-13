from clase import Suma,Saludo

carro = {
}

for x in range(1,3):
	propiedad  = input("Ingrese el nombre de la propiedad ")
	if len(propiedad)<6:
		print("Ingrese una propiedad mayor a 6")
	else:
		carro[propiedad]=""

#funcion que asigna un valor a una propiedad
def setPropiedad(propiedad,valor):
	carro[propiedad]= valor

#funcion que obtiene el valor de una propiedad
def getPropiedad(propiedad):
	return carro[propiedad]

#Itero cada propiedad del diccionario
for propiedad in carro:
	#pido al usuario el valor de la propiedad
	valor = input("Ingrese el valor para "+str(propiedad))
	setPropiedad(propiedad,valor)

#Imprimo el diccionario
for propiedad in carro:
	print(str(propiedad) + " : " + getPropiedad(propiedad))

