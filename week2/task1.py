sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

print(sample_list[0][0])

sorted_list = sorted(sample_list, key=lambda item: item[1])
print(sorted_list)