import random

def start():
    printans = 0
    invalid = 0
    print("Please choose a setting:\n Easy - 1-10\n Medium - 1-100\n Hard - 1-1000")
    setting = input()
    try:
        setting = int(setting)
        if setting < 1 or setting > 20:
            invalid = 1
        elif setting > 10:
            printans = 1
            setting = int(setting)-10
    except:
        setting = setting.lower()
        word = True
        finder = ["easy", "medium", "hard", "extreme", "insane", "6", "7", "8", "9", "impossible"] #numbers will never reach here, just for making impossible the 10th setting
        for i in range(len(finder)):
            if setting == finder[i]:
                setting = i+1
                break
        else:
            invalid = 1
    if invalid == 1:
        print("Invalid setting (" + str(setting) + "), using default")
        rngmax = 100
    elif setting == 10:
        rngmax = 100**100
    else:
        rngmax = 10**setting
    print("Enter a number beteween 1 and", rngmax)
    main(rngmax, printans, 0, 0)

def main(rngmax, printans, wins, guesses): #wins and guesses variables specified to initialise and reduce lines. may also allow for continuing a game
    num = random.randint(1,rngmax)
    while True:
        if printans == 1:
            print("The correct number is", num)
        answer = input()
        try:
            answer = int(answer)
        except:
            if answer == "stop" or answer == "break":
                start() #not sure whether this would cause a mem leak in python as the infinite loop is still on, just interrupted
            print("To stop guessing, enter 'stop'")
            answer = -1
        if answer < 1 or answer > rngmax:
            print("Your answer,", answer, "is out of range 1-" + str(rngmax))
        else:
            guesses = guesses+1
        if answer == num:
            wins = wins+1
            print("You have won", wins, "times and guessed", guesses, "times!")
            if guesses == wins and wins > 10:
                for index in range(10):
                    print("Stop cheating dude")
            num = random.randint(1,rngmax)
        elif answer > num and answer < rngmax+1:
            print("Too high, try again!")
        elif answer < num and answer > 0:
            print("Too low, try again!")

start()
