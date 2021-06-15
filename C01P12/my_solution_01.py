def is_credit_card_valid(number):
    
    list_num = []
    len_num = len(str(number))

    while number != 0:
        list_num.append(number % 10)
        number = number // 10


    for num in range(1, len_num+1):
        if num % 2 == 0:
            list_num[num-1] = list_num[num-1] * 2
            if list_num[num-1] > 9:
                list_num[num-1] = list_num[num-1] % 10 + 1

    return sum(list_num) % 10 == 0

tests = [
    (79927398713, True),
    (4417123456789113, True),
    (4242424242424242, True),
    (79927398715, False),
    (79927398710, False),
    (79927398711, False),
    (79927398712, False),
    (79927398714, False),
    (79927398715, False),
    (79927398716, False),
    (79927398717, False),
    (79927398718, False),
    (79927398719, False)
    ]

for test, expected in tests:
    result = is_credit_card_valid(test)

    print(result == expected)