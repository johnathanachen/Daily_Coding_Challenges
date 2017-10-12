def solve():
    grades = [73,67,38,33]
    split_grades = []
    final_answer = []
    for grade in grades:
        split_grades.append(list(str(grade)))

    for grade in split_grades:
        if len(grade) == 1:
            num = ''.join(grade)
            final_answer.append(num)
        else:
            find_difference = int(grade[1]) - 5
            if find_difference == -2 or find_difference == -1:
                del grade[1]
                grade.append('5')
                rounded_num = ''.join(grade)
                final_answer.append(rounded_num)
            elif find_difference == 3 or find_difference == 4:
                grade.append(str(int(grade[0]) + 1))
                del grade[0]
                del grade[0]
                grade.append('0')
                rounded_num = ''.join(grade)
                final_answer.append(rounded_num)
            else:
                num = ''.join(grade)
                final_answer.append(num)

    for i in final_answer:
        print(i)

      

solve()