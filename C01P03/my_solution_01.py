def fact_digits(n):
    n_str = str(n)
    result = 0

    for num in n_str:
        fact = 1
        for i in range(1, int(num) + 1):
            fact *= i
        result += fact
        fact = 1
    return result



tests = [
    (101, 3),
    (111, 3),
    (145, 145),
    (999, 1088640)
]

for n, expected in tests:
    result = fact_digits(n)

    print(result == expected)