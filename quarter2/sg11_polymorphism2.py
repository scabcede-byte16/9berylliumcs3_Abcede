""" Answer the following questions:
a. What is duck typing, as explained in the video?
- Duck typing is another way of polyphormism without inheritance. An object can be considered a certain 
type if it has the methods and properties that should be expected.

b. What did the Car class need to have so it could work inside the same loop as Dog and
Cat, even if it does not inherit from the Animal class?
- The car class only needed to have a speak method to be able to work inside the same loop as the dog and cat classes. """

class Car:
    def move(self):
        print("The car drives on the road")

class Boat:
    def move(self):
        print("The boat sails on water")

class Drone:
    def move(self):
        print("The drone flies in the sky")

def star_trip(vehicle):
     vehicle.move()

car1 = Car()
boat1 = Boat()
drone1 = Drone()

star_trip(car1)
star_trip(boat1)
star_trip(drone1)

""" How does the code in 2.2 demonstrate polymorphism?
- The code demonstrates polymorphism by using the same method which is move()
for all of the classes."""
