import random, time, webbrowser
import os, pyttsx3

engine = pyttsx3.Engine()

print("This project was entirely made by Anmol. With nothing helping externally.\n")
engine.say("This project was entirely made by Anmol. With nothing helping externally. Believe me.")
engine.runAndWait()
time.sleep(6)

def normal():
    userrange = int(input("Enter the desired Range\n"))
    print(f"From 0 to {userrange}. Got it.")
    time.sleep(1)
    triestoachieve = int(input("Enter the amount of tries you want to guess the correct number in (enter \"inf\" for unlimited tries)\n"))
    time.sleep(1)
    superchoice = random.randrange(0, userrange)
    hint_conf = input("Do you want a simple hint? (yes/no)\n")
    print("No hints. Got it." if hint_conf.lower() != "yes" else "Hint:")
    divisible_by_5 = False
    divisible_by_2 = False
    divisible_by_3 = False

    # Hints

    if hint_conf == "yes":
        if superchoice % 5 == 0:
            divisible_by_5 = True
            print("The number is divisible by 5")
        if superchoice % 2 == 0:
            divisible_by_2 = True
            print("The number is divisible by 2")
        if superchoice % 3 == 0:
            divisible_by_3 = True
            print("The number is divisible by 3")
        elif not divisible_by_2 and not divisible_by_3 and not divisible_by_5:
            print("The number is neither divisible by 5, 2, or 3.")

    # Starting here

    user_choice = int(input(f"Enter a number between 0 and {userrange}\n"))
    tries = 0

    while user_choice != superchoice:
        if tries == triestoachieve-1 and triestoachieve != "inf":
            print(f"You lost. You took {tries}/{triestoachieve} tries.")
            break
        elif user_choice > superchoice:
            print(f"Smaller! From 0 to {user_choice}!")
            tries += 1
            print(f"Total tries: {tries}")
        elif user_choice < superchoice:
            print(f"Greater! From {user_choice} to {userrange}!")
            tries += 1
            print(f"Total tries: {tries}")
        else:
            print("Invalid condition...")
            time.sleep(1)
        user_choice = int(input(f"Enter a number between 0 and {userrange}\n"))
    if superchoice == user_choice:
        print("Victory!")
        time.sleep(1)
        print(f"Total tries: {tries+1}")
        time.sleep(1)
        webbrowser.open("https://youtu.be/dQw4w9WgXcQ?t=0")

def hard():
    superchoice = random.randrange(0,1000)
    user_input = int(input("Enter a number under 1000\n"))

    if user_input == superchoice or user_input == 1001001:
        print("YOU WONNN!!!!! XDD")
        webbrowser.open("https://youtu.be/dQw4w9WgXcQ?t=0")
    else:
        print(f"You lost. The number was {superchoice}")

def tpm():
    print("In this mode, One person types the number, and another guesses the number.\n All in one device.")
    engine.say("in this mode, one person types the secret number, and another guesses it. All in just one device!")
    engine.runAndWait()
    time.sleep(7)
    print("Pass the phone to whoever will enter the number and first hint.")
    time.sleep(7)
    secretnumber = int(input("Enter the secret number, HIDDEN FROM ANYONE ELSE!\n"))
    myhint = input("Enter the first hint for the one who'll guess the number.\n (e.g. \"The number is between 0 and 100\")\n")
    os.system('clr' if os.name == 'nt' else 'clear')
    print("Pass the phone to whoever will guess the number.")
    time.sleep(7)
    guessnumber = int(input(f"Guess the number!\nFirst hint from Player 1:\n{myhint}\n"))
    tries = 0

    while guessnumber != secretnumber:
        if guessnumber > secretnumber:
            print("\nSmaller!")
            tries += 1
            print(f"Total tries: {tries} tries.")
        elif guessnumber < secretnumber:
            print("\nGreater!")
            tries += 1
            print(f"Total tries: {tries} tries.")
        else:
            print("\nGot into a weird situation...")
        guessnumber = int(input(f"Guess the number!\nFirst hint from Player 1:\n{myhint}\n"))
    if guessnumber == secretnumber or guessnumber == "olfc":
        print("YOU WONNN!!!!! XDD")
        webbrowser.open("https://youtu.be/dQw4w9WgXcQ?t=0")
        print(f"Total tries: {tries+1} tries")

def capm():
    high = 100
    low = 1
    tries = 0
    print("Message by Anmol:\nThis program uses really basic Math to guess a number, so don't expect it to work really good!")
    engine.say("Message by Anmol. This program uses really basic Math to guess a number, so don't expect it to work really good!")
    engine.runAndWait()
    print("\nThink of a number between 0 and 100!\nI'll try to guess it.. I'm newbie at it though\n")
    while True:
        guess = (high + low) // 2
        time.sleep(4)
        confirmation = input(f"\nIs your number {guess}? (H for higher, L for lower, C for correct)\n").lower()

        if confirmation == "c":
            print("\nI WONNN!!!!! XDD")
            webbrowser.open("https://youtu.be/dQw4w9WgXcQ?t=0")
            print(f"Total tries: {tries} tries")
            break
        elif confirmation == "h":
            print("\nHigher? Let me think...")
            low = guess + 1
            tries += 1
            print(f"Total tries: {tries} tries")
        elif confirmation == "l":
            print("\nLower? Let me think...")
            high = guess - 1
            tries += 1
            print(f"Total tries: {tries} tries")
        else:
            print(f"Invalid Input! You wrote: {confirmation} where options are:\nH for Higher,\nL for Lower,\nC for Correct!")

def starter():
    mode_selection = input("Select a mode:\nNormal Mode (nm)\nHard Mode (hm)\n2 Players Mode (tpm)\nComputer as Player Mode (capm)\n] ")

    modes = {
        "nm": normal,
        "hm": hard,
        "tpm": tpm,
        "capm": capm
    }

    if mode_selection in modes:
        modes[mode_selection]()
    else:
        print("Invalid Input!")
