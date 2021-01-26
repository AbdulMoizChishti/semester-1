def main():
# Open file for output
    outfile=open('E:\\python.txt','w')
# Write data to the file
    outfile.write("Bill Clinton\n")
    outfile.write("George Bush\n")
    outfile.write("Barack Obama") 
    print(outfile)
    # Close the output file
    outfile.close()  
main()
