from words.words import words, convertWord
from play import start
from raffle import *

#Condition to play:
_play = True

while _play:
  #DRAWING THE THEME:
  themeList = list(words.keys()) #takes the keys from the dictionary 'words' and adds them to a list
  theme = drawTheme(themeList)

  #DRAWING THE SECRET WORD
  wordList = words[theme]
  secretWord = drawWord(wordList)
  
  #REMOVING WORD ACCENTS AND HYPHENS:
  secretWord = convertWord(secretWord)

  #STARTING THE GAME:
  start(theme, secretWord)

  #DECIDING WHETHER TO CONTINUE OR NOT:
  _continue = input("Quer continuar jogando? (S/N):").upper()
  _play = True if _continue == 'S' else False