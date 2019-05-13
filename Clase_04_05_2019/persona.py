class Persona:
	def __init__(self,estatura, peso,tes):
		self.estatura = estatura
		self.peso = peso
		self.tes = tes
	def Pesar(self):
		print("Peso "+str(self.peso))


class Hombre(Persona):
	def __init__(self,estatura,peso, nombre):
		self.nombre = nombre
		Persona.__init__(self,estatura,peso)
	def Descripcion(self):
		print(self.nombre + " pesa "+ str(self.peso))


_hombre = Hombre(1.75,85, "Eliud ")
_hombre.Descripcion()

