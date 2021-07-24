import copy

def in_range(x, y, matrix):
    min_x = 0
    max_x = len(matrix)
    min_y = 0
    max_y = len(matrix[0])

    if_range = x >= min_x and x < max_x and y >= min_y and y < max_y

    return if_range


def bombing(coordinates, matrix):

    new_matrix = copy.deepcopy(matrix)

    x, y = coordinates

    bombing_coord = [
        (x - 1,y - 1),
        (x - 1,y),
        (x - 1,y + 1),
        (x,y - 1),
        (x,y + 1),
        (x + 1,y - 1),
        (x + 1,y),
        (x + 1,y + 1)
        ]

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

    for i, row in enumerate(m):
        for k, col in enumerate(row):

            temp_matrix = bombing((i,k), m)

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

actual = matrix_bombing_plan(matrix)
print(expected == actual)