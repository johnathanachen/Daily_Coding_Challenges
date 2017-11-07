def migratoryBirds(n, ar):
    count = []
    for i in ar:
        count.append(ar.count(i))
    max_num = max(count)
    index_of_num = count.index(max_num)
    highest_ID = ar[index_of_num]


migratoryBirds(6, [1,4,4,4,5,3])
