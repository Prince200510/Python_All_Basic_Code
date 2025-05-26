def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

string1 = input('Enter the First String  :')
string2 = input('Enter the Second String :')

result = 'anagrams' if is_anagram(string1, string2) else 'Not anagrams'
print(result)