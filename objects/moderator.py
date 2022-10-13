from objects.raffler import *
import objects.hangman as hangman
import objects.scoreboard as scoreboard
import os


class Moderator(Raffler):

    def __init__(self):
        Raffler.__init__(self)

        #SETTING OBJECTS:
        self._hangman = hangman.Hangman()
        self._scoreboard = scoreboard.Scoreboard()
        
        discoveredLetters = ["_"]*len(self._word)
        self._scoreboard.setScore(0, 0, [], discoveredLetters)
    
    def askLetter(self):
        """
        Asks the user to type a letter
        and returns the new letter typed.
        """
        entry = input("Digite uma letra:").upper()

        attemptedLetters  = self._scoreboard.getAttempted()

        #Validating letter:
        validator = Raffler.validator
        entry = validator.validateLetter(entry, attemptedLetters)
        #Returning the typed letter:
        return entry
        
    def printHeader(self):
        """
        Prints the game header.
        """
        print()
        print("********** JOGO DA FORCA **********")
        print()
        print("TEMA:", self.getTheme())
    
    def printMenu(self):
        """
        Prints the header, the hangman in its current
        and the scoreboard on the screen.
        """
        self.printHeader()
        self._hangman.printHangman()
        self._scoreboard.printScore()
    
    def printResult(self):
        """
        Analyzes whether the player has already won or lost.
        If yes, prints the final result of the game on the screen.
        """
        secretWord = self.getWord()
        status = self.getStatusPlayer()

        if status == 'winner':
            print("PARABÉNS VOCÊ GANHOU!!")
            
        elif status == 'looser':
            print("GAME OVER! VOCÊ PERDEU O JOGO.")
            print("A palavra era:", secretWord)


    def getStatusPlayer(self):
        secretWord = self.getWord()
        hits = self._scoreboard.getHits()
        errors = self._scoreboard.getErrors()

        if errors == 6:
            return 'looser'

        elif hits == len(secretWord):
            return "winner"
        
        else:
            return "playing"
        

    
    def updateScore(self, typedLetter):
        """
        typedLetter --> string containing a letter

        ________________________________

        Swap the proper dashes from the list of discovered letters for the
        typed letter, if the letter is in the secret word.
        """
        secretWord = self.getWord()
        hits = self._scoreboard.getHits()
        errors = self._scoreboard.getErrors()
        attemptedLetters = self._scoreboard.getAttempted()
        discoveredLetters = self._scoreboard.getDiscovered()

        attemptedLetters.append(typedLetter)
        
        if typedLetter in secretWord:
            i = 0 #index
            for letter in secretWord:
                if letter == typedLetter:
                    hits += 1
                    discoveredLetters[i] = letter
                i += 1
        else:
            errors += 1
            self._hangman.setState(errors)

        self._scoreboard.setScore(hits, errors, attemptedLetters, discoveredLetters)



    def clear(self):
        """
        Clear the screen.
        """
        
        if os.name == "nt": #if the Operational System is Windows
            os.system("cls") 
            
        else:
            os.system("clear")