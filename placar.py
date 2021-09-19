class Placar(object):
	def __init__(self):
		self._acertos = 0
		self._erros = 0

	def getAcertos(self):
		return self._acertos

	def getErros(self):
		return self._erros

	def setAcertos(self, numero):
		self._acertos = numero

	def setErros(self):
		self._erros = numero
