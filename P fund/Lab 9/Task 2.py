def common_element(list1, list2):
    result1 = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result 
#For list 1
print(common_element([1,2,3,4,5,6,7,8,9,10], [2,4,6,8,10])) 
#For list 2
print(common_element([2,4,6,8,10], [1,3,5,7,9])) 