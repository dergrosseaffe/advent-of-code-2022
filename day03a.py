sum = 0
while True:
    try: line = input()
    except EOFError: break

    mid = len(line)//2

    a, b = line[:mid], line[mid:]
    for c in a:
        if c in b:
            diff = 0
            if (ord(c) <= ord('Z')):
                diff = ord(c) - ord('A') + 27
            else:
                diff = ord(c) - ord('a') + 1

            sum += diff
            break

print(sum)