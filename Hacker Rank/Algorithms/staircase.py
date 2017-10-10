def staircase():
    n = 6
    for num in range(0,n):
        print("#" * ((n-1)-num), "o" * (num + 1))

    # print("#" * (n - 5))
    # print("#" * (n - 4))
    # print("#" * (n - 3))
    # print("#" * (n - 2))
    # print("#" * (n - 1))
    # print("#" * n)
staircase()