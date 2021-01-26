groceries={'rice':3,'wheat':6,'oil':9,'eggs':12,'bread':15}


def calculate_bill():
    total=0
    count=0
    while count!=3:
        i=input("Enter food/ groceries:")
        for i,price in groceries.items():
        
            total +=1
            print(i, "",price)
        count+=1
        
calculate_bill()