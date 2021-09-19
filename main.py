from forca import Forca
from placar import Placar
from inspetor import Inspetor
from menu import Menu

continuar = True
while continuar:
	menu = Menu()
	palavra = menu.getPalavra()

	forca = Forca()
	forca.printForca()

	