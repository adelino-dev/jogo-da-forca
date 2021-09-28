from forca import Forca
from jogador import Jogador
from inspetor import Inspetor
from menuJogadores import MenuJogadores
from menuTema import MenuTema


class Partida(object):
	def __init__(self):
		self._jogadores = []
		self._forca = Forca()
		self._tema = ""
		self._palavra = ""


		self._menuJogadores = MenuJogadores()
		self._menuTema = MenuTema()
		self._inspetor = Inspetor()

		self.modo = "solo" #solo ou multiplayer

	def iniciar(self):
		self._definirJogadores()
		self._definirTema()
		self._definirPalavra()

		self._inspetor.setPalavraSecreta(palavra)
		self._jogarSolor()

	def _jogarSolo(self):
		jogador = self._jogadores[0]
		placar = jogador.getPlacar()

		numDeletras = len(self._palavra)

		sentence1 = placar.getErros() < 6
		sentence2 = placar.getAcertos() < numDeletras

		while sentence1 and sentence2:
			self.forca.printForca()
			print("Tema:", self._tema)

			self._inspetor.printAcertos()
			self._inspetor.printLetrasDigitadas()

			jogador.printPlacar()
			letra = input("\nDigite uma letra:")

			self._inspetor.giveLetra(letra)

			if letra in self._palavra:
				jogador.addAcerto()

			else:
				jogador.addErro()

			self._inspetor.printAcertos()
			self._inspetor.printLetrasDigitadas()
			
			sentence1 = placar.getErros() < 6
			sentence2 = placar.getAcertos() < numDeletras
			
			if sentence1 == False:
				forca.printForca()
				print("A palavra era:", self._palavra)
				print("Game Over!")

			if sentence2 == False:
				print("Palavra:", self._palavra)
				print("Parabéns! Você ganhou!\n")

			print("\n###########################")

	def _jogarMultiplyer(self):
		sentence1 = self._forca.getEstadoAtual() < 6
		sentence2 = True #<-To change


		while sentence1 and sentence2:
			self._forca.printForca()

			for jogador in self._jogadores:
				print(jogador.getNome())

		#Incomplete

 
	def _definirJogadores(self):
		self._menuJogadores.pedirEscolha()
		self._menuJogadores.criarJogadores()

		self._jogadores = self._menuJogadores.getJogadores()
 

	def _definirTema(self):
		self._menuTema = MenuTema()
		self._menuTema.pedirEscolha()
		self._menuTema.definirTema()
		self._tema = self._menuTema.getTema()

	def _definirPalavra(self):
		self._menuTema.definirPalavra()
		self._palavra = menuPalavra.getPalavra()

	def _inspecionar(self):
		pass
