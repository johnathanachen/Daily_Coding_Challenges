import sys

def kangaroo(x1, v1, x2, v2):
    # if x1 < x2:
    #     if v1 > v2:
    #         return "YES"
    #     elif v1 < v2:
    #         return "NO"
    # elif x1 > x2: 
    #     if v1 < v2:
    #         return "YES"
    #     elif v1 > v2:
    #         return "NO"
    # first_kang = (x1 + v1) + v1
    # second_kang = (x2 + v2) + v2
    # kang2_step_two = second_kang * v1
    # kang1_step_two = first_kang * v2
    # if kang2_step_two % kang1_step_two == 0 or kang1_step_two % kang2_step_two == 0:
    #     print("YES")
    # else:
    #     print("NO")
    x = range(0,20)
    first_kang = x1
    second_kang = x2
    results = []
    for i in x:
        first_kang += v1
        second_kang += v2
        if first_kang == second_kang:
            results.append(i)
        else:
            pass

    if len(results) == 0:
        return "NO"
    else: 
        return "YES"
        # if first_kang == second_kang:
        #     print("match")
        # else:
        #     print("not match")
    
x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)