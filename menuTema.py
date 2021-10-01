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

		self._opcoes = palavras.index_temas

		self._indexModoAleatorio = 0
		self._opcoes[self._indexModoAleatorio] = "Escolher Aleatoriamente"

	def getPalavra(self):
		return self._palavra

	def getTema(self):
		return self._tema

	def _escolherTemaAleatoriamente(self):
		self._tema = random.choice(MenuTema.temas)

	def definirTema(self):
		indexEscolhido = self.getEscolha()

		if indexEscolhido == self._indexModoAleatorio:
			self._escolherTemaAleatoriamente()

		else:
			self._tema = self._opcoes[self._escolha]
			
	def definirPalavra(self):
		palavras = MenuTema.temas_palavras[self._tema]
		self._palavra = random.choice(palavras)