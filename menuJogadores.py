from menu import Menu
from jogador import Jogador

class MenuJogadores(Menu):
	def __init__(self):
		self._jogadores = []

	def pedirEscolha:
		self.escolha = int(input("Digite o número de jogadores:"))

	def criarJogadores(self):
		for num in range(self.escolha+1):
			nome = input("Nome do jogador %i:"% num)
			self._jogadores[num] = Jogador(nome)

	def getJogadores(self):
		return self._jogadores

	def getJogador(self, num):
		jogador = self._jogadores[num]
		return jogador