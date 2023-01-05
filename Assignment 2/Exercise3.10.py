# Exersice 3.10

p=1000
r=0.07
for i in range(1,31):
    a=round(p*(1+r)**i,2)
    print(f'Deposit at the end of {i} year will be {a}' )