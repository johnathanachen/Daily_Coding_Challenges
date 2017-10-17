def getRecord():
    # Complete this function
    arr = [10, 5, 20, 20, 4, 5, 2, 25, 1]
    high = arr[0]
    high_list = []
    low = arr[0]
    low_list = []
    current = 0

    for i in arr:
        if i < low:
            low = i
            low_list.append(i)
        elif i > high:
            high = i
            high_list.append(i)
        else:
            pass

    answer = []
    answer.append(str(len(high_list)))
    answer.append(str(len(low_list)))
    print(' '.join(answer))



getRecord()