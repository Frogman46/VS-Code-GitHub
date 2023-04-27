#type: In Python, type is a built-in function that returns the data type of a given object or variable

num_char = len(input("What is your name? "))
#print("Your name has " + num_char + " characters")  ERROR 404- Integers cannot be directly concatenated, you need to add (str) for an integer.
print(type(num_char))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters")


a = str(123)
b = float(1.23)

print(type(a))
print(type(b))



