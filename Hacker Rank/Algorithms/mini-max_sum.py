def min_max_sum():
    arr = [1,2,3,4,5]
    sum_total = []
    for num in arr:
        x = sum(arr) - num
        sum_total.append(x)

    print(min(sum_total), max(sum_total))