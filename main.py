from forca import Forca
from placar import Placar
from inspetor import Inspetor
from menu import Menu

debugar = input("Debugar?") 

if debugar == 's':
	pdb.set_trace()

continuar = True
while continuar:
	menu = Menu()
	palavra = menu.getPalavra()

	forca = Forca()
	inspetor = Inspetor(palavra)
	placar = Placar()

	while placar.getErros() < 6 and placar.getAcertos() < len(palavra):
		forca.printForca()
		menu.printTema()

		inspetor.printAcertos()
		inspetor.printLetrasDigitadas()
		
		letra = input("\nDigite uma letra:")
		inspetor.giveLetra(letra)

		letrasErradas = inspetor.getLetrasErradas()
		letrasCertas = inspetor.getLetrasCertas()

		numErradas = len(letrasErradas)
		placar.setErros(numErradas)

		numCertas = 0
		for letra in letrasCertas:
			repeticoes = palavra.count(letra)
			numCertas += repeticoes
		placar.setAcertos(numCertas)

		forca.setEstadoAtual(placar.getErros())
			
		if numErradas == 6:
			forca.printForca()
			print("A palavra era:", palavra)
			print("Game Over!")

		if numCertas == len(palavra):
			print("Palavra:", palavra)
			print("Parabéns! Você ganhou!\n")

		print("\n###########################")
