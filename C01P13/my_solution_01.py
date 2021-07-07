def is_prime_number(n):
    
    if n > 1:
        for num in range(2, n):
            if n % num == 0:
                return False
        return True

def next_prime_number(num):
    num += 1
    while not is_prime_number(num):
        num += 1

    return num

def prime_factorization(n):
    result = []
    prime_num = 2

    if is_prime_number(n):
        return [(n, 1)]

    count = 0

    while n != 1:
        while n % prime_num == 0:
            count += 1
            n /= prime_num

        if count > 0:
            result.append((prime_num, count))

        count = 0
        prime_num = next_prime_number(prime_num)

    return result

tests = [
    (10, [(2, 1), (5, 1)]),
    (14, [(2, 1), (7, 1)]),
    (356, [(2, 2), (89, 1)]),
    (89, [(89, 1)]),
    (1000, [(2, 3), (5, 3)])
    ]

for test, expected in tests:
    result = prime_factorization(test)

    print(result, result == expected)