#Exercise 5.15
invoices=[('83','Electric sander',7,57.98),
          ('24','Power saw',18,99.99),
          ('7','Sledge hammer',11,21.50),
          ('77','Hammer',76,11.99),
          ('39','Jig saw',3,79.50)]
from operator import itemgetter
#a
for a,b,c,d in sorted(invoices,key=itemgetter(1)):
    print(f'{a:<5}{b:<15}{c:>5}{d:10}')
#b
for a,b,c,d in sorted(invoices,key=itemgetter(3)):
    print(f'{a:<5}{b:<15}{c:>5}{d:10}')
#c
get_quantity=itemgetter(2)
get_description=itemgetter(1)
quantity=[get_quantity(temp)for temp in invoices]
description=[get_description(temp)for temp in invoices]
description_quantity=list(zip(description,quantity))
for a,b in sorted(description_quantity,key=itemgetter(1)):
    print(f'{a:<20}{b}')
#d
description_value=[(temp[1],round(temp[2]*temp[3],2))for temp in invoices]
for a,b in sorted(description_value,key=itemgetter(1)):
    print(f'{a:<20}{b}')
#e
invoice_value=[temp  for temp in description_value
               if 200<=temp[1]<=500]
for a,b in sorted(invoice_value,key=itemgetter(1)):
    print(f'{a:<20}{b}')
#f
total=sum(temp[1] for temp in description_value )
print('The total of the invoices is:',total)

