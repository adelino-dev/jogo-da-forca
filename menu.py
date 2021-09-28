class Menu(object):
	def __init__(self):
		self.opcoes = {}#num:opção
		self.escolha = 0

	def printOpcoes(self):
		print("--------------")
		print("Escolha:")
		for num in self.opcoes:
			opcao = self.opcoes[num]
			print(num, '-', opcao)
		("--------------")

	def pedirEscolha(self):
		self.escolha = int(input("Digite um número:"))

	def getEscolha(self):
		return self.escolha