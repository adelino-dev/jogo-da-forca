from hangman import printHangman
from raffle import drawWord, drawTheme
from menu import *

  
def start(theme, secretWord):
  """
   theme --> string containing the theme of the round.
   secretWord --> string containing the secret word of the round.
   ----------------------
  
   Given a theme and a secret word, the game starts.
  """
  
  clear() #Clear the screen to start the game
  
  #GAME SCORE:
  hits = 0
  erros = 0
  typedLetters = []
  discoveredLetters = ["_"]*len(secretWord)

  setScore(hits, erros, typedLetters, discoveredLetters)
  
  #STARTING THE ROUND:
  maxHits= len(secretWord) #Maximum number of letters that it is possible to hit
  
  while (erros < 6):
    printHeader(theme)
    printHangman(erros)
    printScore()
    
    typedLetter = askLetter(typedLetters)
    
    if typedLetter in secretWord:
      #REPLACING THE DASHES FOR THE LETTER DISCOVERED: 
      updateHits(typedLetter, discoveredLetters, secretWord)
      hits += secretWord.count(typedLetter)
      if hits == maxHits:
        setScore(hits, erros, typedLetters, discoveredLetters)
        clear()
        break

    else:
      erros += 1
      
    #Updating the scoreboard values:
    setScore(hits, erros, typedLetters, discoveredLetters)
    clear()

  #FINAL GAME IMPRESSIONS:
  printHeader(theme)
  printHangman(erros)
  printScore()
  printResult(secretWord, hits, erros)
  print()
  print("---------------FIM DE JOGO---------------")