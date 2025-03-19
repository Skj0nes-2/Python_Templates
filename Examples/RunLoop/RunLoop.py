# Made by Skj0nes-2 | https://github.com/Skj0nes-2

# Notes:
#    All sections are optional!
#    Run Loop is often used in more complicated projects such as games
#    Code does not have to loop!
#    Not all code has to be contained within a function!

# Language Definitions:
#    1. Persistent Memory; refers to a file at the main file's location containing data
#    2. File; refers to a file at any location containing data
#    3. Temporary Memory; refers to data stored temporarily, in the main file, while the main file is running; Examples: Variable, Function, Etc
#    4. Run Loop; When code is separated into functions and then the functions are run

# Pros & Cons:

#   Pros:
#       1. Allows for easy reuse/repeating of sections of the code

#   Cons:
#       1. Can be harder to read/write as a developer

# Uses:
#    1. Games; Reasons: More robust functions
#    2. Complicated operations; Reasons: More robust functions

# What is this example?:
#    This example is the game Rock Paper Scissors made in this form


# All below is the example


# Imports
import numpy as np
import random as ran

# Definitions - Establish definitions / Import definitions

#    Extra Definitions  - Definitions not part of run loop
def loadarr(name:str ): # Load Numpy array
    import numpy as np
    try:
        arr = np.load(f"{str(name)}.npy")
    except FileNotFoundError:
        arr = np.array([["All","Games","Below"]])
        np.save(str(name), arr)
    except Exception as e:
        print(f"Array {str(name)} failed to load!\nErr: {e}")
        arr = np.array([["All","Games","Below"]])
    return arr
      
def savearr(name:str, arr): # Save numpy array
    import numpy as np
    try:
        np.save(str(name), arr)
    except Exception as e:
        print(f"Array {str(name)} failed to save!\nErr: {e}")

def autoPath(name): # Find memory path
    from os import path
    currentFile = path.realpath(__file__)
    currentFileName = path.basename(__file__)
    currentFilePath = currentFile.rstrip(currentFileName)
    path = f"{currentFilePath}{name}" 
    return path 

def clear():
    from os import system, name
    system('cls' if name == 'nt' else 'clear')

#    Load Definition - Load persistent memory / Load file
def def_load():
    global loadarr
    global mem
    global arr; arr = loadarr(mem)

# Start menu - Used if program has multiple functions / optional options / or if program should not autostart / often used in Run Loop
def def_menu():
    global arr
    start = input("(P)lay (C)lear Memory (E)xit: ").upper()
    if start == "C":
        arr = np.array([["All","Games","Below"]])
        start2 = input("(P)lay (E)xit: ").upper()
        if start2 == "E":
            exit()
    elif start == "E":
        exit()

#    Input Definition  - Take input from user
def def_input():
    global arr
    global hand; hand = input("Hand? (R)ock (P)aper (S)cissors: ").upper()
    global output; output = input("Output Type? (T)his Game (A)ll Games: ").upper()
    global clear
    if hand == "R":
        hand = 1
    elif hand == "P":
        hand = 2
    else:
        hand = 3
    clear()
  
#    Main Definition - Logic / Modify temporary memory / Modify persistent memory / Modify file
def def_main():
    global hand
    global results
    global bot
    global arr
    bot = ran.randint(1, 3)
    if hand == bot:
        results = "Tied"
    elif hand == 1 and bot == 3 or hand == 2 and bot == 1 or hand == 3 and bot == 2:
        results = "Won"
    else:
        results = "Lost"
    new_row = np.array([[f'Bot: {bot}', f'Hand: {hand}', f'Result: {results}']])
    arr = np.concatenate((arr, new_row), axis=0)
     
#    Output Definition - Show Result / Write result to file / Write result to persistent memory
def def_output():
    global output
    global results
    global arr
    if output == "T":
        print("You " + results)
    else:
        print("You " + results)
        print(str(arr).replace("[", "").replace("]", "").replace("'", ""))
        

#    Save Definition - Save persistent memory / Write to file
def def_save():
    global savearr
    global mem
    savearr(mem, arr)  

# Variables
mem = autoPath('mem')

# Run Loop - Runs definitions containing code and general code

#    Run Load
def_load()

#    Run Menu
def_menu()

while True:
#       Run Input
    def_input()
        
#       Run Main
    def_main()
        
#       Run Output
    def_output()
    
#       Loop Check
    isplaying = input("Play again? (Y)es (N)o: ")
    if isplaying == "N":
        break
    clear()
    
#    Run Save
def_save()
