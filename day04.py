sum1 = 0; sum2 = 0
while True:
    try: w, e = input().split(",")
    except EOFError: break

    wa, wb = w.split("-")
    ea, eb = e.split("-")

    wa, wb = int(wa), int(wb)
    ea, eb = int(ea), int(eb)

    sum1 += (wa <= ea and wb >= eb) or (ea <= wa and eb >= wb)
    sum2 += 1 if min(wb, eb) - max(wa, ea) >= 0 else 0

print(sum1, sum2)