from collections import Counter

def is_anagram(s1,s2):
    return Counter(s1) == Counter(s2)
s1 = "listen"
s2 = "silent"
print(is_anagram(s1,s2))  