class Inspetor(object):
	def __init__(self, palavra):
		self._palavraSecreta = palavra
		self._letrasDigitadas = []
		self._letrasCertas = []
		self._letrasErradas = []

	def giveLetra(self, letra):
		self._letrasDigitadas.append(letra)
		
		if letra in self._palavraSecreta:
			self._letrasCertas.append(letra)
			self._letrasCertas.sort()

		else:
			self._letrasErradas.append(letra)
			self._letrasErradas.sort()
			
	def printLetrasDigitadas(self):
		print("Letras Digitadas: [", end = " ")
		for letra in self._letrasDigitadas:
			if letra != self._letrasDigitadas[-1]:
				print(letra + ",", end = " ")
			else:
				print(letra, end = "")
		print("]")

	def printAcertos(self):
		print("\nPalavra Secreta:", end = " ")
		for letra in self._palavraSecreta:
			if letra in self._letrasCertas:
				print(letra, end = "")
			else:
				print("-", end = "")
		print()

	def getLetrasDigitadas(self):
		return self._letrasDigitadas

	def getLetrasCertas(self):
		return self._letrasCertas

	def getLetrasErradas(self):
		return self._letrasErradas