
#LISTAS DE PALAVRAS POR TEMA
animais = open("palavras/animais.txt", "r", encoding="utf8").readlines()
frutas = open("palavras/frutas.txt", "r", encoding="utf8").readlines()
objetos = open("palavras/objetos.txt", "r", encoding="utf8").readlines()
paises = open("palavras/paises.txt", "r", encoding="utf8").readlines()

#TEMAS COM PALAVRAS SECRETAS
palavras = {
        'ANIMAL':animais,
        'FRUTA':frutas,
        'OBJETO': objetos,
        'PAÍS': paises
}

# CONVERTE PALAVRA PARA O PADRÃO SEM ACENTO:
letrasEspeciais = {
    "Á":"A", "À":"A", "Ã":"A", "Â":"A",
    "É":"E", "È":"E", "Ê":"E",
    "Í":"I", "Ì":"I", "Î":"I",
    "Ó":"O", "Õ":"O", "Ò":"O",
    "Ú":"U", "Ù":"U", "Û":"U",
    "Ç":"C",
    "-":"",
    " ":"",
  }

def convertPalavra(palavra):
  """
  palavra --> string contendo uma palavra

  ________________
  Retorna a palavra sem 'acentos', sem hifens e em CAIXA ALTA.
  Também tira espaços e quebra de linha da palavra, se houver.
  """
  palavra = palavra.replace("\n", "")
  palavra = palavra.upper()
  
  for letra in palavra:
    if letra in letrasEspeciais:
      semAcento = letrasEspeciais[letra] #pega a letra sem acento
      palavra = palavra.replace(letra, semAcento)

  return palavra