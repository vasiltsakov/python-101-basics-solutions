def prime_number(n):
    
    if n > 1:
        for num in range(2, n):
            if n % num == 0:
                return False
        return True


def goldbach(n):
    if n % 2 == 1:
        return None
    else:
        list_primes = []

        for num in range(2, n):
            if prime_number(num):
                list_primes.append(num)

        result = []

        for prime in list_primes:
            for num in list_primes:
                if prime + num == n and (num, prime) not in result:
                    result.append((prime, num))

        return result




tests = [
    (4, [(2,2)]),
    (6, [(3,3)]),
    (8, [(3,5)]),
    (10, [(3,7), (5,5)]),
    (100, [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]),
    (5, None)
    ]

for test, expected in tests:
    result = goldbach(test)
    print(result == expected)