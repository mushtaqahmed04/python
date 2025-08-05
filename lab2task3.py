

# create a input variable

age = int(input("enter age : "))

# use conditional statement

if age <= 0 and age < 2:
    print("it a baby")
elif age == 4 and age < 13:
    print("it a kid")
elif age <= 13 and age < 20:
    print("it a teenager")
elif age <= 20 and age < 65:
    print("it a adult")
elif age >= 60:
    print("the person is elder")
else :
    print("invaild")
