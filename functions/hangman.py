"""
The hangman has 7 states ranging from state 0 (nothing hanged) 
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

#Function to print the hangman:
def printHangman(erros):
  """
  errors --> the number of errors in integer (0 - 6)
   -------------

   Given the number of errors, prints the hangman in its 
   current state on the screen.
  """
  hangman = states[erros]
  for line in hangman:
    print(line)