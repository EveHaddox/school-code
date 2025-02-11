import random
import time

x1 = "n"

print("welocme to the roll game!\n")

def start():
    x1 = input("would you like to play? \ny/n\n")

    if (x1 == "y"):

        time.sleep(0.2)

        print("\nRoll a higher number! \n")
        time.sleep(0.3)
        enRoll = random.randrange(0, 101, 2)
        print("enemy rolled: " + str(enRoll))
        time.sleep(0.1)
        plyRoll = random.randrange(0, 101, 2)
        print("you rolled: " + str(plyRoll), "\n")

        time.sleep(0.5)
        if (enRoll > plyRoll):
            print("You Lost\n")
        elif (enRoll < plyRoll):
            print("You Won\n")
        else:
            print("Stelmate\n")

        start()


start()