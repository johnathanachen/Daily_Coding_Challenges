def test_numbers(n):
    if n % 2 == 0 and n in range(2,5):
        print("Not Weird")
    elif n % 2 == 0 and n in range(6,20):
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")
    else: 
        print("Weird")

test_numbers(4)