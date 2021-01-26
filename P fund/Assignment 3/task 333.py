# defining a dictionary with key and values
electronics = {'Tv':1,'Laptop':2,'Camera':3,'Camcorder':4,'SmartPhone':5,'Speakers':6,'fridge':7 ,'Air conditioner':8}
# defining a function 
def calculate_bil():
    total=0    
    key_list = list(electronics.keys())
    val_list = list(electronics.values())

    print("")
    total=sum(electronics.values())
    print("Total sum of old list =",total,"\n")
    a= electronics.popitem()#removing the last item
    total=sum(electronics.values())
    print("\nTotal Sum of new list =",total)
calculate_bil()