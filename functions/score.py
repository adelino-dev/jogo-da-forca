hits = 0
erros = 0
attemptedLetters = []
discoveredLetters = []

def printScore():
  """
  Prints the current score on the screen.
  """
  print("Palavra secreta:", discoveredLetters)
  print("Letras tentadas:", attemptedLetters)
  print("Acertos:", hits)
  print("Erros:", erros)
  print()


def setScore(h, e, al, dl):
  """
  h --> hits (int),
  e --> erros (int),
  al --> attempted letters (list),
  dl --> discovered letters (list),

  ______________
  Changes the value of scoreboard variables.
  """
  global hits, erros, attemptedLetters, discoveredLetters
  hits = h
  erros = e
  attemptedLetters = al
  discoveredLetters = " ".join(dl) #convert to string