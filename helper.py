from random_word import RandomWords;
import time;
import sys;
# Initialization of game

def __init__():
    print ("Hi!\n");
    print ("Welcome to the game of HANGMAN");
    print ("\n");

    print ("Thinking a word for you");

    animation = "|/-\\"

    for i in range(50):   

        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
        time.sleep(0.1)


def getRandomWord():
    return RandomWords().get_random_word();    


# Helper Functions
def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]