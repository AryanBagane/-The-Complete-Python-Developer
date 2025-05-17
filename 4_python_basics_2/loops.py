for items in [1,2,3,4,5]:
    for x in ['a', 'b', 'c']:
        print(items, x)

# iterable -> list, dict, tuple, set, string
# iterate -> one by one check each item in the collection

user = {
    "name": "Aryan",
    "age": 69,
    "can_swim": True
}

for x in user.items():
    print(x)

for k, v in user.items():
    print(k, v)

for x in user.keys():
    print(x)

for x in user.values():
    print(x)

# example of counter
my_list = [1,2,3,4,5,6,7,8,9,10]

counter = 0

for x in my_list:
    counter += x
    print(x, counter)
