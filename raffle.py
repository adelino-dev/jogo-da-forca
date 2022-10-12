import random

def drawWord(words):
  """
  words --> a list containing words;
  ---------------
  Given a list of words, it draws and returns a word from the list.
  """
  word = random.choice(words)
  return word

def drawTheme(themes):
  """
  themes --> a list of themes;
  ---------------
  Given a list of themes, it draws and returns a theme from the list.
  """
  theme = random.choice(themes)
  return theme