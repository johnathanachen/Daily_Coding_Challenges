import sys

def distance():
    apple_ranges = []
    number_of_apples_in_range = []
    number_of_oranges_in_range = []
    orange_ranges = []
    # apple = [-2, 2, 1]
    # orange = [5, -6]
    # a,b = [5, 15]
    # s,t = [7, 11]

    for count in apple:
        apple_ranges.append(count + a)
    for count in apple_ranges:
        if count >= s and count <= t: 
            number_of_apples_in_range.append(count)
    print(len(number_of_apples_in_range))

    for count in orange:
        orange_ranges.append(count +b)
    for count in orange_ranges:
        if count >= s and count <= t: 
            number_of_oranges_in_range.append(count)
    print(len(number_of_oranges_in_range))



# s,t = input().strip().split(' ')
# s,t = [int(s),int(t)]
# a,b = input().strip().split(' ')
# a,b = [int(a),int(b)]
# m,n = input().strip().split(' ')
# m,n = [int(m),int(n)]
# apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
# orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

distance()