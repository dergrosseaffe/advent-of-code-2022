sum = 0
while True:
    try: w, e = input().split(",")
    except EOFError: break

    wa, wb = w.split("-")
    ea, eb = e.split("-")

    wa, wb = int(wa), int(wb)
    ea, eb = int(ea), int(eb)

    sum += (wa <= ea and wb >= eb) or (ea <= wa and eb >= wb)

print(sum)