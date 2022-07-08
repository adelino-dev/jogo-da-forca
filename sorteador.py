import random

def sortearPalavra(palavras):
  """
  palavras --> uma lista contendo palavras;
  ---------------
  Dada uma lista de palavras, sorteia e retorna uma palavra da lista.
  """
  palavra = random.choice(palavras)
  return palavra

def sortearTema(temas):
  """
  temas --> uma lista contendo temas;
  ---------------
  Dada uma lista de temas, sorteia e retorna um tema da lista.
  """
  tema = random.choice(temas)
  return tema