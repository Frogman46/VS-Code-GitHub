#Data Types

#String: In Python, a string is a sequence of characters enclosed within quotation marks (either single quotes or double quotes).
#Concatenation: Concatenation is the process of combining two or more strings together. In Python, concatenation is typically done using the + operator.
#Concatenation can only be done for a string and not for a integer 

#Subscript: It is a process in which you can pull a letter from a word or a number.
# Always start counting from 0. When you program, you always program in binary and space given is also counted as number.
#Example of a Subscript
print("Hello"[1])

#Integer: In Python, an integer is a whole number (positive, negative, or zero) that is not a decimal or a fraction.
#Large Integer: To denote comma in a integer we use "_" instead of "," to improve readability
num = 10_000
print(num)

#Flot: In Python, a float is a numerical data type used to represent decimal numbers with a fractional component.
x = 3.14
print(x)

#Boolean: In Python, a Boolean is a data type that can have one of two values: True or False.
True
False

x = True
y = False

print(x)  
print(y) 

z = 10 > 5
print(z)
  
w = 5 == 7
print(w)


#No, the len() function in Python is used to find the length of a sequence, such as a string, 
# list, tuple, or set. It does not make sense to use len() on an integer because an integer is 
# not a sequence and does not have a length.
# If you try to pass an integer to the len() function, you will get a TypeError:


num_char = len(input("What is your name? "))
print("Your name has " + num_char + " characters")

#type: In Python, type is a built-in function that returns the data type of a given object or variable
print(type(num_char))


#Mathematics

3 + 2
7 - 4
3 * 2
6 / 3
2 ** 3 
# ** is used to denote raise to the power off. example 2 to the power of 3 is 8 (Exponents)
print(6 / 3)
print(type(6 / 3))

# PEMDAS Rule
# Parentheses ()
# Exponents **
# Multiplication *
# Division / 
# Addition +
# Subcription -

print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)



