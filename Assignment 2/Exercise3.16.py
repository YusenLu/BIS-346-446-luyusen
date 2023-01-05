# Exersice 3.16
a=[]
b=[]
c=[0]
for i in range(10):
    b=int(input("Enter a number(up to ten):"))
    a.append(b)
max1=max(a)

for i in range(10):
    if a[i]==max1:
        a[i]=min(a)
max2=max(a)

print('The two largest values are',max1,'and',max2)