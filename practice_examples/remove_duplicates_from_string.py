string1 = input("Enter a string: ")

set1 = set()
string2 = ""

for char in string1:
    if char not in set1:
        set1.add(char)
        string2 = string2 + char
print(string2)
