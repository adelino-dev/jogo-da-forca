from menu import Menu
from jogador import Jogador

class MenuJogadores(Menu):
	def __init__(self):
		self._jogadores = {}

	def pedirEscolha(self):
		self.escolha = int(input("Digite o número de jogadores:"))

	def criarJogadores(self):
		for num in range(self.escolha):
			n = num+1
			nome = input("Nome do jogador %i:" % n)
			self._jogadores[num] = Jogador(nome)

	def getJogadores(self):
		return self._jogadores

	def getJogador(self, num):
		jogador = self._jogadores[num]
		return jogador