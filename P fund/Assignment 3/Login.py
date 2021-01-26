cred=["admin","123"]
count = 0 
while True:
    print("*******************LOGIN PAGE**********************")
    username = input("Username: ") 
    password = input("Password: ")
    count = count + 1
    if count == 2: 
        print("Login Attempt Over")
        break
    
    else:
        if username == cred[0] and password == cred[1]:
            print("Welcome\n")
            print("*******************HOME PAGE**********************\n")
            print("**************MENU**************\n")
            print("**************SETTING***********\n")
            print("**************CONTACT US********\n")
            break
        
        else:
            print("\nUser Not Found\n")