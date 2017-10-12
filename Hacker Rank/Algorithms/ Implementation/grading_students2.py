def round_grades():
    grades = 73  
    grade_arr = []
    if grades > 37:
        for grade in str(grades):
            split_grade = list(str(grade))
            grade_arr.append(split_grade)
        oneth_digit = ''.join(grade_arr[1]) 
        check_rounding = int(oneth_digit) - 5
        # round up for 5
        if check_rounding == -2 or check_rounding == -1:
            # oneth_digit.replace(str(check_rounding), "5")
            # print(oneth_digit)
            # oneth_place.remove(oneth_place[1])
            # oneth_place.append('5')
            # joined_numbers = ''.join(oneth_place)
            # print(every_grade, "was rounded to", joined_numbers)
        # round up for 10
        elif check_rounding == 3 or check_rounding == 4:
            print("round to 10")
    else:
        print("nothing")
round_grades()