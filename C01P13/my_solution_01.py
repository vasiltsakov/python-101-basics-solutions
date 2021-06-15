def prime_number(n):
    
    if n > 1:
        for num in range(2, n):
            if n % num == 0:
                return False
        return True


# Sorry, I didn't find a solution, so I copied this:
def next_prime(n):
    n = n + 1

    while not prime_number(n):
        n = n + 1

    return n


def prime_factorization(n):

    result = []
    p = 2

    if prime_number(n):
        return [(n, 1)]
    else:
        while n != 1:
            a = 0
            while n % p == 0:
                a = a + 1
                n = n // p

            if a > 0:
                result.append((p, a))

            p = next_prime(p)
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