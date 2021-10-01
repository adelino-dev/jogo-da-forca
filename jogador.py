from placar import Placar

class Jogador(object):
	def __init__(self, nome):
		self._nome = nome
		self._placarAtual = Placar()
		self._vitorias = 0
		self._derrotas = 0

	def getVitorias(self):
		return self._vitorias
	def getDerrotas(self):
		return self._derrotas
	def getPlacarAtual(self):
		return self._placarAtual

	def getNome(self):
		return self._nome

	def addAcerto(self):
		self._placarAtual.addAcerto()

	def addErro(self):
		self._placarAtual.addErro()

	def printPlacar(self):
		pass