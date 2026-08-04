states = ["Start", "Middle", "Check", "Win"]
actions = {
    "Start": ["Attack", "Defend"],
    "Middle": ["Attack", "Retreat"],
    "Check": ["Checkmate", "Retreat"]
}

reward = {
    ("Start","Attack"):5,
    ("Start","Defend"):2,
    ("Middle","Attack"):10,
    ("Middle","Retreat"):-5,
    ("Check","Checkmate"):100,
    ("Check","Retreat"):-20
}

state = "Start"

while state!="Win":
    print("Current State:",state)
    action=input("Choose action: ")

    if state=="Start" and action=="Attack":
        state="Middle"

    elif state=="Middle" and action=="Attack":
        state="Check"

    elif state=="Check" and action=="Checkmate":
        state="Win"

    else:
        print("Game Over")
        break

print("You Win!")
