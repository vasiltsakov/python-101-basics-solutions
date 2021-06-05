def sum_of_digits(n):
    str_list = str(abs(n))
    result = 0
    for letter in str_list:
        result += int(letter)

    return result

print(sum_of_digits(1325132435356))
print(sum_of_digits(123))
print(sum_of_digits(6))
print(sum_of_digits(-10))
