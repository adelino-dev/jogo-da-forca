import Placar

class Jogador(object):
	def __init__(self, nome):
		self._nome = nome
		self.placarAtual = Placar()
		self.vitorias = 0
		self.derrotas = 0

	def getVitorias(self):
		return self.vitorias

	def atualizarPlacar(self):
		pass

	def printPlacar():
		pass