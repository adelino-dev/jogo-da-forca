class Validator(object):

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

    def convertWord(self, word):
        """
        word --> string containing a word

        ________________
        Returns the word without 'accents', without 
        hyphens and in UPPERCASE.
        It also strips spaces and line wraps, if any.
        """
        
        word = word.upper()
        word = word.replace("\n", "")
        
        for letter in word:
            if letter in Validator.specialLetters:
                noAccent = Validator.specialLetters[letter] #take the letter without accent
                word = word.replace(letter, noAccent)

        return word

    def validateLetter(self, entry, typedLetters):
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
        
        entry = self.convertWord(entry) #Remove accents from the word
        
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
            
            entry = self.convertWord(entry)#Remove accents from the word
            
            test1 = not entry.isalpha() #Analyzes if the input is not a letter
            test2 = len(entry) > 1  #Analyzes if more than one letter was typed
            test3 = entry in typedLetters #checks if the letter had already been entered before
        
        return entry