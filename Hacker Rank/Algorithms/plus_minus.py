def plus_minus():
    negatives = []
    postives = []
    zeroes = []
    n = 6
    arr = [-4,3,-9,0,4,1]

    for number in arr:
        if number == 0:
            zeroes.append(number)

    for number in arr:
        if number < 0: 
            negatives.append(number)
        if number > 0:
            postives.append(number)
    
    
    
    neg_fract = len(negatives)/n
    pos_fract = len(postives)/n
    zero_fract = len(zeroes)/n

    print("{0:.6f}".format(round(pos_fract,2)))
    print("{0:.6f}".format(round(neg_fract,2)))
    print("{0:.6f}".format(round(zero_fract,2)))


plus_minus()