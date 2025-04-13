# Dictionary -> it is an unordered value pair
Dictionary = {
    'a':69,
    'b':"Aryan",
    'c':[1,3,5,7],
    'd':True
}
print(Dictionary['b'])
print(Dictionary['c'][3])

my_list = [
    {
    'a':69,
    'b':"Aryan",
    'c':[1,3,5,7],
    'd':True
},
{
    'a':9,
    'b':"Adu",
    'c':[2,4,6,8],
    'd':False
}
]
print(my_list[1]['c'][2])

# dictionary keys -> they should be immutable
user = {
    "name": "Aryan",
    "dates": [2,3,4,6]
}
print(user["name"])
print(user.get("dates"))
print(user.get("age", 69))
print(user.get("status"))   # to avoid errors

# other way to creare a dictionary
user2 = dict(name = "Aditya", age = 45)
print(user2)

# dict methods
print("name" in user.keys())
print("name" in user.keys())
print(user.items())
print(user.clear())
print(user)

user3 = user2.copy()
print(user3)

print(user2.pop("age"))   # pop shows which item is removed
print(user2)

user4 = dict(name = "Piyush", age = 45)

print(user4.popitem())   # removes last item from dict
print(user4)

print(user4.update({"name":"asdfgh","naav":"vishwa"}))   # if there is no key in dict and added new here then it gets added
print(user4)
