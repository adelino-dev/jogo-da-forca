import estados_da_forca as ef

class Forca(object):
	estado0 = ef.estado0
	estado1 = ef.estado1
	estado2 = ef.estado2
	estado3 = ef.estado3
	estado4 = ef.estado4
	estado5 = ef.estado5
	estado6 = ef.estado6
	estados = {0:estado0, 1:estado1, 2:estado2, 3:estado3, 4:estado4, 5:estado5, 6:estado6}

	def __init__(self):
		"""
		Estados da Forca:
		estadi0 --> apenas a forca
		estado1 --> cabeça
		estado2 --> cabeça,tronco
		estado3 --> cabeça, tronco, 1 braço
		estado4 --> cabeça, tronco, 2 braços
		estado5 --> cabeça, tronco, 2 braços, 1 perna
		estado6 --> cabeça, tronco, 2 braços, 2 pernas
		"""
		self._estadoAtual = 0

	def getEstadoAtual(self):
		"""
		Retorna um valor inteiro entre 1 a 6.
		"""
		return self._estadoAtual

	def setEstadoAtual(self, numero):
		"""
		Insira um valor inteiro entre 1 a 6.
		"""
		self._estadoAtual = numero
	
	def printForca(self):
		"""
		Imprime a forca no seu estado atual
		"""
		print("\n--------------")
		for linha in Forca.estados[self._estadoAtual]:
			print(linha)

		print("--------------")