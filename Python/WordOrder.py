words = []
word_count = {}
for _ in range(int(input())):
    word = input()
    words.append(word)
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(len(word_count))
string = [str(word_count[item]) for item in word_count]
print(' '.join(string))
