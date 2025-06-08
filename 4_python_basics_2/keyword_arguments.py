# *args takes as much as arguments you take
# Rule: params, *args, default parameters, **kwargs

def super_func(*args, **kwargs):
    print(kwargs) # dict format
    total = 0
    for items in kwargs.values():
        total += items
    print(args) # tuple format
    return sum(args) + total

print(super_func(1,2,3,4,5, num1 = 5, num2 = 10))