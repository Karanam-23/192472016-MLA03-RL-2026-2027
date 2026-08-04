states=["A","B","C","Goal"]

actions={
"A":["Right"],
"B":["Right"],
"C":["Right"]
}

current="A"

while current!="Goal":
    print(current)

    if current=="A":
        current="B"

    elif current=="B":
        current="C"

    elif current=="C":
        current="Goal"

print("Reached Goal")
