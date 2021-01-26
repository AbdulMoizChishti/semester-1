import random

a=[random.randrange(1, 50) for i in range(6)]
xyz=["A:"+str(a[0]),"B:"+str(a[1]),"C:"+str(a[2]),"D:"+str(a[3]),"E:"+str(a[4]),"F:"+str(a[5]),]
print(xyz)
odd = 0
even = 0
for j in a:
    if not j % 2:
        even+=1
    else:
        odd+=1

print("number of even numbers :",even)
print("number of odd numbers :",odd)


