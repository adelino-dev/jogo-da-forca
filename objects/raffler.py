import random
from objects.validator import Validator

#WORD LISTS BY THEME:
animals = open("./words/animals.txt", "r", encoding="utf8").readlines()
fruits = open("./words/fruits.txt", "r", encoding="utf8").readlines()
objects = open("./words/objects.txt", "r", encoding="utf8").readlines()
countries = open("./words/countries.txt", "r", encoding="utf8").readlines()



class Raffler(object):
    """
    Creates a Raffler object that 
    draws a secreat theme and a secret word.
    """
    
    #THEMES WITH SECRET WORDS:
    themes = {
        'ANIMAL': animals,
        'FRUTA': fruits,
        'OBJETO': objects,
        'PAÍS': countries
    }
    
    validator = Validator()

    def __init__(self):
        self.drawTheme()
        self.drawWord()

    def drawTheme(self):
        """
        Draws a theme from the themes list.
        """
        themes = list(Raffler.themes.keys())
        self._theme = random.choice(themes)
    
    def drawWord(self):
        """
        Draws a word from the secret words list.
        """
        words = Raffler.themes[self._theme]
        self._word = random.choice(words)
        self._word = Raffler.validator.convertWord(self._word)

    def getTheme(self):
        """
        Returns the current theme drawn.
        """
        return self._theme

    def getWord(self):
        """
        Returns the current word drawn.
        """
        return self._word