# write a python script that take a user input and to create a multiplication table from (1 to 10)
# of that number

# create a input variable

table = int(input("Enter a number : "))

# use loop for iteration

for i in range(1,11):
   
    print(table,"*",i,"=", table*i)