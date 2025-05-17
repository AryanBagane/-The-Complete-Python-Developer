# Logical operators
# In Unicode (and ASCII), uppercase letters come before lowercase letters.
# That means lowercase characters have higher numeric values than uppercase ones, so 'a' is greater than 'A'.
# 'A' → Unicode code point: 65
# 'a' → Unicode code point: 97
print('a' > 'A')

# Example of Wizards
is_magician = True
is_expert = False

if is_magician and is_expert:
    print("Your are a magician")
elif is_magician and not is_expert:
    print("Atleast you are getting there")
elif not is_magician:
    print("You need magic powers")


# is operator -> checks the location in the memory is as same as it 
print(True is True)
print(1 is 1)
print("1" is 1)
print([] is []) # here it is false because everytime we add list then is it stored new list
a = [1,2,3]
b = [1,2,3]
print(a is b) # here false because it is stored in different memory locations