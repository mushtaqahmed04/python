# age = int(input("Enter a number"))

# # print("elder") if age == 18 else print("older")

# age = ("Yes","No") [age ==18]

# print (age)

# a = 30
# b = 50

# print (not True)
# print (not( a > b ))

# var1 = True
# var2 = False

# print (not True)
# print ("print", var1 or var2)


# a = "first"
# b = "second"
# print(a[-2:-1])
# print(b[:-5])
# print(a.count("fi"))

# name = input("Enter a name : ")
# lenght =len(name)
# print(lenght)

# age = int (input("Enter a number : "))
# if (age%2==0):
#     print("even")
# elif (age%2==1):
#     print("odd")

# age = int (input("Enter a number : "))
# if (age%7==0):
#     print("7")
# else :
#     print("not")


a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))

if (a > b and a > c):
    print ("a is greater")
elif (b > a and b > c):
    print("b is greater")
elif (c > b and c > a):
    print("c is greater")