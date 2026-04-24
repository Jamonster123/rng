import random

def start():
    printans = 0
    invalid = 0
    print("Please choose a setting:")
    print(" Easy - 1-10\n Medium - 1-100\n Hard - 1-1000")
    setting = input()
    try:
        setting = int(setting)
        if setting < 1 or setting > 20:
            invalid = 1
        elif setting > 10:
            printans = 1
            setting = str(int(setting)-10)
    except:
        setting = setting.lower()
    finder = ["easy", "medium", "hard", "extreme", "insane", "none", "none", "none", "none" "impossible"]
    try:
        setting = int(setting)
    except:
        for i in range(len(finder)):
            if setting == finder[i]:
                print(setting)
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
"""
if setting == "easy" or setting == "1":
    rngmax = 10
elif setting == "medium" or setting == "2":
    rngmax = 100
elif setting == "hard" or setting == "3":
    rngmax = 1000
elif setting == "extreme" or setting == "4":
    rngmax = 10000
elif setting == "insane" or setting == "5":
    rngmax = 1000000
elif setting == "impossible" or setting == "6":
    rngmax = random.randint(10,50)**random.randint(10,50)
else:
    rngmax = 100
    print("Invalid setting (" + setting + "), using default max of 100")
"""

def main(rngmax, printans, wins, guesses):
    num = random.randint(1,rngmax)
    while True:
        if printans == 1:
            print(num)
        answer = input()
        try:
            answer = int(answer)
        except:
            if answer == "stop":
                start()
            answer = -1
        if answer < 1 or answer > rngmax:
            print("Your answer,", answer, "is out of range 1-" + str(rngmax))
        else:
            guesses = guesses+1
        if answer == num:
            wins = wins+1
            print("You have won", wins, "times and guessed", guesses, "times!")
            num = random.randint(1,rngmax)
            if guesses == wins and wins > 10:
                for index in range(10):
                    print("Stop cheating dude")
        elif answer > num and answer < rngmax+1:
            print("Too high, try again!")
        elif answer < num and answer > 0:
            print("Too low, try again!")

start()
