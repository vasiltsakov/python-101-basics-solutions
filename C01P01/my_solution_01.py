# This is my solution

def iban_formatter(iban):
    iban = iban.replace(' ','')
    str_list = []
    for num in range(0,22,4):
        str_list.append(iban[num:num+4])
    return ' '.join(str_list)

print(iban_formatter("BG80BNBG96611020345678"))
print(iban_formatter("BG80 BNBG 9661 1020 3456 78"))
print(iban_formatter("BG14TTBB94005362446381"))
print(iban_formatter("BG91UNCR70001864961754"))


# iban_formatter("BG80BNBG96611020345678") == "BG80 BNBG 9661 1020 3456 78"
# iban_formatter("BG80 BNBG 9661 1020 3456 78") == "BG80 BNBG 9661 1020 3456 78"
# iban_formatter("BG14TTBB94005362446381") == "BG14 TTBB 9400 5362 4463 81"
# iban_formatter("BG91UNCR70001864961754") == "BG91 UNCR 7000 1864 9617 54"
