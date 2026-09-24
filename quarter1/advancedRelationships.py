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

print("--- BEFORE ---")
object1.displayInfo()
object2.displayInfo()
object3.displayInfo()

print("Updating Points of object 1...")

print("--- AFTER ---")
object1.displayInfo()
object2.displayInfo()
object3.displayInfo()

class UAAPWomensVolleyballAthletes(FilipinoUAAPWomensVolleyball):
    def __init__(self, Length, Available, Points, Name, AthleteName, Position, TeamName, Status):
        super().__init__(Length, Available, Points, Name)
        self.AthleteName = AthleteName
        self.Position = Position
        self.team = TeamName
        self.status = Status

    def displayAthleteInfo(self):
        print(f"Athlete Name: {self.AthleteName}, Position: {self.Position}, Team: {self.team}, Status: {self.status}")

    def updateStatus(self, new_status):
        self.status = new_status
        print(f"Updated Status: {self.status}")

    def displayTeam(self):
        print(f"Team: {self.team}")

    def displayAthleteName(self):
        print(f"Athlete Name: {self.AthleteName}")

    def displayPosition(self):
        print(f"Position: {self.Position}")

object4 = UAAPWomensVolleyballAthletes("1 Hour and 30 minutes", "Available", "3-1", "UST Golden Tigresses vs. FEU Lady Tamaraws", "Maria Cassandra Rae Carballo", "Setter", "UST Golden Tigresses", "Active")
object5 = UAAPWomensVolleyballAthletes("1 Hour", "Not Available", "4-0", "DLSU Lady Spikers vs. Ateneo Lady Eagles", "Angel Anne Canino", "Outside Hitter", "DLSU Lady Spikers", "Active")
object6 = UAAPWomensVolleyballAthletes("1 Hour and 45 minutes", "Available", "3-0", "UP Fighting Maroons vs. Adamson Lady Falcons", "Niña Ytang", "Middle Blocker", "UP Fighting Maroons", "Inactive")

print("--- BEFORE ---")
object4.displayAthleteInfo()
object5.displayAthleteInfo()
object6.displayAthleteInfo()

print("Updating Status of object 4...")

print("--- AFTER ---")
object4.displayAthleteInfo()
object5.displayAthleteInfo()
object6.displayAthleteInfo()