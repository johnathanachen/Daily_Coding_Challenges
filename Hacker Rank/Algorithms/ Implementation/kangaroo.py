import sys

def kangaroo(x1, v1, x2, v2):
    if x1 < x2:
        if v1 > v2:
            return "YES"
        elif v1 < v2:
            return "NO"
    elif x1 > x2: 
        if v1 < v2:
            return "YES"
        elif v1 > v2:
            return "NO"

    
x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)