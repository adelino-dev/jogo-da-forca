from menu import Menu
import palavras
import random

class MenuTema(Menu):
	temas = palavras.temas #<-- Analisar
	temas_palavras = palavras.temas_palavras #< -- Analisar
	numeroDeTemas = len(temas) #<-- Analisar
	
	def __init__(self):
		self._palavra = ""
		self._tema = ""

		self.opcoes = palavras.index_temas

		self.indexModoAleatorio = 0
		self.opcoes[self.indexModoAleatorio] = "Escolher Aleatoriamente"

	def getPalavra(self):
		return self._palavra

	def getTema(self):
		return self.tema

	def _escolherTemaAleatoriamente(self):
		self._tema = random.choice(Menu._temas)

	def definirTema(self):
		indexEscolhido = self.getEscolha()

		if indexEscolhido == self.indexModoAleatório:
			self._escolherAleatoriamente()

		else:
			self._tema = self.opcoes[self.escolha]
			
	def definirPalavra(self):
		self._palavra = Menu.temas_palavras[self._tema]