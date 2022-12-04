sum = 0
group = []
counter = 0
while True:
    try: a, b, c = input(), input(), input()
    except EOFError: break

    for x in a:
        if x in b and x in c:
            diff = 0
            if (ord(x) <= ord('Z')):
                diff = ord(x) - ord('A') + 27
            else:
                diff = ord(x) - ord('a') + 1

            sum += diff
            break

print(sum)