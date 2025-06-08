def highestEven(li):
    evens = []
    for items in li:
        if items % 2 == 0:
            evens.append(items)

    return max(evens)

print(highestEven(li=[1,2,3,5,7,8,4,2,1,2,3,1,2,11,13,28,24]))