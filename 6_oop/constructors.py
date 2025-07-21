#OOP

class PlayerCharacter:
    membership = True # class object attribute (static)
    def __init__(self, name, age):
        if self.membership:
            self.name = name  # attributes (dynamic)
            self.age = age

    def run(self):
        print(f"my name is {self.name}")
        return 96
    
player1 = PlayerCharacter("Aditya", 69)

print(player1.run())
print(player1.name)
print(player1.age)
# help(player1.age)