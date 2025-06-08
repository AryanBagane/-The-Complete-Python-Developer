# Positional parameters
def say_hello(name, age):
    print(f"Hello my name is {name}. My age is {age}.")

# Positional arguments
say_hello("Aryan", 24)

# Keyword arguments
say_hello(name="Aditya", age=19)


# Default parameters
def hello(name="AB", age=69):
    print(f"Hello my name is {name}. My age is {age}.")

hello()