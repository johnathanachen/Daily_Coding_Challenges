def should_continue(s):
    for index in range(len(s)):
        if index == 0:
            previous_letter = s[index]
        else:
            if s[index] == previous_letter:
                return True
            previous_letter = s[index]
    return False

def super_reduced_string(s):
    previous_letter = ""
    while should_continue(s)
        for index in range(len(s)):
            temp = s
            if index == 0:
                previous_letter = s[index]
            else:
                if s[index] = previous_letter:
                    s = temp[:index-1] + temp[index + 1:]
                    break
                else: 
                    previous_letter = s[index]


super_reduced_string("aaabccddd")
