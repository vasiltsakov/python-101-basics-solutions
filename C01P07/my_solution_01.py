from enum import Enum

class Monotonicity(Enum):
    INCREASING = 1
    DECREASING = 2
    NONE = 3

def increasing_or_decreasing(ns):
    result = 0

    for i,num in enumerate(ns):
        if ns[i] == ns[-1]:
            break
        else:
            if ns[i] < ns[i+1]:
                result += 1
            elif ns[i] > ns[i+1]:
                result -= 1
            else:
                return Monotonicity.NONE

    if result > 0 and result == len(ns) - 1:
        return Monotonicity.INCREASING
    elif result < 0 and abs(result) == len(ns) - 1:
        return Monotonicity.DECREASING
    else:
        return Monotonicity.NONE


tests = [
    ([1, 2, 3, 4, 5], Monotonicity.INCREASING),
    ([5, 6, -10], Monotonicity.NONE),
    ([1, 1, 1, 1], Monotonicity.NONE),
    ([9, 8, 7, 6], Monotonicity.DECREASING),
    ([], Monotonicity.NONE),
    ([1], Monotonicity.NONE),
    ([1, 100], Monotonicity.INCREASING),
    ([1, 100, 100], Monotonicity.NONE),
    ([100, 1], Monotonicity.DECREASING),
    ([100, 1, 1], Monotonicity.NONE),
    ([100, 1, 2], Monotonicity.NONE)
    ]

for test, expected in tests:
    result = increasing_or_decreasing(test)
    print(result == expected)


