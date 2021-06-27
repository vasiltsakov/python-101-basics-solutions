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
    upper_letter = []

    temp_list = []
    
    for i,num in enumerate(pressed_sequence):
        
        if temp_list == []:
            if num == 0:
                count.append((0, 1))
            else:
                temp_list.append(num)

        elif num == temp_list[0]:
            temp_list.append(num)

        elif num == -1:
            count.append((temp_list[0], len(temp_list)))
            temp_list = []

        else:
            count.append((temp_list[0], len(temp_list)))
            temp_list = []
            temp_list.append(num)

    if temp_list:
        count.append((temp_list[0], len(temp_list)))


    for i, (key, pressed) in enumerate(count):
        if (key, pressed) == (1, 1):
            pass
        else:
            if pressed > len(keypad[key]):
                pressed = pressed - (len(keypad[key]) * (pressed // len(keypad[key])))
            if count[i-1] == (1, 1):
                result.append(keypad[key][pressed-1])
                result[-1] = result[-1].upper()
            else:
                result.append(keypad[key][pressed-1])

    return ''.join(result)


tests = [
    ([0, 0, 0, 0], "    "),
    ([2, -1, 2, 2, -1, 2, 2, 2], "abc"),
    ([2, 2, 2, 2], "a"),
    ([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2], "Ivo e Panda"),
    ([2, 3, 4, 5, 6, 7, 8, 9], "adgjmptw"),
    ([2, -1, 3,-1, 4, -1, 5, -1, 6, -1, 7, -1, 8, -1, 9], "adgjmptw"),
    ([2, 2, 2, -1, 2], "ca")
    ]

for test, expected in tests:
    result = numbers_to_message(test)
    print(result, result == expected)