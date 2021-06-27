def message_to_numbers(message):
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

    temp_key = None
    is_upper = False

    for i in range(len(message)):
        letter = message[i]
        is_upper = letter.isupper()
        letter = letter.lower()

        for key, letters in keypad.items():
            if letter in letters:
                if key == temp_key:
                    result.append(-1)
                if is_upper:
                    result.append(1)
                for x in range(letters.index(letter) + 1):
                    result.append(key)
                    temp_key = key

    return result



tests = [
    ("abc", [2, -1, 2, 2, -1, 2, 2, 2]),
    ("a", [2]),
    ("Ivo e Panda", [1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 2, 6, 6, 3, 2]),
    ("aabbcc", [2, -1, 2, -1, 2, 2, -1, 2, 2, -1, 2, 2, 2, -1, 2, 2, 2])
    ]

for test, expected in tests:
    result = message_to_numbers(test)
    print(result, result == expected)