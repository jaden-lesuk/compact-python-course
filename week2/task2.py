sample_string = "h1ell2o 9worl1d8"
string_list = list(sample_string)

def is_number(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

only_numbers = list(filter(is_number, string_list))

sum_of_numbers = sum(int(number) for number in only_numbers)
average = sum_of_numbers / len(only_numbers)

print(only_numbers)
print(f"sum: {sum_of_numbers} average: {average}")