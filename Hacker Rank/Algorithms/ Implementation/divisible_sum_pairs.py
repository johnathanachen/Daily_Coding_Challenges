def divisibleSumPairs():
    n,k = [6,3]
    ar = [1, 3, 2, 6, 1, 2]
    all_sum = []
    current_add = 0

    for index, x in enumerate(ar):    
        current = x
        next_num = ar[index+1]
        while len(all_sum) < len(ar) - 1:
            sum_num = current + next_num
            all_sum.append(sum_num)
            
    print(all_sum)
    # for i in ar:
    #     ar2.append(i)

    # for index, x in enumerate(ar):
    #     while len(new_list) < len(ar2) - 1:
    #         pair = ar[index + 1] + ar[index + 1]
    #         new_list.append(pair)
    #         ar.pop(1)

    # for i in ar2:
    #     ar3.append(i)

    # for index, x in enumerate(ar2):
    #     while len(new_list2) < len(ar3) - 2:
    #         pair = ar2[index + 1] + ar2[index + 2]
    #         new_list2.append(pair)
    #         ar2.pop(2)
    # print(new_list2)

divisibleSumPairs()