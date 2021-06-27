def sum_matrix(m):
    result = []
    for li in m:
        result += li


    return sum(result)



tests = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 45),
    ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0),
    ([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]], 55)
    ]

for test, result in tests:
    print(sum_matrix(test) == result)