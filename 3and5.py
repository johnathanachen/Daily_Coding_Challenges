# find the sum of all multiples of 3 or 5 below 1000
 

up_to_1000 = range(1,1000)
multiples_of_3_array = []
multiples_of_5_array = []
other = []


def sum_multiples():
    for i in up_to_1000:
        if i % 3 == 0:
            multiples_of_3_array.append(i)
        elif i % 5 == 0:
            multiples_of_5_array.append(i)
        else:
            other.append(i)

    combined_3_and_5_multiples = multiples_of_3_array + multiples_of_5_array

    solution = sum(combined_3_and_5_multiples)
    print(combined_3_and_5_multiples)
    print(solution)
    
    return 


sum_multiples()

