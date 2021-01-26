from random import randint
alp=['A','B','C','D','E']
a={}
b=0
list1=[randint(1,50) for i in range(5)]

for i in alp:
    a[i]=list1[b]
    b+=1
    
print(a)