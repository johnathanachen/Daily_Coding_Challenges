def round_grades():
    grades = [4,73,67,38,33]
    grade_arr = []
    for grade in grades:
        if grade > 37:
            for single_grade in str(grade):
                split_grade = list(single_grade)
                grade_arr.append(split_grade)
            oneth_digit = ''.join(grade_arr[1]) 
            check_rounding = int(oneth_digit) - 5
            # round up for 5
            if check_rounding == -2 or check_rounding == -1:
                converted_nums = []
                oneth_digit = ["5"]
                del grade_arr[1]
                grade_arr.append(oneth_digit)
                for i in grade_arr:
                    for x in i:
                        converted_nums.append(x)
                converted_results = ''.join(converted_nums)
                # print(converted_results)
            # round up for 10
            elif check_rounding == 3 or check_rounding == 4:
                oneth_digit = ["0"]
                tenth_digit = ''.join(split_grade)
                tenth_digit_added = int(tenth_digit) + 1
                tenth_digit_list = [str(tenth_digit_added)]
                converted_nums = []
                del grade_arr[0]
                grade_arr.append(tenth_digit_list)
                del grade_arr[0]
                grade_arr.append(oneth_digit)
                for i in grade_arr:
                    for x in i:
                        converted_nums.append(x)
                converted_results = ''.join(converted_nums)
                # print(converted_results)
        elif grade < 10:
            # print("low")
            pass
        else:
            # print(grade)
            pass
round_grades()