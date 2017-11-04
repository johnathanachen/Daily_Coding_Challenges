n = 3
a = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

# for i in a:
#     for index, x in enumerate(i):
#         x[index] + x[index + 1] + x[index + 2]

# for i in range(len(a)):
list_to_add = []
for index, x in enumerate(a):
    list_to_add.append(x[index])

first_diagonal = sum(list_to_add)

second_list_to_add = []
for index, x in enumerate(reversed(a)):
    second_list_to_add.append(x[index])

second_diagnoal = sum(second_list_to_add)

if first_diagonal > second_diagnoal:
    final_sum = first_diagonal - second_diagnoal
else:
    final_sum = second_diagnoal - first_diagonal

print(final_sum)