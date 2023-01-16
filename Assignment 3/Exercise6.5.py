#Exercise 6.5
text = str.lower(input('Enter a sentence:'))

word_count={}
# You never list and count the words    -5
for word in text.split():
    if word.isalpha():
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
print(f'{"WORD":<12}COUNT')

for word,count in sorted(word_count.items()):
    if count>1:
        print(f'{word:<12}{count}')


