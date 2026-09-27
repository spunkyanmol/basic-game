import game1

print("========================================",
    "\nNAME                |           SHORTCUT",
    "\n----------------------------------------",
    "\ngame1               |                 g1",
    "\n========================================")

selection = input("\nSelect a game (enter its shortcut code)\n] ")

if selection == "g1":
    print("\n")
    game1.starter()
else:
    print("Invalid argument.")
