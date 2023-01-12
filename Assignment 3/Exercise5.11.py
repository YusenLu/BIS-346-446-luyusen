# Exercise5.11
def summarize_letters(string):
    string=str.lower(string)
    l=[]
    n=[]
    for i in string:
        if i.isalpha():
            if i in l:
                n[l.index(i)]+=1
            else:
                l.append(i)
                n.append(1)
    letter_tuple=list(zip(l,n))
    print(letter_tuple)
    return letter_tuple

string=input('Please write some letters here:')
result=summarize_letters(string)
for a,b in result:
    print(f'{a}  {b}')

if len(result)==26:
    print('The string has all letters of the alphabet')
else:
    print("The string doesn't has all letters of the alphabet")    
