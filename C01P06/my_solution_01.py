def nan_expand(times):
    if times == 0:
        return ''
    else:
        txt = ''
        for x in range(times):
            txt += 'Not a '
        return txt + 'NaN'


tests = [
    (0, ""),
    (1, "Not a NaN"),
    (2, "Not a Not a NaN"),
    (3, "Not a Not a Not a NaN")
    ]

for test, expected in tests:
    print(nan_expand(test), nan_expand(test) == expected)