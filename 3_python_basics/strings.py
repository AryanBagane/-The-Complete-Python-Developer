a = "Hello Aryan"
print(type(a))

long_string = """
WOW
0 0
___
"""
print(long_string)

fname = "Aryan"
lname = "Bagane"
fullname = fname + " " + lname
print(fullname)

# string concatenation
print("Aditya" + " Bagane")

# type conversion
print(type(str(100)))
print(type(int(str(100))))

# escape sequences
# \ -> after this we can use any string
# \t -> tab spacing
# \n -> new line
weather = "\tit\'s too \n\"SUNNY\"."
print(weather)

# formatted strings
name = "Aryan"
age = 69
print(f"My name is {name}. My age is {age}")

# string manipulation
selfish = "me me me"
         # 01234567
print(selfish[4])

manu = "012345678"
# [start:stop:stepover]
print(manu[0:9:3])
print(manu[1:])
print(manu[:5])
print(manu[::3])
print(manu[-2])
print(manu[::-1])
print(manu[::-2])

# Immutability -> Strings in python are Immutabale, they cannot be changed, but we can reassign.
manu = manu + "9"
print(manu)

# bultin functions and methods
print(len("aryan"))

quote = "to be or not to be"
print(quote.upper())
print(quote.lower())
print(quote.capitalize())
print(quote.find("be"))   # finds the word at which index it is situated
print(quote.replace("be", "me"))
