class Placar(object):
	def __init__(self):
		self.__acertos = 0
		self.__erros = 0

	def getAcertos(self):
		return self.__acertos

	def getErros(self):
		return self.__erros

	def setAcertos(self, numero):
		self.__acertos = numero

	def setErros(self):
		self._erros = numero
