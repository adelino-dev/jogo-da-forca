class Scoreboard(object):
    """
    Create a Scoreboard object that manages:
        - Number of Hits
        - Number of Erros
        - Attempted Letters
        - Discovered Letters
    """
        
    def __init__(self):

        self._hits = 0
        self._errors = 0
        self._attemptedLetters = []
        self._discoveredLetters = []
    
    def getHits(self):
        """
        Returns the number of hits.
        """
        return self._hits

    def getErrors(self):
        """
        Returns the number of errors.
        """
        return self._errors
        
    def getAttempted(self):
        """
        Returns a list of attempted letters
        """
        return self._attemptedLetters
        
    def getDiscovered(self):
        """
        Returns a list of discovered letters
        """
        return self._discoveredLetters
    
    def setScore(self, h, e, al, dl):
        """
        Parameters:

        - h --> hits (int),
        - e --> errors (int),
        - al --> attempted letters (list),
        - dl --> discovered letters (list),

        ______________

        Changes the value of scoreboard variables.
        (and automatically sort the list of attempted letters )
        """

        self._hits = h
        self._errors = e
        self._attemptedLetters = al
        self._discoveredLetters = dl

        self._attemptedLetters.sort() #Sorting the list:
    
    def printScore(self):
        """
        Prints the current scoreboard on the screen.
        """
        print("Palavra secreta:", " ".join(self._discoveredLetters))
        print("Letras tentadas:", self._attemptedLetters)
        print("Acertos:", self._hits)
        print("Erros:", self._errors)
        print()
    
