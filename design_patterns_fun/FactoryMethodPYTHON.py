from random import choice
# I ignore interfaces, just implementation

class Dog():
    def speak(self):
        return "Woof!"

class Cat():
    def speak(self):
        return "Meow!"

class DogFactory():
    def create_animal(self):
        return Dog()

class CatFactory():
    def create_animal(self):
        return Cat()

class AnimalLocalFactory():
    _a_dog = None
    def create_animal(self):
        if not AnimalLocalFactory._a_dog:
            AnimalLocalFactory._a_dog = True
            return Dog()
        else:
            return Cat()    

# Usage
if __name__ == "__main__":
    dog_factory = DogFactory()
    dog = dog_factory.create_animal()
    print(dog.speak())  

    cat_factory = CatFactory()
    cat = cat_factory.create_animal()
    print(cat.speak())  
    ALF = AnimalLocalFactory()
    #btw: interface may disable factory to speak :)
    #also: different factories may differently create unit!
    x = ALF.create_animal().speak() 
    y = ALF.create_animal().speak()
    print(x, y)
    