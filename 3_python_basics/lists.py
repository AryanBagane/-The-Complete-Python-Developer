# Lists -> list are collection of objects
li = [1,2,3,4,5]
li2 = ["a", "d", "c"]
li3 = [1,2,"a","d",4,5]
print(li[1])

# list slicing
print(li3[0:3])

# list are mutable they can be changed
li2[1] = "b"
print(li2)

# matrix -> matrix is nothing but multidimensional array
matrix = [
    [2,4,5],
    [2,3,6],
    [0,1,0]
]
print(matrix[0][1])

# list methods
basket = [1,2,3,4,5]

# adding
basket.append(69)
print(basket)

basket.insert(2, 34)
print(basket)

basket.extend([23])
print(basket)

# removing
basket.pop()
print(basket)

basket.pop(1)   # we give index we want to remove
print(basket)

basket.remove(4)   # we give value we want to remove
print(basket)

a = [1,2,3,4]
a.clear()   # clears all the list
print(a)

nums = [1,2,3,4,5,6]
print(nums.index(3))   # asks for the index of given value

alpha = ['a','b','c','x','f']
print('b' in alpha)
print(alpha.count('c'))

# sorting
print(sorted(alpha))
alpha.sort()
print(alpha)

# copying
copy_list = alpha.copy()
print(copy_list)

# reversing
copy_list.reverse()
print(copy_list)

alphabet = ['a','b','c','x','f','f']
alphabet.sort()
alphabet.reverse()
print(alphabet[::-1])
print(alphabet)

# create a ist from 1 to 100
print(list(range(1, 101)))

# .join method
new_sen = ' '.join(['hi', 'Atharv'])
print(new_sen)

# list unpacking
a,b,*other,d = [1,2,3,4,5,6,7,8,9] 
print(a)
print(b)
print(other)
print(d)

# None
weapons = None
print(weapons)