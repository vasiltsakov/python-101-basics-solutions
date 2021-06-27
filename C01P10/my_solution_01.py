def palindromes_count(n):
    if n >= 10 and n <= 99999:
        
        count = 0

        for num in range(10, n+1):
            str_num = str(num)

            if str_num == str_num[::-1]:
                count += 1

        return count


tests = [
    (10, 0),
    (20, 1),
    (30, 2),
    (101, 10),
    (200, 19),
    (43539, 525),
    (4247, 132),
    (48877, 577),
    (94012, 1029),
    (62560, 715),
    (92009, 1009),
    (63176, 721),
    (67409, 763),
    (62834, 718),
    (77420, 863),
    (99999, 1089)
    ]

for test, expected in tests:
    result = palindromes_count(test)
    print(result == expected)