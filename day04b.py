sum = 0
while True:
    try: w, e = input().split(",")
    except EOFError: break

    wa, wb = w.split("-")
    ea, eb = e.split("-")

    wa, wb = int(wa), int(wb)
    ea, eb = int(ea), int(eb)

    sum += 1 if min(wb, eb) - max(wa, ea) >= 0 else 0

print(sum)