#!/bin/python3
import sys

def simpleArraySum(n, ar):
    x = sum(ar)
    return x
        

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)