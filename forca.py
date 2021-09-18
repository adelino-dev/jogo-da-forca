import estados_da_forca as ef

class Forca(object):
	estado1 = ef.estado1
	estado2 = ef.estado2
	estado3 = ef.estado3
	estado4 = ef.estado4
	estado5 = ef.estado5
	estado6 = ef.estado6
	estados = {1:estado1, 2:estado2, 3:estado3, 4:estado4, 5:estado5, 6:estado6}

	def __init__(self):
		"""
		Estados da Forca:
		estado1 --> cabeça
		estado2 --> cabeça,tronco
		estado3 --> cabeça, tronco, 1 braço
		estado4 --> cabeça, tronco, 2 braços
		estado5 --> cabeça, tronco, 2 braços, 1 perna
		estado6 --> cabeça, tronco, 2 braços, 2 pernas
		"""
		self.__estadoAtual = 1

	def getEstadoAtual(self):
		"""
		Retorna um valor inteiro entre 1 a 6.
		"""
		return self.__estadoAtual

	def setEstadoAtual(self, numero):
		"""
		Insira um valor inteiro entre 1 a 6.
		"""
		self.__estadoAtual = numero
	
	def printForca(self):
		"""
		Imprime a forca no seu estado atual
		"""
		print(estados[self.__estadoAtual])