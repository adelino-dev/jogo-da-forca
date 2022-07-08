import os
from placar import printPlacar, setPlacar
from palavras.palavras import convertPalavra

def pedirLetra(letrasDigitadas):
  """
  letrasDigitadas --> uma lista contendo
  as letras que já foram digitadas
  --------------------------
  Pede para o usuário digitar uma letra,
  adiciona essa letra na lista, 
  põe a lista em ordem alfabética e
  retorna a nova letra digitada.
  """

  letraDigitada = input("Digite uma letra:").upper()
  letraDigitada = validarLetra(letraDigitada, letrasDigitadas)

  #Adicionando entrada na lista:
  letrasDigitadas.append(letraDigitada)

  #Ordenando a lista:
  letrasDigitadas.sort()

  #Retornando a letra digitada:
  return letraDigitada


def validarLetra(entrada, letrasDigitadas):
  """
  entrada --> uma string para análise
  letrasDigitadas --> uma lista contendo as letras já digitadas.
  --------------------------
  
  Analisa se a entrada é válida, tendo como exigência que a entrada seja apenas uma
  letra e que essa letra não tenha sido digitada antes.
  
  Para isso, analisa se a entrada realmente é apenas UMA letra e não uma palavra.
  Também analisa se nessa entra há outros caracteres como números e/ou pontuações.
  Ademais, verifica se essa entrada já está na lista de letras digitadas ou não.
  
  Caso não cumpra às exigências, pede para o usuário digitar novamente 
  até que a entrada corresponda às exigências.

  No final, retorna a entrada já validada.
  """
  
  entrada = convertPalavra(entrada)#Tira os acentos da palavra
  
  #VALIDANDO ENTRADA:
  teste1 = not entrada.isalpha() #Analisa se a entrada não é uma letra
  teste2 = len(entrada) > 1  #Analisa se foi digitada mais que uma letra
  teste3 = entrada in letrasDigitadas #Analisa se a letra já tinha sido inserida antes
  
  while teste1 or teste2 or teste3:
    
    if teste1:
      print("   Ops! Digite apenas uma LETRA!")
    
    elif teste2:
      print("   Ops! Você você digitou algo amais que uma letra...")
  
    elif teste3:
      print("   Ops! Você já digitou essa letra...")
    
    entrada = input("   Digite uma letra novamente:").upper()
    print()
    
    entrada = convertPalavra(entrada)#Tira os acentos da palavra
    
    teste1 = not entrada.isalpha() #Analisa se a entrada não é uma letra
    teste2 = len(entrada) > 1  #Analisa se foi digitada mais que uma letra
    teste3 = entrada in letrasDigitadas #Analisa se a letra já tinha sido inserida antes
  
  return entrada

def printHeader(tema):
  """
  tema --> tema da rodada.
  
  ----------------------
  Imprime o cabeçalho do jogo.
  """
  print()
  print("********** JOGO DA FORCA **********")
  print()
  print("TEMA:", tema)

def printResultado(palavraSecreta, acertos, erros):
  """
  palavraSecreta --> uma sintrg com a palavra secreta da rodada;
  acertos --> quantidade de letras acertadas (int)
  erros -> quantidade de letras erradas (int)
  ----------------------------------
  Analisa se o jogador já ganhou ou perdeu.
  Se sim, imprime na tela o resultado final do jogo.
  """
  
  if acertos == len(palavraSecreta):
    print("PARABÉNS VOCÊ GANHOU!!")
    
  if erros == 6:
    print("GAME OVER! VOCÊ PERDEU O JOGO.")
    print("A palavra era:", palavraSecreta)


def updateAcertadas(letraDigitada, letrasDescobertas, palavraSecreta):
  """
  letraDigitada --> string contendo uma letra
  letrasDescobertas --> lista de letras descobertas
  palavraSecreta --> string contendo a palavra secreta
  
  ________________________________
  Troca os devidos tracinhos da lista de letras descobertas pela 
  letra digitada, se a letra estiver na palavra secreta.
  """
  if letraDigitada in palavraSecreta:
    i = 0 #índice (posição da letra)
    for letra in palavraSecreta:
      if letra == letraDigitada:
        letrasDescobertas[i] = letraDigitada
      i += 1

#Criando função para limpar a tela:
def clear():
  """
  Limpa a tela.
  """
  
  if os.name == "nt": #Se for Windows
      os.system("cls") 
    
  else:
      os.system("clear") 