def solve():
    grades = [73,67,38,33]
    answer = []

    for grade in grades:
        if grade > 37:
            grade_split = list(str(grade))
            find_difference = int(grade_split[1]) - 5
            if find_difference == -2 or find_difference == -1:
                del grade_split[1]
                grade_split.append('5')
                rounded_num = ''.join(grade_split)
                answer.append(rounded_num)
            elif find_difference == 3 or find_difference == 4:
                grade_split.append(str(int(grade_split[0]) + 1))
                del grade_split[0]
                del grade_split[0]
                grade_split.append('0')
                rounded_num = ''.join(grade_split)
                answer.append(rounded_num)
            else:   
                answer.append(str(grade))
        else:   
            answer.append(str(grade))
    
    print("\n".join(map(str, answer)))
    return answer
    
solve()