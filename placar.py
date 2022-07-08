acertos = 0
erros = 0
letrasTentadas = []
letrasDescobertas = []

def printPlacar():
  """
  Imprime na tela o placar atual.
  """
  print("Palavra secreta:", letrasDescobertas)
  print("Letras tentadas:", letrasTentadas)
  print("Acertos:", acertos)
  print("Erros:", erros)
  print()


def setPlacar(a, e, lt, ld):
  """
  a --> acertos (int),
  e --> erros (int),
  lt --> letras tentadas (list),
  ld --> letras descobertas (list),

  ______________
  Altera o valor das variáveis do placar.
  """
  global acertos, erros, letrasTentadas, letrasDescobertas
  acertos = a
  erros = e
  letrasTentadas = lt
  letrasDescobertas = " ".join(ld) #transforma em string