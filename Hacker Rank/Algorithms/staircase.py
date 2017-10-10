def staircase():
    n = 6
    # for num in range(0,n):
    #     print("#" * ((n-1)-num), "o" * (num + 1))
    #     # print("o" * (num + 1))

    for num in range(0,n):
        spread = list("0" * ((n-1)-num))
        if len(spread) < n:
            spread.append("#")
        # b = spread[(n-1):] + [0]
        print(spread)

        # if num < (n-1):
        
        #     print("0")
        # else:
        #     print("#")

    
staircase()