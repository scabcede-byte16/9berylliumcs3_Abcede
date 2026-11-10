#code ni abcede sofiya
class Animal: # This is the parent/super class
    def __init__(self, name): # This is the name attribute of the class
        self.name = name
        
    def eat(self): #This is the method of the parent class that represents an eating animal
        print(f"{self.name} is eating.")
    def make_sound(self): #This method represents an animal making a sound
        print(f"{self.name} makes a sound.") 
        
class Lion(Animal): # This is the child/subclass of Animal
    def make_sound(self): # This method overrides the initial make_sound method from the parent class
        print(f"{self.name} roars loudly!") # This replaces the "makes a sound" with roars loudly for the animal class
    def eat(self): # This method overrides the initial eat method from the parent class
        print(f"{self.name} eats fresh meat.") # This replaces the "is eating" with eats fresh meat for the animal class
class Elephant(Animal): # This is another child/subclass of Animal
    def make_sound(self):
        print(f"{self.name} trumpets!") # This replaces the "makes a sound" with a specific sound for this animal class
    def eat(self): 
        print(f"{self.name} eats grass and fruits.") # This replaces the "is eating" with a specific food for the animal class

class Monkey(Animal): # This is another child/subclass of Animal
    def make_sound(self): 
        print(f"{self.name} chatters!") # This replaces the "makes a sound" with a specific sound for this animal class
    def eat(self): 
        print(f"{self.name} eats bananas.") # This replaces the "is eating" with a specific food for the animal class

lion = Lion("Simba") # This gives a name to the lion subclass which is "Simba"
elephant = Elephant("Dumbo") # This gives a name to the elephant subclass which is "Dumbo"
monkey = Monkey("George") # This gives a name to the monkey subclass which is "George"

lion.make_sound() # This calls the make_sound method from the lion subclass
lion.eat() # This calls the eat method from the lion subclass
print("-----")
elephant.make_sound() # This calls the make_sound method from the elephant subclass
elephant.eat() # This calls the eat method from the elephant subclass
print("-----")
monkey.make_sound() # This calls the make_sound method from the monkey subclass
monkey.eat() # This calls the eat method from the monkey subclass
print("-----")
