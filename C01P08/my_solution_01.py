def group(items):
    result = []
    group_list = []

    for i in range(len(items)):
        if i == len(items) - 1:
            group_list.append(items[i])
            result.append(group_list)
        else:
            group_list.append(items[i])
            if items[i] == items[i+1]:
                continue
            else:
                result.append(group_list)
                group_list = []
    return result


tests = [
    ([1, 1, 1, 2, 3, 1, 1], [[1, 1, 1], [2], [3], [1, 1]]),
    ([1, 2, 1, 2, 3, 3], [[1], [2], [1], [2], [3, 3]]),
    ([], []),
    ([1], [[1]]),
    ([1, 1, 1, 1], [[1, 1, 1, 1]])
    ]

for test, expected in tests:
    result = group(test)
    print(result, result == expected)