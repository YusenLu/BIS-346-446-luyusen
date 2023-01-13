#Exercise 6.8
#method 1
hunreds=["one","two","three","four","five",
                   "six","seven","eight","nine"]

teen=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen',
      'seventeen','eighteen','nineteen']

ty=['twenty','thirty','forty','fifty','sixty',
              'seventy','eighty','ninety']

check=float(input('Please enter the amount of the check(less than 1000):'))

if check > 100 :
    for i in range(len(hunreds)):
        if i==(check//100)-1:
            print(f'{str.upper(hunreds[i])} HUNRED',end=' ')

for j in range(len(teen)):
    if 10 <= (check%100) < 20:
        if j==int(((check%100)%10)):
            print(f'{str.upper(teen[j])}',end=' ')
    elif (check%100) >= 20:
        if j==int(((check%100)//10))-2:
            print(f'{str.upper(ty[j])}',end=' ')
            for k in range(len(hunreds)):
                if k==int((check%10))-1:
                    print(f'{str.upper(hunreds[k])}',end=' ')
    elif (check%100) < 10:
        if j==int((check%10))-1:
            print(f'{str.upper(hunreds[j])}',end=' ')

print(f'AND {int(round((check%1),2)*100)}/100')


#method 2
number_to_word = {
    0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 
    5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE',
    10: 'TEN', 11: 'ELEVEN', 12: 'TWELVE', 13: 'THIRTEEN', 
    14: 'FOURTEEN', 15: 'FIFTEEN', 16: 'SIXTEEN', 17: 'SEVENTEEN', 
    18: 'EIGHTEEN', 19: 'NINETEEN', 20: 'TWENTY', 30: 'THIRTY', 
    40: 'FORTY', 50: 'FIFTY', 60: 'SIXTY', 70: 'SEVENTY', 
    80: 'EIGHTY', 90: 'NINETY'
}

amount = input('Please enter the amount of the check(less than 1000): ')
dollars, cents = amount.split('.')
dollars = int(dollars)
cents = int(cents)
amount_in_words = []

if dollars == 0:
    amount_in_words.append(number_to_word[dollars])
elif dollars >= 100:
    amount_in_words.append(number_to_word[dollars // 100] + ' HUNDRED')

dollars %= 100 

if dollars in range(10, 20):
    amount_in_words.append(number_to_word[dollars])
elif dollars in range(20, 100):
    amount_in_words.append(number_to_word[dollars // 10 * 10])
    dollars %= 10 

if dollars in range(1, 10):
    amount_in_words.append(number_to_word[dollars])

print(f'{" ".join(amount_in_words)} AND {cents}/100')          
            


