# Made By Skj0nes-2 | https://github.com/Skj0nes-2

# Notes:
#    All sections are optional!
#    Classic is often used for simple operations such as a calculator

# Language Definitions
#    1. Persistent Memory; refers to a file at the main file's location containing data
#    2. File; refers to a file at the location that the user is operating from containing data
#    3. Temporary Memory; refers to data stored temporarily, in the main file, while the main file is running

# Pros & Cons:

#   Pros:
#       1. Is easier to read/write as a developer

#   Cons:
#       1. Can be harder to reuse/repeat sections of the code

# Uses:
#    1. Simple Operations; Reasons: Simpler, easy functions

# What is this example?:
#    This example asks your name, adds it to an array, prints the array, and then saves the array to persistent memory


# All below is the example


# Imports - Import
import numpy as np

# Definitions - Establish definitions / Import definitions

def loadarr(name:str ): # Load Numpy array
    import numpy as np
    try:
        arr = np.load(f"{str(name)}.npy")
    except FileNotFoundError:
        arr = np.array([])
        np.save(str(name), arr)
    except Exception as e:
        print(f"Array {str(name)} failed to load!\nErr: {e}")
        arr = np.array([])
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

# Variables - Establish variables
mem = autoPath('mem')

# Load - Load persistent memory / Load file
arr = loadarr(mem)

# Start menu - Used if program has multiple functions / optional options / or if program should not autostart / not often used in Classic

# Input - Take input from user
name = input("Name: ")

# Main - Logic / Modify temporary memory / Modify persistent memory / Modify file
arr = np.append(arr, name)

# Output - Show Result / Write result to file / Write result to persistent memory
print(arr)

# Save - Save persistent memory / Write to file
savearr(mem, arr)
