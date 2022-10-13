import objects.moderator as moderator

class Round(object):
    
    def start(self):
        self._moderator = moderator.Moderator()
        #Clear the screen to start the game:
        self._moderator.clear()

        #STARTING THE ROUND:
        statusPlayer = self._moderator.getStatusPlayer()

        while statusPlayer == 'playing':

            self._moderator.printMenu()

            typedLetter = self._moderator.askLetter()

            #Updating the scoreboard values:
            self._moderator.updateScore(typedLetter)
            statusPlayer = self._moderator.getStatusPlayer()
            
            self._moderator.clear()

        #FINAL GAME PRINTS:
        self._moderator.printMenu()
        self._moderator.printResult()
        print()
        print("---------------FIM DE JOGO---------------")