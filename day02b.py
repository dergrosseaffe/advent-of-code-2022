my_points = 0
while True:
    try: other, me = input().split()
    except EOFError: break
    except ValueError: break

    po, pm = ord(other) - ord('A'), ord(me) - ord('X')
    my_points += (po - 1 + pm)%3 + 1 + pm*3
    print(po, pm, my_points)
            
print(my_points)