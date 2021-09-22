import palavras
import random

class Menu(object):
	temas = palavras.temas
	index_temas = palavras.index_temas
	temas_palavras = palavras.temas_palavras
	numeroDeTemas = len(temas)


	def __init__(self):
		self._tema = ""
		self._palavra = ""

		self._printMenuTemas()
		self._escolherTema()
		self._escolherPalavra()

	def _printMenuTemas(self):
		print("--------------")
		print("Temas:")

		for index in Menu.index_temas:
			tema = Menu.index_temas[index]
			print('%i- %s' % (index, tema))

		print("ou %i para Modo Aleatório." % (Menu.numeroDeTemas+1), end = "\n\n")

	def printTema(self):
		print("Tema:", self._tema)

	def _escolherTema(self):
		numEscolhido = int(input("Escolha um número:"))

		if numEscolhido == Menu.numeroDeTemas+1:
			numeroAleatorio = random.randint(0, Menu.numeroDeTemas)
			self._tema = random.choice(Menu.temas)
		
		else:
			self._tema = Menu.index_temas[numEscolhido]

	def _escolherPalavra(self):
		palavras = Menu.temas_palavras[self._tema]
		self._palavra = random.choice(palavras)

	def getTema(self):
		return self._tema

	def getPalavra(self):
		return self._palavra