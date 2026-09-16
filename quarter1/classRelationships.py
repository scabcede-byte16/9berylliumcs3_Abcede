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

class UAAPWomensVolleyballAthletes:
    def __init__(self, Athlete, Position, Team, Status):
        self.Athlete = Athlete
        self.Position = Position
        self.Team = Team
        self.Status = Status

        def displayAthleteInfo(self):
            print(f"Athlete: {self.Athlete}, Position: {self.Position}, Team: {self.Team}, Status: {self.Status}")

        def updateStatus(self, new_status):
            self.Status = new_status
            print(f"Updated Status: {self.Status}")

        def displayTeam(self):
            print(f"Athlete: {self.Athlete}, Team: {self.Team}")

        def displayPosition(self):
            print(f"Athlete: {self.Athlete}, Position: {self.Position}")

object4 = UAAPWomensVolleyballAthletes("Maria Cassandra Rae Carballo", "Setter", "UST Golden Tigresses", "Active")
object5 = UAAPWomensVolleyballAthletes("Angel Anne Canino", "Outside Hitter", "DLSU Lady Spikers", "Active")
object6 = UAAPWomensVolleyballAthletes("Shaira Jardio", "Libero", "National University Lady Bulldogs", "Active")

object4.displayAthleteInfo()
object5.displayAthleteInfo()
object6.displayAthleteInfo()

print("--- BEFORE ---")
print("Object 4: displayAthleteInfo")
print("Object 5: displayAthleteInfo")
print("Object 6: displayAthleteInfo")

print("Changing Status of object 4...")

print("--- AFTER ---")
print("Object 4: displayAthleteInfo")
print("Object 5: displayAthleteInfo")
print("Object 6: displayAthleteInfo")