def nan_expand(times):
    if times == 0:
        return ""

    parts = ["Not a"] * times
    parts.append("NaN")

    return ' '.join(parts)


tests = [
    (0, ""),
    (1, "Not a NaN"),
    (2, "Not a Not a NaN"),
    (3, "Not a Not a Not a NaN")
]

for times, expected in tests:
    result = nan_expand(times)

    print(result == expected)