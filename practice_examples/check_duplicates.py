some_list = ['a','a','b','c']

duplicates = []
for dup in some_list:
    if some_list.count(dup) > 1:
        if dup not in duplicates:
            duplicates.append(dup)

print(duplicates)