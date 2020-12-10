vowels = ('AEIOU')

def minion_game(string):
    stuart_score = 0
    kevin_score = 0
    string_length = len(string)
    
    for i in range(string_length):
        if string[i] in vowels:
            kevin_score += (string_length - i)
        else:
            stuart_score += (string_length - i)
    
    if stuart_score > kevin_score:
        print('Stuart', stuart_score)
    elif stuart_score < kevin_score:
        print('Kevin', kevin_score)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
