#write a code for inheritence 
class Animal:
    def speak():
        return"Animal is speaking"
class Dog(Animal):
    def Bark():
        return"Bow..."
obj1=Animal
obj2=Dog
print(obj1.speak())
print(obj2.Bark())

