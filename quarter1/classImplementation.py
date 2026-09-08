class FilipinoUAAPWomensVolleyball:
    def __init__(self, Length, Available, Points, Name):
        self.Length = Length
        self.Available = Available
        self.Points = Points
        self.Name = Name

    def displayInfo(self):
        print(f"Length: {self.Length}, Available: {self.Available}, Points: {self.Points}, Name: {self.Name}")

    def updatePoints(self, amount):
        self.Points += amount
        print(f"Updated Points: {self.Points}")

    def displayAvailable(self):
        print(f"Name: {self.Name}, Length: {self.Length}")

    def displayName(self):
        print(f"Name: {self.Name}")

object1 = FilipinoUAAPWomensVolleyball("1 Hour and 30 minutes", "Available", "3-1", "UST Golden Tigresses vs. FEU Lady Tamaraws")
object2 = FilipinoUAAPWomensVolleyball("1 Hour", "Not Available", "4-0", "DLSU Lady Spikers vs. Ateneo Lady Eagles")
object3 = FilipinoUAAPWomensVolleyball("1 Hour and 45 minutes", "Available", "3-0", "UP Fighting Maroons vs. Adamson Lady Falcons")

object1.displayInfo()
object2.displayInfo()
object3.displayInfo()

print("--- BEFORE ---")
print("Object 1: displayInfo")
print("Object 2: displayInfo")
print("Object 3: displayInfo")

print("Changing Name of object 1...")

print("--- AFTER ---")
print("Object 1: displayInfo")
print("Object 2: displayInfo")
print("Object 3: displayInfo")
