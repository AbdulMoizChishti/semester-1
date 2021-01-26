i = 15
a = []
while i > 0:
    num = input("Enter number: ")
    a.append(num)
    i = i-1
print (a)
abc = []
for i in a:
    if i not in abc:
        abc.append(i)
print ("list after removing duplicates : " + str(abc))