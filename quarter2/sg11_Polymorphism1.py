#Code ni sofiya absidy
class Patient: #This is the parent class
    def __init__(self, name, original_bill_amount, final_bill_amount): #This is the constructor method for this class
        self.name = name
        self.original_bill_amount = original_bill_amount
        self.final_bill_amount = final_bill_amount 
    def get_name(self): #This is the getter for this name attribute
        return self.name #This returns the value that is in the name attribute
    def set_name(self, name): #This is the setter for this name attribute
        self.name = name #This sets the value in the name attribute
    def get_original_bill_amount(self): #This is the getter for this original_bill_amount attribute
        return self.original_bill_amount #This returns the value that is in the original_bill_amount attribute
    def set_original_bill_amount(self, original_bill_amount): #This is the setter for this original_bill_amount attribute
        self.original_bill_amount = original_bill_amount #This sets the value in the original_bill_amount attribute
    def get_final_bill_amount(self): #This is the getter for this final_bill_amount attribute
        return self.final_bill_amount #This returns the value that is in the final_bill_amount attribute
    def set_final_bill_amount(self, final_bill_amount): #This is the setter for this final_bill_amount attribute
        self.final_bill_amount = final_bill_amount #This sets the value in the final_bill_amount attribute  
    def calculate_bill(self): #This method calculates the final bill amount for a regular patient
        return self.final_bill_amount #This returns the final bill amount for a regular patient
    def display_patient_type(self): #This method displays the patient type for a regular patient
        print("Patient Type: Regular Patient") # This prints the patient type for a regular patient
    def display_info(self): #This method displays the patient information for a regular patient
        print(f"Patient Name: {self.name}, Original Bill: {self.original_bill_amount} Final Bill: {self.final_bill_amount}") #This prints the current patient's information
        self.display_patient_type() #This calls the display_patient_type method to display the patient type for a regular patient

class SeniorPatient(Patient): #This is one of the child class of Patient
    def __init__(self, name, original_bill_amount, final_bill_amount): #This is the constructor method for this class
        super().__init__(name, original_bill_amount, final_bill_amount) #This calls the constructor methods from the Patient class
    def calculate_bill(self): #This method calculates the final bill amount for a senior patient
        discount = 0.20 #This is the discount foor the senior patient which is 20%
        discounted_amount = float(self.final_bill_amount) * (1 - discount) #This calculates the discounted amount for the SP
        return f"{discounted_amount:.2f}" #This returns the discounted amount for the SP
    def display_patient_type(self): #This method displays the patient type for a SP
        print("Patient Type: Senior Citizen") #This prints the patient type for a SP

class PhilHealthPatient(Patient): #This is the other child class of Patient
    def __init__(self, name, original_bill_amount, final_bill_amount): #This is the constructor method for this class
        super().__init__(name, original_bill_amount, final_bill_amount) #This calls the constructor methods from the Patient class
    def calculate_bill(self): #This calculates the final bill
        discount = 0.15 #This is the discount for PHP (PhilHealth Patients) which is 15%
        discounted_amount = float(self.final_bill_amount) * (1 - discount) #This calculates the discounted amount for the PHP
        return f"{discounted_amount:.2f}" #This returns the discounted amount for the PHP
    def display_patient_type(self): #This method displays the patient type for a PHP
        print("Patient Type: PhilHealth Patient") #This prints the patient type for a PHP

#These are the objects for the class
Patient1 = Patient("Juan Dela Cruz", "15,000.00", "15,000.00")
SeniorPatient1 = SeniorPatient("Maria Santos", "15,000.00", "12,000.00")
PhilHealthPatient1 = PhilHealthPatient("Pedro Reyes", "15,000.00", "12,750.00")
#This prints the final output for the 
print("Hospital Billing System")
print("-----------------------")
Patient1.display_info()

SeniorPatient1.display_info()

PhilHealthPatient1.display_info()

#Nahirapan ako d2 sir