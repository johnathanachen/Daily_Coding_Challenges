def solve(a0, a1, a2, b0, b1, b2):
    Alice = 0
    Bob = 0
    if a0 > b0:
        Alice = Alice + 1
    elif b0 > a0:
        Bob = Bob + 1
    
    if a1 > b1:
        Alice = Alice + 1
    elif b1 > a1:
        Bob = Bob + 1

    if a2 > b2:
        Alice = Alice + 1
    elif b2 > a2:
        Bob = Bob + 1
    
    print(Alice, Bob)


solve(5, 6, 7, 3, 6, 10)