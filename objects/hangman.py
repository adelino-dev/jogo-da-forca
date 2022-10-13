class Hangman(object):
    """
    Creates a Hangman object that can to be 7 states 
    ranging from state 0 (nothing hanged) 
    up to state 6 (fully hanged).
    """

    #Hangman states:

    state0 = [
    "╔════════╗",
    "║        ¥",
    "║", 
    "║", 
    "║", 
    "║"
    ]

    state1 = [
    "╔════════╗",
    "║        ¥",
    "║        O", 
    "║", 
    "║", 
    "║"
    ]

    state2 = [
    "╔════════╗",
    "║        ¥",
    "║        O",
    "║        |",
    "║", 
    "║"
    ]

    state3 = [
    "╔════════╗",
    "║        ¥",
    "║        O",
    "║       /|",
    "║",
    "║"
    ]

    state4 = [
    "╔════════╗",
    "║        ¥",
    "║        O",
    "║       /|\ ",
    "║", 
    "║"
    ]

    state5 = [
    "╔════════╗",
    "║        ¥",
    "║        O",
    "║       /|\ ",
    "║       /",
    "║"
    ]

    state6 = [
    "╔════════╗",
    "║        ¥",
    "║        O",
    "║       /|\ ",
    "║       / \ ",
    "║"
    ]

    states = {
    0:state0, 
    1:state1, 
    2:state2,
    3:state3,
    4:state4,
    5:state5,
    6:state6
    }

    def __init__(self):
        self._current_state = Hangman.state0

    def getState(self):
        """
        Returns a list with the hangman at the current state.
        """
        return self._current_state
    
    def setState(self, value):
        """
        value --> the number of errors in integer (0 - 6)
        """
        self._current_state = Hangman.states[value]
    
    def printHangman(self):
        """
        Prints the hangman in its current 
        state on the screen.
        """
        for line in self._current_state:
            print(line)