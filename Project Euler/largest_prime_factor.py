# prime factor of 600851475143

prime_numbers = []
divide_this = 0

def prime_factor(num):
    if num % 2 == 0:
        prime_numbers.append(2)
        divide_this = (num/3)
    elif num % 3 == 0:
        prime_numbers.append(3)
        divide_this = (num/3)
    elif num % 5 == 0:
        prime_numbers.append(5)
        divide_this = (num/3)
    elif num % 7 == 0:
        prime_numbers.append(7)
        divide_this = (num/3)
    elif num % 11 == 0:
        prime_numbers.append(11)
        divide_this = (num/3)

    while divide_this > 11
    
    prime_factor(divide_this)


    print(prime_numbers)
    print(divide_this)

    
prime_factor(75)



