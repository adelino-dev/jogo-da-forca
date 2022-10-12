import os
from score import printScore, setScore
from words.words import convertWord

def askLetter(typedLetters):
  """
  typedLetters --> a list containing
  letters that have already been typed
  --------------------------
  Asks the user to type a letter,
  add that letter to the list,
  put the list in alphabetical order and
  returns the new letter typed.
  """

  entry = input("Digite uma letra:").upper()
  typedLetter = validateLetter(entry, typedLetters)

  #Adding the entry to the list:
  typedLetters.append(typedLetter)

  #Sorting the list:
  typedLetters.sort()

  #Returning the typed letter:
  return typedLetter


def validateLetter(entry, typedLetters):
  """
  entry --> a string for parsing
  typedLetters --> a list containing the letters already typed.
  --------------------------
  
  Analyzes whether the input is valid, with the requirement
  that the input is only one letter and that this letter has not been typed before.
  
  For this, it analyzes if the input really is just ONE letter and not a word. 
  It also analyzes whether this entry contains other characters such as numbers 
  and/or punctuation. Also, it checks whether this entry is already in the list 
  of typed letters or not.
  
  If it doesn't meet the requirements, 
  it asks the user to type it again until the input matches the requirements.

  At the end, it returns the already validated input.
  """
  
  entry = convertWord(entry) #Remove accents from the word
  
  #VALIDING ENTRY:
  test1 = not entry.isalpha() #Analyzes if the input is not a letter
  test2 = len(entry) > 1  #Analyzes if more than one letter was typed
  test3 = entry in typedLetters #Analyzes if the letter had already been entered before
  
  while test1 or test2 or test3:
    
    if test1:
      print("   Ops! Digite apenas uma LETRA!")
    
    elif test2:
      print("   Ops! Você você digitou algo amais que uma letra...")
  
    elif test3:
      print("   Ops! Você já digitou essa letra...")
    
    entry = input("   Digite uma letra novamente:").upper()
    print()
    
    entry = convertWord(entry)#Remove accents from the word
    
    test1 = not entry.isalpha() #Analyzes if the input is not a letter
    test2 = len(entry) > 1  #Analyzes if more than one letter was typed
    test3 = entry in typedLetters #checks if the letter had already been entered before
  
  return entry

def printHeader(theme):
  """
  theme --> round theme.
  
  ----------------------
  Print the game header.
  """
  print()
  print("********** JOGO DA FORCA **********")
  print()
  print("TEMA:", theme)

def printResult(secretWord, hits, erros):
  """
  secretWord --> a string with the secret word of the round;
  hits --> number of hits (int)
  errors -> number of wrong letters (int)
  ----------------------------------
  Analyzes whether the player has already won or lost.
  If yes, prints the final result of the game on the screen.
  """
  
  if hits == len(secretWord):
    print("PARABÉNS VOCÊ GANHOU!!")
    
  if erros == 6:
    print("GAME OVER! VOCÊ PERDEU O JOGO.")
    print("A palavra era:", secretWord)


def updateHits(typedLetter, discoveredLetters, secretWord):
  """
  string containing a letter
  discoveredLetters --> list of discovered letters
  secretWord --> string containing the secret word
  
  ________________________________
  Swap the proper dashes from the list of discovered letters for the
  typed letter, if the letter is in the secret word.
  """

  if typedLetter in secretWord:
    i = 0 #index
    for letter in secretWord:
      if letter == typedLetter:
        discoveredLetters[i] = typedLetter
      i += 1

#Creating function to clear the screen:
def clear():
  """
  Clear the screen.
  """
  
  if os.name == "nt": #if the Operational System is Windows
      os.system("cls") 
    
  else:
      os.system("clear")