string1 = input("Enter a string: ")

reverese_string = string1[::-1]
print("Reversed string is: ", reverese_string)

if reverese_string == string1:
    print("String is palindrome")
else:
    print("String is not palindrome")