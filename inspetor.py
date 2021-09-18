class Inspetor(object):
	def __init__(self, palavra):
		self.__palavraSecreta = palavra
		self.__letrasDigitadas = []
		self.__letrasCertas = []
		self.__letrasErradas = []


	def giveLetra(self, letra):
		self.__letrasDigitadas.append(letra)
		
		if letra in self.__palavraSecreta:
			self.__letrasCertas.append(letra)
			self.__letrasCertas.sort()

			self.__acertos += 1

		else:
			self.__letrasErradas.append(letra)
			self.__letrasErradas.sort()

			self.__erros += 1

	def printLetrasDigitadas(self):
		print("Letras Digitadas:", end = " ")
		for letra in self.__letrasDigitadas:
			if letra != self.__letrasDigitadas[-1]:
				print(letra + ",", end = " ")
			else:
				print(letra+".")

	def printAcertos(self):
		for letra in self.__palavraSecreta:
			if letra in self.__letrasCertas:
				print(letra, end = "")
			else:
				print("-", end = "")

	def getLetrasDigitadas(self):
		return self.__letrasDigitadas

	def getLetrasCertas(self):
		return self.__letrasCertas

	def getLetrasErradas(self):
		return self.__letrasErradas

