groceries={'rice':3,'wheat':6,'oil':9,'eggs':12,'bread':15}
def calculate_bill():
     total=0
     count=0

     key_list = list(groceries.keys())
     val_list = list(groceries.values())
     choice= input("Enter the food:")
     price = key_list.index(choice)

     a=val_list[price]
     total= total+a
     print("Price of ",choice,"=",total)
calculate_bill()
def calculate_bil():
     print("")
     total=sum(groceries.values())
     print("Total sum of old list =",total,"\n")
     if total >20:
         groceries["milk"]=300
         groceries["salt"]=100
         groceries["sugar"]=200


         del groceries["rice"]
         del groceries["wheat"]
         print("New list=",groceries)
         total=sum(groceries.values())
         print("\nTotal Sum of new list =",total)
calculate_bil()
