print("Please enter my last name or my CSU ID: ")
inp = input()
if(inp == "Nguyen" or inp == "nguyen"):
    print("Input " , inp, " is my last name.")
elif(inp.isdigit() and inp == "2729679"):
    print("Input " , inp, " is my CSU ID." )
else:
    print("Input " , inp, " is not valid." )