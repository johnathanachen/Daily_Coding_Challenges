# Don't exceed four million, get sum of all even
import sys

def fibonacci(num):

    # range_calc = list(range(1,1000))
    temp = []
    previous = 0
    current = 1
    new_result = []

    for x in range(num): 
        added = previous + current
        # print(sum)
        previous = current 
        current = added
        temp.append(added)
        
    all_sums = temp

    for i in all_sums:
        if i < 4000000 and i % 2 == 0:
            new_result.append(i)
    
    solution = sum(new_result)
    print(solution)

        
    # for num in range_calc:
    #     if num % 2 == 0:
    #         temp.append(num)

    # even_sum = sum(temp)

    # print(temp)
    # print(even_sum)

fibonacci(100)

#         global tempvar
#         tempvar = temp


    
# fibonacci()

# def sum_of_evens(previous, current):


# sum_of_evens(previous, current)
