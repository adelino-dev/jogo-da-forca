"""
A forca possui 7 estados que vão desde o estado 0 (forca sem o corpo), 
até o estado 6 (totalmente enforcado).
"""

#Estados da Forca:
estado0 = [
"╔════════╗",
"║        ¥",
"║", 
"║", 
"║", 
"║"
]

estado1 = [
"╔════════╗",
"║        ¥",
"║        O", 
"║", 
"║", 
"║"
]

estado2 = [
"╔════════╗",
"║        ¥",
"║        O",
"║        |",
"║", 
"║"
]

estado3 = [
"╔════════╗",
"║        ¥",
"║        O",
"║       /|",
"║",
"║"
]

estado4 = [
"╔════════╗",
"║        ¥",
"║        O",
"║       /|\ ",
"║", 
"║"
]

estado5 = [
"╔════════╗",
"║        ¥",
"║        O",
"║       /|\ ",
"║       /",
"║"
]

estado6 = [
"╔════════╗",
"║        ¥",
"║        O",
"║       /|\ ",
"║       / \ ",
"║"
]

estados = {
  0:estado0, 
  1:estado1, 
  2:estado2,
  3:estado3,
  4:estado4,
  5:estado5,
  6:estado6
}

#FUNÇÃO PARA IMPRIMIR A FORCA:
def printForca(erros):
  """
  erros --> a quantidade de erros em número inteiro (0 - 6)
  -------------

  Dado o número de erros, imprime na tela a forca em seu estado atual.
  """
  forca = estados[erros]
  for linha in forca:
    print(linha)