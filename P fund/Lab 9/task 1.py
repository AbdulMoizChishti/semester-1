list = [1, 3, 5, 7, 9] #list of odd numbers
print(list) 
element = int(input("Enter Any number from the above list :")) #selection of number 
length = len(list)

def search(list , length, element): # to search the entered number in the list
    for i in range(0, length):
        if (list[i] == element):
            return i
    return 0

result = search(list, length, element) 

if(result == 0):
    print("Not found in the above list") 
else:
    print("found at index", result) 