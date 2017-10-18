def getRecord():
    # Complete this function
    high = s[0]
    high_list = []
    low = s[0]
    low_list = []
    current = 0

    for i in s:
        if i < low:
            low = i
            low_list.append(i)
        elif i > high:
            high = i
            high_list.append(i)
        else:
            pass

    return len(high_list), len(low_list)
    
    answer = []
    answer.append(str(len(high_list)))
    answer.append(str(len(low_list)))
    print(' '.join(answer))



getRecord()