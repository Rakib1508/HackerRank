import re

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
checker = '(?<=[' + consonants + '])([' + vowels + ']{2,})[' + consonants + ']'

case = re.findall(checker, input().strip(), re.IGNORECASE)
if case:
    print(*case, sep='\n')
else:
    print('-1')
