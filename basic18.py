# wap to test if the passed letter if vowel or not

def check_if_vowel(letter):
    all_vowel = 'aeiou'
    for v in all_vowel:
        if v in letter:
            return 'its a vowel'
        return 'its not'

print(check_if_vowel('a'))


