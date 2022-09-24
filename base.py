import os

def mainLoop():
    name = "model"
    try:
        categories = int(input("How many categories? "))
    except ValueError:
        print("Please enter a number.")
        mainLoop()
    csv = input("Enter the name of the CSV file: ")
    # Do stuff with the CSV file, PARSE IT HERE
    
    x = input("What do you want to do? (+ for add layer, - for subtract layer")
    if x == "+":
        try:
            howmany = int(input("How many layers do you want to add? "))
        except ValueError:
            print("Please enter a number.")
            mainLoop()
    elif x == "-":
        try:
            howmany = int(input("How many layers do you want to subtract? "))
        except ValueError:
            print("Please enter a number.")
            mainLoop()
    #do something with howmany here in order to add or subtract layers
    #train it here
    print("training")
    #print loss and accuracy here
    print("Saving to local device with name " + name)
    whether = input("Are you satisfied? If not, we can delete and redo. (y/n)")
    if whether == "y":
        print("Saving to local device with name " + name)
        #save it here
    if whether == "n":
        os.remove(os.getcwd() + "/" + name)
        mainLoop()
    else:
        print("Please enter y or n.")
        mainLoop()
    #save it here

mainLoop()

    
