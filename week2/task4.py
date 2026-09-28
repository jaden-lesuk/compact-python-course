list_of_strings = ["Java", "HTML", "CSS", "JS"]

def string_to_list(sample):
    return list(sample)

list_of_lists = list(map(string_to_list, list_of_strings))
print(list_of_lists)