count = 0 
while True:

    username = input("Username: ") 
    password = input("Password: ")
    count = count + 1
    if count == 2: 
        print("Login Attempt Over")
        break
    
    else:
        if username == 'user' and password == 'ssuet':
            print("Welcome")
            break
        else:
            print("User Not Found")
