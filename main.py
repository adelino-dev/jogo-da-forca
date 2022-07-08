from palavras.palavras import palavras, convertPalavra
from play import start
from sorteador import *

#CONDIÇÃO PARA CONTINUAR JOGANDO
querJogar = True

while querJogar:
  #SORTEANDO O TEMA
  listaTemas = list(palavras.keys()) #pega as chaves do dicionário palavras e adiciona elas numa lista
  tema = sortearTema(listaTemas)

  #SORTEANDO A PALAVRA SECRETA
  listaPalavras = palavras[tema]
  palavraSecreta = sortearPalavra(listaPalavras)
  
  #REMOVENDO ACENTOS E HÍFENS DA PALAVRA:
  palavraSecreta = convertPalavra(palavraSecreta)

  #COMEÇANDO O JOGO:
  start(tema, palavraSecreta)

  #DECIDINDO SE CONTINUA OU NÃO
  continuar = input("Quer continuar jogando? (S/N):").upper()
  querJogar = True if continuar == 'S' else False