#Midterm2022.py

def exchange(amount):
    UK_currency=round(0.84*amount,2)
    EU_currency=round(0.95*amount,2)
    CA_currency=round(1.36*amount,2)
    print(f'The dollar amount you want to convert is {amount}\n')
    print(f'{"Currency"}{"Amount":>25}')
    print(f'{"British Pound"}{UK_currency:>20}')
    print(f'{"Euro"}{EU_currency:>28}')
    print(f'{"Canadian Dollar"}{CA_currency:>18}')
    
amount=int(input('Please enter the amount of dollar you want to convert:'))
exchange(amount)
