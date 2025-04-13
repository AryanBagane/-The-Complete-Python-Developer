# Tuples -> tuples are immutable
my_tuple = (1,2,4,5)
print(7 in my_tuple)
print(len(my_tuple))
print(my_tuple.count(4))
print(my_tuple.index(2))

user = {
    (1,2): "Aryan",
    "dates": [2,3,4,6]
}
print(user[(1,2)])