def anagrams(word1, word2):
    
    word1_fit = word1.replace(' ', '').lower()
    word2_fit = word2.replace(' ', '').lower()


    list_word1 = list(word1_fit)
    list_word2 = list(word2_fit)

    list_word1.sort()
    list_word2.sort()

    return list_word1 == list_word2



tests = [
    ("listen", "silent", True),
    ("LISTEN", "silent", True),
    ("python", "ruby", False),
    ("New York Times", "monkeys write", True),
    ("snake", "sssnakee", False),
    ("a gentleman", "elegant man", True),
    ("eleven plus two", "twelve plus one", True),
    ("William Shakespeare", "I am a weakish speller", True),
    ("", "", True)
    ]

for word1, word2, expected in tests:
    result = anagrams(word1, word2)

    print(result, result == expected)