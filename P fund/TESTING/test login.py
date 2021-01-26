c = 0 
while True: 
    username = input("Username: ") 
    password = input("Password: ")
    c = c + 1
    
    if c == 2:
    break 
    else:
        if userName == 'elmo' and password == 'blue':
            break 
        else:
            print("invalid")