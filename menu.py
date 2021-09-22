class Menu(object):
	def __init__(self):
		self.opcoes = {}#num:opção
		self.escolha = 0

	def printOpcoes():
		print("--------------")
		print("Escolha:")
		for num in self.opcoes:
			opcao = self.opcoes[num]
			print(num, '-', opcao)
		("--------------")

	def pedirEscolha():
		escolha = int(input("Digite um número:"))

	def getEscolha():
		return self.escolha