def numbers_to_message(pressed_sequence):
    keypad = {
    2 : ['a', 'b', 'c'],
    3 : ['d', 'e', 'f'],
    4 : ['g', 'h', 'i'],
    5 : ['j', 'k', 'l'],
    6 : ['m', 'n', 'o'],
    7 : ['p', 'q', 'r', 's'],
    8 : ['t', 'u', 'v'],
    9 : ['w', 'x', 'y', 'z'],
    0 : [' ']
    }

    result = []
    count = []

    temp_list = []
    # print(f'temp_list: {temp_list}')
    # temp_list.append(pressed_sequence[0])
    # print(f'temp_list: {temp_list}')

    for num in pressed_sequence:
        print(f'num: {num}')
        # print(temp_list)
        if temp_list == []:
            temp_list.append(num)
            print(f'temp_list: {temp_list}')

        elif num == temp_list[0]:
            temp_list.append(num)
            print(f'temp_list: {temp_list}')

        elif num == -1:
            count.append((temp_list[0], len(temp_list)))
            print(f'num is -1, count: {count}')
            temp_list = []

        else:
            count.append((temp_list[0], len(temp_list)))
            print(f'num is different, count: {count}')
            temp_list = []

    count.append((temp_list[0], len(temp_list)))

        # count.append((temp_list[0]))


    # temp_number = pressed_sequence[0]
    # count_number = 1

    # for i in range(1, len(pressed_sequence)):
    #     print(f'i: {i}, temp_number: {temp_number}, count_number: {count_number}')
    #     if pressed_sequence[i] == temp_number:
    #         count_number += 1
    #     elif pressed_sequence[i] == -1:
    #         count.append((temp_number, count_number))
    #         temp_number = pressed_sequence[i+1]
    #         count_number = 1
    #         print(f'from elif: {count}')
    #     else:
    #         count.append((temp_number, count_number))
    #         print(f'from else: {count}')
    #         temp_number = pressed_sequence[i+1]
    #         count_number = 1


        


    for key, pressed in count:
        result.append(keypad[key][pressed-1])




    return ''.join(result)


tests = [
    # ([2, -1, 2, 2, -1, 2, 2, 2], "abc"),
    # ([2, 2, 2, 2], "a"),
    ([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2], "Ivo e Panda")
    ]

for test, expected in tests:
    result = numbers_to_message(test)
    print(result, result == expected)