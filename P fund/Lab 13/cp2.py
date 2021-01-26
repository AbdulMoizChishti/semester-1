def main():
# Open file for output
    outfile=open('E:\\python3.txt','x')
# Write data to the file
    outfile.write("var, account_balance, client_name")
    outfile.write("var = 1\n account_balance = 1000.0\nclient_name = 'John Doe'") 
    print(outfile)
    # Close the output file
    outfile.close()  
main()
