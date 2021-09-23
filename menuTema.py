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

	def getPalavra(self):
		return self._palavra

	def getTema(self):
		return self.tema

	def escolherAleatoriamente:
		random.choice
