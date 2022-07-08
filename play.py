from forca import printForca
from sorteador import sortearPalavra, sortearTema
from menu import *

  
def start(tema, palavraSecreta):
  """
  tema --> string contendo o tema da rodada.
  palavraSecreta --> string contendo a palavra secreta da rodada.
  ----------------------
  
  Dados um tema e uma palavra secreta, inicia o jogo.
  """
  
  clear() #Limpa a tela para iniciar o jogo
  
  #PLACAR DO JOGO
  acertos = 0
  erros = 0
  letrasDigitadas = []
  letrasDescobertas = ["_"]*len(palavraSecreta)

  setPlacar(acertos, erros, letrasDigitadas, letrasDescobertas)
  
  #COMEÇANDO A RODADA:
  maximoAcertos = len(palavraSecreta) #Quantidade máxima de letras que é possível acertar
  
  while (erros < 6):
    printHeader(tema)
    printForca(erros)
    printPlacar()
    
    letraDigitada = pedirLetra(letrasDigitadas)
    
    if letraDigitada in palavraSecreta:
      #SUBSTITUINDO OS TRACINHOS PELA LETRA DESCOBERTA: 
      updateAcertadas(letraDigitada, letrasDescobertas, palavraSecreta)
      acertos += palavraSecreta.count(letraDigitada)
      if acertos == maximoAcertos:
        setPlacar(acertos, erros, letrasDigitadas, letrasDescobertas)
        clear()
        break

    else:
      erros += 1
      
    #Atualizando os valores do placar:  
    setPlacar(acertos, erros, letrasDigitadas, letrasDescobertas)
    clear()

  #IMPRESSÕES DO FINAL DO JOGO:
  printHeader(tema)
  printForca(erros)
  printPlacar()
  printResultado(palavraSecreta, acertos, erros)
  print()
  print("---------------FIM DE JOGO---------------")