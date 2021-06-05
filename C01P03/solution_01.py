def fact(n):
    result = 1

    for x in range(1, n + 1):
        result *= x

    return result


# xyz = x! + y! + z! (x + y + z)
def fact_digits(n):
    n = abs(n)

    result = 0

    while n != 0:
        digit = n % 10
        result += fact(digit)

        n = n // 10

    return result


tests = [
    (5, 120),
    (101, 3),
    (111, 3),
    (145, 145),
    (999, 1088640)
]


for n, expected in tests:
    result = fact_digits(n)

    print(result, result == expected)