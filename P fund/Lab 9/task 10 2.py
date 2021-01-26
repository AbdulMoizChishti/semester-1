#Program for Guess the capitals by using a dictionary
Guess = {"Pakistan" : "Islamabad","Russia" : "Moscow","Germany" : "Bonn"}
valid=0
invalid=0
for Country , Capital in Guess.items():
     print("\t Give The Capital Of The City = " ,Country)
     ans= input("Write Answer : " )
     if ans == Capital:
         print("*Your Answer Is Correct*" )
         valid=valid+1
         
     else:
         print("*Your Answer Is Invalid*")
         invalid=invalid+1
         
print("corrects: ",valid)
print("In-corrects: ",invalid)