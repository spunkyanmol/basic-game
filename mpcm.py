import random

# ---------- Helper functions ----------

def ask_number(question, minimum, maximum):
    """Keeps asking until the user types a whole number in the allowed range."""
    while True:
        answer = input(question)
        if answer.isdigit():
            number = int(answer)
            if minimum <= number <= maximum:
                return number
        print("Please type a whole number from", minimum, "to", maximum)


def make_hint(target):
    """Returns a hint saying which of 2, 3, 5 divide the target."""
    divisors = []
    for d in [2, 3, 5]:
        if target % d == 0:
            divisors.append(str(d))

    if len(divisors) == 0:
        return "The number is NOT divisible by 2, 3 or 5"
    return "The number is divisible by " + ", ".join(divisors)


def start_round(players, highest, want_hints):
    """Gives every player a NEW secret number and resets their round data."""
    for p in players:
        p["target"] = random.randint(0, highest)
        p["guess"] = None
        p["tries"] = 0
        p["status"] = "ACTIVE"

        if want_hints:
            print("Hint for", p["name"], "->", make_hint(p["target"]))

def game():
# ---------- Game setup ----------

    print("=== MULTIPLAYER NUMBER GAME ===")

    player_count = ask_number("How many players? ", 1, 20)

    players = []
    for i in range(player_count):
        name = input("Name of player " + str(i + 1) + ": ")
        # Name stays forever. The rest changes every round.
        players.append({
            "name": name,
            "target": 0,
            "guess": None,
            "tries": 0,
            "status": "ACTIVE",
        })

    max_tries = ask_number("Max tries per round? ", 1, 100)
    highest = ask_number("Highest possible secret number? ", 1, 1000000)

    answer = input("Do you want hints (divisible by 2, 3, 5)? (y/n): ")
    want_hints = answer.lower() == "y"

    print()
    print("Secret numbers are between 0 and", highest)
    print("You have", max_tries, "tries per round.")


    # ---------- Game loop ----------

    round_number = 1
    game_over = False

    while not game_over:
        print()
        print("===== ROUND", round_number, "=====")
        start_round(players, highest, want_hints)

        round_failed = False

        while not round_failed and not game_over:

            # PHASE 1: COLLECT - everyone active guesses
            print()
            for p in players:
                if p["status"] == "ACTIVE":
                    p["guess"] = ask_number(p["name"] + ", your guess: ", 0, highest)
                    p["tries"] = p["tries"] + 1

            # PHASE 2: EVALUATE - check all guesses after everyone is done
            print()
            for p in players:
                if p["status"] == "ACTIVE":
                    if p["guess"] == p["target"]:
                        p["status"] = "CORRECT"
                        print(p["name"], "-> Correct!")
                    elif p["guess"] > p["target"]:
                        print(p["\nname"], "-> Your number is smaller.")
                    else:
                        print(p["\nname"], "-> Your number is greater.")

            # Did EVERYONE get it right?
            everyone_correct = True
            for p in players:
                if p["status"] != "CORRECT":
                    everyone_correct = False

            if everyone_correct:
                print()
                print("EVERYONE WINS!")
                game_over = True
            else:
                # Did anyone run out of tries?
                for p in players:
                    if p["status"] == "ACTIVE" and p["tries"] >= max_tries:
                        round_failed = True

        if round_failed:
            print()
            print("Someone ran out of tries! All numbers change.")
            round_number = round_number + 1

    print("Game over. Thanks for playing!")
