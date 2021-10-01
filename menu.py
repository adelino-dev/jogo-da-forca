class Menu(object):
	def __init__(self):
		self._opcoes = {}#num:opção
		self._escolha = 0

	def printOpcoes(self, fraseInicial = "Escolha:"):
		print("--------------")
		print(fraseInicial)
		for num in self._opcoes:
			opcao = self._opcoes[num]
			print(num, '-', opcao)
		("--------------")

	def pedirEscolha(self):
		self._escolha = int(input("Digite um número:"))

	def getEscolha(self):
		return self._escolha