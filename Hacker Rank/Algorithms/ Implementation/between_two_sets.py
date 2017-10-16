#!/bin/python3
import sys

def getTotalX():
    n,m = [2, 3]
    a = [2, 4]
    b = [16, 32, 96]
    indexes = []
    combined = a + b
    max_int = max(combined)
    min_int = min(combined)
    range_list = range(min_int,max_int)
    a_to_b = []
    answer = []

    for i in range(min_int,max_int):
        if i % a[0] == 0 and i % a[1] == 0:
            print(i)
            if b[0] % i == 0 and b[1] % i == 0 and b[2] % i == 0:
                answer.append(i)
 
    # for i in range_list:
    #     if i % ai == 0:
    #         print(i)

    # for i in set(a_to_b):
    #     for bi in b:
    #         if bi % i == 0:
    #             answer.append(i)

    # print(answer)


getTotalX()