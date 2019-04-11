'''Ejemplo de funciones
Teoria basada de : https://devcode.la/tutoriales/funciones-en-python/
'''

#funcion de tipo RETORNO, que regresa la suma de 2 valores
def Suma(valor1, valor2):
	return valor1 + valor2

#funcion de tipo RETORNO que regresa un string con un saludo
def Saludo(nombre):
	return "Hola "+ nombre

#funcion de tipo PROCESO que imprime si un valor es mayor a 0
def ValidarNumero(valor):
	if valor>0:
		print("El valor "+str(valor)+" es mayor a 0")
	else:
		print("El valor "+str(valor)+" es menor a 0")


#Para implemetar las funciones solo basta con llamarlas

resultadoSuma_ = Suma(5,3)#nos regresara el valor de la suma
print(resultadoSuma_)

resultadoSaludo_ = Saludo("Luisa")
print(resultadoSaludo_)#nos regresa un string con un saludo

ValidarNumero(-1)#la funcion va a imprimir si el numero es mayor o menor a 0

