# Store a person’s name, and include some whitespace characters (\t and \n) 
# at the beginning and end. Then print the name once as it is, and then 
# using the three strip functions.


# Store name with whitespace characters
name = "\t\n   John Doe   \n\t"

# Print the name as it is
print("Original name with whitespace:")
print(repr(name))  # repr shows whitespace characters

# Using lstrip()
print("\nUsing lstrip():")
print(repr(name.lstrip()))

# Using rstrip()
print("\nUsing rstrip():")
print(repr(name.rstrip()))

# Using strip()
print("\nUsing strip():")
print(repr(name.strip()))