elves = {}

current = 1
while True:
    try: value = input()
    except EOFError: break

    if (value == ""):
        current += 1
    else:
        value = int(value)

        currentValue = value
        if current in elves:
            currentValue += elves[current]
        elves[current] = currentValue

for k in sorted(elves, key=elves.get, reverse=True):
    print(f"{k}: {elves[k]}")