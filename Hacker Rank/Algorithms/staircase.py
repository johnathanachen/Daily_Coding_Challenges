def staircase():
    n = 6
    for num in range(0,n):
        spread = list(" " * ((n-1)-num))
        while len(spread) < n:
            spread.append("#")

        join_arr = ''.join(spread)
        print(join_arr)

staircase()