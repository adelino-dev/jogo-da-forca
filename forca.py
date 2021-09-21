import estados_da_forca as ef

class Forca(object):
	_estado0 = ef.estado0
	_estado1 = ef.estado1
	_estado2 = ef.estado2
	_estado3 = ef.estado3
	_estado4 = ef.estado4
	_estado5 = ef.estado5
	_estado6 = ef.estado6
	_estados = {0:_estado0, 1:_estado1, 2:_estado2, 3:_estado3, 4:_estado4, 5:_estado5, 6:_estado6}

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
		for linha in Forca._estados[self._estadoAtual]:
			print(linha)

		print("--------------")