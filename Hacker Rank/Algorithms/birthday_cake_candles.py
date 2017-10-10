# def birthdayCakeCandles():
#     n = 4
#     ar = [3,2,1,3]

#     max_number = max(ar)
#     appear_count = ar.count(max_number)
#     print(appear_count)

# birthdayCakeCandles()

def birthdayCakeCandles(n, ar):
    max_number = max(ar)
    appear_count = ar.count(max_number)
    return appear_count
    print(appear_count)

n = 4
ar = [1,2,3,4]
result = birthdayCakeCandles(n, ar)
print(result)
