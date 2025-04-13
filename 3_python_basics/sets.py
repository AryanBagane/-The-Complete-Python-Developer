# Sets -> unordered collections of unique objects
# set object does not support indexing
my_set = {2,5,7,3,1,5,4}
print(my_set)   # only returns unique set
print(len(my_set))

# convert a list into unique set
my_list = [2,6,2,2,5,6,3,3,5]
print(set(my_list))

set1 = {1,2,3,5,6}
set2 = {4,5,6,7,8,9}

print(set1.difference(set2))

print(set2.discard(9))
print(set2)

# print(set1.difference_update(set2))
# print(set1)

# print(set1.intersection(set2))
# also we can use 
# print(set1 & set2)

print(set1.isdisjoint(set2))

print(set1.union(set2))
# also we can use 
print(set1 | set2)

set3 = {5,6}
print(set3.issubset(set2))

print(set2.issuperset(set3))
