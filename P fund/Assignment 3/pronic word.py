# ch='false'
n=int(input("enter number:"))
for i in range(1,n+1):
    if i*(i+1)==n:
#         ch ='true'
        break
if (ch==n):
    print('pronic')
else:
    print('not pronic')