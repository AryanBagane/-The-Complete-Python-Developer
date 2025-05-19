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


# range
for i in range(0, 10, 2):   # here 2 is step-over
    print(i)

for x in range(10, 0 ,-1):
    print(x)

# enumrate
for i, char in enumerate("aryan"):
    print(i, char)

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f"index of 50 is {i}")

# while
i = 0
while i < 50:
    print(i)
    i+=1

while True:
    response = input("Say Something: ")
    if response == "bye":
        print("Bye honey.")
        break