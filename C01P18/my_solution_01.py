import copy

def in_range(x, y, matrix):
    min_x = 0
    max_x = len(matrix)
    min_y = 0
    max_y = len(matrix[0])

    if_range = x >= min_x and x < max_x and y >= min_y and y < max_y

    return if_range


def template(coordinates,matrix):
    
    x, y = coordinates

    x1 = x - 1
    y1 = y - 1

    x2 = x - 1
    y2 = y

    x3 = x - 1
    y3 = y + 1

    x4 = x
    y4 = y - 1

    x5 = x
    y5 = y + 1

    x6 = x + 1
    y6 = y - 1

    x7 = x + 1
    y7 = y

    x8 = x + 1
    y8 = y + 1

    bombing_coord = [
        (x1,y1),
        (x2,y2),
        (x3,y3),
        (x4,y4),
        (x5,y5),
        (x6,y6),
        (x7,y7),
        (x8,y8)
        ]

    return bombing_coord


def bombing(coordinates, matrix):

    new_matrix = copy.deepcopy(matrix)

    bombing_coord = template(coordinates, matrix)

    x, y = coordinates

    value_point = matrix[x][y]

    for point in bombing_coord:
        x, y = point
        if in_range(x,y,matrix):
            new_matrix[x][y] = new_matrix[x][y] - value_point
            if new_matrix[x][y] < 0:
                new_matrix[x][y] = 0

    return new_matrix

def sum_of_matrix(matrix):
    result = 0
    for x in matrix:
        for y in x:
            result += y

    return result

def matrix_bombing_plan(m):
    result = {}

    for i, row in enumerate(matrix):
        for k, col in enumerate(row):

            temp_matrix = bombing((i,k), matrix)

            result[(i,k)] = sum_of_matrix(temp_matrix)

    return result

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

expected = {
    (0, 0): 42,
    (0, 1): 36,
    (0, 2): 37,
    (1, 0): 30,
    (1, 1): 15,
    (1, 2): 23,
    (2, 0): 29,
    (2, 1): 15,
    (2, 2): 26
    }

result = matrix_bombing_plan(matrix)
print(result == expected)