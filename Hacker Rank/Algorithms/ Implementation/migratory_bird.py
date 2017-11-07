def migratoryBirds(n, ar):
    count = []
    arry_of_highest_num_index = []
    biggest = []

    for i in ar:
        count.append(ar.count(i))

    max_num = max(count)

    for index, i in enumerate(count):
        if i == max_num:
            arry_of_highest_num_index.append(index)

    # get a list of the most frequent ID
    for index, i in enumerate(ar):
        for x in arry_of_highest_num_index:
            if index == x:
                biggest.append(i)

    # find the smallest ID from the most occured list
    one_set = list(set(biggest))
    smallest_most_freq = min(one_set)
    print(smallest_most_freq)


migratoryBirds(6, [1,4,4,4,5,5,5])
