def count_substring(string, sub_string):
    string = string.upper()
    sub_string = sub_string.upper()
    counter = 0

    # for i in range(0, len(string)):
    #     if string.find(sub_string):
    #         counter += 1
    print(string.find(sub_string))


count_substring("ABCDABC", "ABC")


# Tried:
# for i in range(0, len(string)):
#     x = string.find(sub_string)
# print(x)
# -----------------
# for i in range(0, len(string)):
#     print(string[i])
#     if sub_string in string:
#         counter += 1
# print(counter)
