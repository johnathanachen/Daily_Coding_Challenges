#!/bin/python3
import sys

def getTotalX():
    n,m = [2, 3]
    a = [2, 4]
    b = [16, 32, 96]

    combined = a + b
    max_int = max(combined)
    min_int = min(combined)
    range_list = range(min_int,max_int)
    answer = []

    # for i in range_list:
    #     if i % a[0] == 0 and i % a[1] == 0:
    #         print(i)
    #         if b[0] % i == 0 and b[1] % i == 0 and b[2] % i == 0:
    #             answer.append(i)

    x = list(map(a.index,a))
    print(x)

    # for x in a:
    #     for i in range_list:
    #         if i % x == 0:
    #             print(i)

    # for i in a:
    #     a = i
    #     for x in range_list:
    #         if x % a == 0:
            #     print(x)

    # for i in range_list:
    #     if i % a == 0:
    #         print(i)

    # for i in set(a_to_b):
    #     for bi in b:
    #         if bi % i == 0:
    #             answer.append(i)

    # print(answer)


getTotalX()