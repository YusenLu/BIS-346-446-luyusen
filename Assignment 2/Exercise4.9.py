# Exercise  4.9
F=0
for i in range(102):
    if i !=0:
        F=round(((i-1)*(9/5)+32),1)
        print(f'{i-1:<10}{F:<10}')
    else:
        print(f'{"Celsius":<10}{"Fahrenheit":<10}')

