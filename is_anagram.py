

def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)       
        


assert is_anagram('abba', 'baab') == True
assert is_anagram('abba', 'bbaa') == True
assert is_anagram('abba', 'abbba') == False
assert is_anagram('abba', 'abca') == False
