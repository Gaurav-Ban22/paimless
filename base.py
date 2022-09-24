import os

RESET = "\u001B[0m"
BLACK = "\u001B[30m"
RED = "\u001B[31m"
GREEN = "\u001B[32m"
YELLOW = "\u001B[33m"
BLUE = "\u001B[34m"
PURPLE = "\u001B[35m"
CYAN = "\u001B[36m"
WHITE = "\u001B[37m"
BLACK_BOLD = "\033[1;30m"
RED_BOLD = "\033[1;31m"
GREEN_BOLD = "\033[1;32m"
YELLOW_BOLD = "\033[1;33m"
BLUE_BOLD = "\033[1;34m"
PURPLE_BOLD = "\033[1;35m"
CYAN_BOLD = "\033[1;36m"
WHITE_BOLD = "\033[1;37m"


def colorize(text, color):
    return color + text + RESET

def mainLoop():
    name = "model"
    try:
        categories = int(input("How many categories? "))
    except ValueError:
        print(colorize("Please enter a number.", GREEN))
        mainLoop()
    csv = input(colorize("Enter the name of the CSV file: ", BLUE))
    # Do stuff with the CSV file, PARSE IT HERE
    
    x = input(colorize("What do you want to do? (+ for add layer, - for subtract layer", YELLOW))
    if x == "+":
        try:
            howmany = int(input(colorize("How many layers do you want to add? ", YELLOW)))
        except ValueError:
            print(colorize("Please enter a number.", RED))
            mainLoop()
    elif x == "-":
        try:
            howmany = int(input(colorize("How many layers do you want to add? ", YELLOW)))
        except ValueError:
            print(colorize("Please enter a number.", RED))
            mainLoop()
    #do something with howmany here in order to add or subtract layers
    #train it here
    print("training")
    #print loss and accuracy here
    print(colorize("Saving to local device with name " + name, GREEN))
    whether = input(colorize("Are you satisfied? If not, we can delete and redo. (y/n)", BLUE))
    if whether == "y":
        print("Saving to local device with name " + name)
        #save it here
    if whether == "n":
        print("Removing")
        os.remove(os.getcwd() + "/" + name)
        mainLoop()
    else:
        print(colorize("Please enter y or n.", RED))
        mainLoop()
    #save it here

mainLoop()

    