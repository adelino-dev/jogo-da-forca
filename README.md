# Jogo da Forca (Hangman Game)

## Requirements
* Python 3.x

## How to Use?

1. Clone the repository:
    ```bash
    git clone https://github.com/adelino-dev/jogo-da-forca.git
    ```

2. Run the file "main.py"


## How to play?

### Description

The Hangman Game is a popular game in which the player must decipher the secret word, taking as a hint the number of letters and the theme connected to the word.

### Rules
1. The player must guess and type a letter of the secret word.

2. If the letter is part of the secret word, the player will score a hit. But if not, the error is logged and the hangman will change state.

3. The player can only to do six errors because the hangman has seven states ranging from state 0 (nothing hanged) up to state 6 (fully hanged):

```
State 0:    State 1:     State 2:
╔════════╗   ╔════════╗    ╔════════╗ 
║        ¥   ║        ¥    ║        ¥
║            ║        O    ║        O
║            ║             ║        |  
║            ║             ║       
║            ║             ║            

State 3:    State 4:     State 5:
╔════════╗   ╔════════╗    ╔════════╗ 
║        ¥   ║        ¥    ║        ¥
║        O   ║        O    ║        O
║       /|   ║       /|\   ║       /|\  
║            ║             ║       / \
║            ║             ║        

State 6:
╔════════╗ 
║        ¥
║        O
║       /|\  
║       / \
║      
```

4. If the player types any invalid characters (such as numbers and punctuation) or 
types more than one letter at the same time or types a letter he/she has typed before, 
the player will be prompted to enter again.

5. If the player hits all the letters, he wins. otherwise, he loses.

6. At the end of the game, the player is asked if he wants to play another round.