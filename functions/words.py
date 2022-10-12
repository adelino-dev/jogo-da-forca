#WORD LISTS BY THEME:
animals = open("./words/animals.txt", "r", encoding="utf8").readlines()
fruits = open("./words/fruits.txt", "r", encoding="utf8").readlines()
objects = open("./words/objects.txt", "r", encoding="utf8").readlines()
countries = open("./words/countries.txt", "r", encoding="utf8").readlines()

#THEMES WITH SECRET WORDS:
words = {
        'ANIMAL': animals,
        'FRUTA': fruits,
        'OBJETO': objects,
        'PAÍS': countries
}

#CONVERT WORD TO PATTERN WITHOUT ACCENT:

specialLetters = {
    "Á":"A", "À":"A", "Ã":"A", "Â":"A",
    "É":"E", "È":"E", "Ê":"E",
    "Í":"I", "Ì":"I", "Î":"I",
    "Ó":"O", "Õ":"O", "Ò":"O",
    "Ú":"U", "Ù":"U", "Û":"U",
    "Ç":"C",
    "-":"",
    " ":"",
  }

def convertWord(word):
  """
  word --> string containing a word

   ________________
   Returns the word without 'accents', without 
   hyphens and in UPPERCASE.
   It also strips spaces and line wraps, if any.
  """
  word = word.replace("\n", "")
  word = word.upper()
  
  for letter in word:
    if letter in specialLetters:
      noAccent = specialLetters[letter] #take the letter without accent
      word = word.replace(letter, noAccent)

  return word