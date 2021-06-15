def sum_of_digits(n):
    str_list = str(abs(n))
    result = 0
    for letter in str_list:
        result += int(letter)

    return result

def is_number_balanced(number):
    if number >= 0 and number <10:
        return True
    else:
        str_num = str(number)
        len_num = int(len(str_num)/2)
        start_num = int(str_num[:len_num])
        str_num = str_num[::-1]
        end_num = int(str_num[:len_num])

        return sum_of_digits(start_num) == sum_of_digits(end_num)



tests = [
    (9, True),
    (4518, True),
    (1111, True),
    (11111, True),
    (28471, False),
    (1238033, True),
    (123, False),
    (121, True),
    ]

for test, expected in tests:
    result = is_number_balanced(test)

    print(result == expected)

