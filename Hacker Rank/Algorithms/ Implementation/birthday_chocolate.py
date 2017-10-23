# def solve():
#     n = 5
#     s = [1, 2, 1, 3, 2 ]
#     d,m = [3,2] 
#     current_num = 0 
#     next_num = 0
#     counter = 0
#     all_sum = []
#     for index, x in enumerate(s):
#         if index < len(s) - 1 :
#             current = x
#             next_num = s[index+1]
#             sum_num = current + next_num
#             all_sum.append(sum_num)

#     for i in all_sum:
#         if d == i:
#             counter += 1
#     print(counter)

def solve():
    n = 1
    s = 4
    d,m = [4, 1]
    # n = 5
    # s = [1, 2, 1, 3, 2 ]
    # d,m = [3,2] 
    current_num = 0 
    next_num = 0
    counter = 0
    all_sum = []
    if type(s) == int:
        if d == s and m == 1:
            print("1")
        else:
            print("0")
    else:
        for index, x in enumerate(s):
            if index < len(s) - 1 :
                current = x
                next_num = s[index+1]
                sum_num = current + next_num
                all_sum.append(sum_num)
        for i in all_sum:
            if d == i:
                counter += 1
        print(counter)
        

    


solve()
