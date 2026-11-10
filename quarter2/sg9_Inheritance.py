#Code ni sofiya absidy(Abcede
class Publication: # Parent class of dis code
    def __init__(self, title, author): # This is the constructor method na naga initialize ng attributes
        self.title = title #This is the title attribute of the publication
        self.author = author #This is the author attribute of the publication
        
    def display_info(self): #This displays the information in this class
        print(f"Title: {self.title}, Author: {self.author}")

class Book(Publication): # This is a child class of the publication class
    def __init__(self, title, author, number_of_pages): # This is the constructor method that shows the inherited and new attributes of the class
        super().__init__(title, author) # This calls the constructor from the parent class to initialize the inherited attributes
        self.number_of_pages = number_of_pages # This is the new attribute of this class that did now come from the parent class
        
    def display_info(self): # This displays the information of this child class
        super().display_info() # This displays the attributes from the parent class
        print(f"Number of Pages: {self.number_of_pages}") #This displays the new attribute of this class

class Magazine(Publication): # This is a child class of the publication class
    def __init__(self, title, author, issue_number): # This is the constructor method that shows the inherited and new attributes of the class
        super().__init__(title, author) # This calls the constructor from the parent class to initialize the inherited attributes
        self.issue_number = issue_number # This is the new attribute of this class that did not come from the parent class
        
    def display_info(self): # This displays the information of this child class
        super().display_info() # This displays the attributes from the parent class
        print(f"Issue Number: {self.issue_number}") # This displays the new attribute of this class

#objects of the classes
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dogen, H.")
book1 = Book ("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

#This is the printed output of the objects
print("Publication Information:")
pub1.display_info()
print("\nBook Information:")
book1.display_info()
print("\nMagazine Information:")
mag1.display_info()
