my_points = 0
their_points = 0

while True:
    try: other, me = input().split()
    except EOFError: break
    except ValueError: break

    po, pm = ord(other) - ord('A') + 1, ord(me) - ord('X') + 1
    print(pm, po)
    my_points += pm
    their_points += po

    # calculate outcomes
    match abs(po - pm):        
        case 0: # draw
            my_points += 3
            their_points += 3
            print("case 0", my_points, their_points)
        case 1: # rock < paper < scissors
            if pm > po:
                my_points += 6
            else:
                their_points += 6
            print("case 1", my_points, their_points)
        case 2: # scissors vs rock
            if pm < po:
                my_points += 6
            else:
                their_points += 6
            print("case 2", my_points, their_points)
            
print(my_points, their_points)