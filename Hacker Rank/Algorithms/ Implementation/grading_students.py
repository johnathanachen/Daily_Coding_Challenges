def round_grades():
    grades = [71,73,67,38,33,48]
    single_digits = []
    answer_list = []
    for every_grade in grades:
        single_digit = list(str(every_grade))
        single_digits.append(single_digit)
        # CORRECT - filtering 37 or up
        if every_grade > 37:
            for oneth_place in single_digits:
                check_rounding = int(oneth_place[1]) - 5
                round_ups = [-2,-1,3,4,0]
                if check_rounding in round_ups:
                    # rounds 03 and 04
                    if check_rounding == -2 or check_rounding == -1:
                        oneth_place.remove(oneth_place[1])
                        oneth_place.append('5')
                        joined_numbers = ''.join(oneth_place)
                        print(every_grade, "was rounded to", joined_numbers)
                    # rounds five 08 and 09    
                    elif check_rounding == 3 or check_rounding == 4 :
                        oneth_place.remove(oneth_place[1])
                        oneth_place.append('0')
                        tenth_add_one = int(oneth_place[0]) + 1
                        oneth_place.remove(oneth_place[0])
                        oneth_place.insert(0, str(tenth_add_one))
                        joined_numbers = ''.join(oneth_place)
                        print(every_grade, "was rounded to", joined_numbers)
                
        # all under 40
        else:
            joined_numbers = ''.join(oneth_place)
            print(every_grade, "stayed the same", joined_numbers)
            


    # print(answer_list)

        #     if round_five == -2 or -1 or 3 or 4 or 0:
        #         print(i,"round up")
        #     else:
        #         print(i, "round down")

round_grades()

# 71 - 5 = -4 N
# 72 - 5 = -3 N 

# 73 - 5 = -2
# 74 - 5 = -1

# 76 - 5 = 1  N 
# 77 - 5 = 2  N

# 78 - 5 = 3 
# 79 - 5 = 4
