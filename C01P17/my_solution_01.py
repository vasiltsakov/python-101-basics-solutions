def find_word(len_word, coordinates, direction, matrix):
    
    xd = 0
    yd = 0

    x = 0
    y = 0

    next_word = []

    if direction == 'e':
        xd = 0
        yd = 1

        x, y = coordinates
        
    for num in range(len_word):
        
        point = matrix[x][y]
        next_word.append(point)
        x = x + xd
        y = y + yd

    return "".join(next_word)

def word_counter(matrix, word):
    
    result = 0

    direction = ['n', 's', 'w' , 'e', 'nw', 'ne', 'sw', 'se']

    # for y, row in enumerate(matrix):
    #     for x, col in enumerate(row):
    #         for d in direction:
    #             # print(f'x: {x}, y: {y}, d: {d}')
    #             next_word = find_word(len(word), (x, y), d, matrix)
    #             if next_word == word:
    #                 result += 1

    result = find_word(len(word), (0, 0), 'e', matrix)

    return result


word = "ivan"
matrix = [
    ["i", "v", "a", "n"],
    ["e", "v", "n", "h"],
    ["i", "n", "a", "v"],
    ["m", "v", "v", "n"],
    ["q", "r", "i", "t"]
]
result = word_counter(matrix, word)
print(result, result == 3)

# word = "actually"
# matrix = [
#     ["i", "v", "a", "n", "q", "h", "r", "e", "z", "g", "t", "z", "o", "y", "m"],
#     ["e", "v", "n", "h", "t", "r", "x", "e", "k", "y", "d", "a", "i", "l", "c"],
#     ["i", "a", "c", "t", "u", "a", "l", "l", "y", "m", "c", "x", "r", "l", "e"],
#     ["m", "v", "c", "n", "p", "u", "a", "m", "n", "t", "l", "u", "e", "a", "a"],
#     ["q", "r", "i", "t", "w", "e", "a", "q", "u", "p", "r", "x", "t", "u", "z"],
#     ["p", "e", "a", "c", "t", "u", "a", "l", "l", "y", "w", "p", "y", "t", "m"],
#     ["o", "y", "h", "t", "r", "e", "l", "u", "f", "p", "q", "n", "z", "c", "s"],
#     ["p", "a", "c", "t", "u", "a", "l", "l", "y", "u", "r", "e", "q", "a", "r"]
# ]
# result = word_counter(matrix, word)
# print(result, result == 4)

# word = "madam"
# matrix = [
#     ["z", "v", "a", "n", "q", "h", "r", "e", "z", "g", "t", "z"],
#     ["e", "v", "m", "h", "t", "r", "x", "e", "k", "y", "m", "a"],
#     ["i", "a", "c", "a", "u", "a", "l", "l", "y", "a", "c", "x"],
#     ["m", "v", "c", "n", "d", "u", "a", "m", "d", "t", "l", "u"],
#     ["q", "t", "i", "t", "w", "a", "a", "a", "u", "p", "r", "x"],
#     ["p", "e", "m", "a", "d", "a", "m", "l", "l", "y", "w", "p"],
#     ["o", "y", "h", "t", "e", "e", "l", "u", "f", "p", "q", "n"],
#     ["p", "a", "c", "t", "u", "a", "l", "l", "y", "u", "r", "e"]
# ]
# result = word_counter(matrix, word)
# print(result, result == 3)

# word = "python"
# matrix = [
#   ["r", "u", "b", "y"],
#   ["r", "u", "b", "y"],
#   ["r", "u", "b", "y"],
#   ["r", "u", "b", "y"],
# ]

# result = word_counter(matrix, word)
# print(result, result == 0)
