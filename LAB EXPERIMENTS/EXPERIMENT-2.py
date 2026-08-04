import random

rooms = ["Kitchen","Hall","Bedroom"]

current = random.choice(rooms)

for i in range(5):
    print("Robot in",current)

    if current=="Kitchen":
        current="Hall"

    elif current=="Hall":
        current="Bedroom"

    else:
        current="Kitchen"
