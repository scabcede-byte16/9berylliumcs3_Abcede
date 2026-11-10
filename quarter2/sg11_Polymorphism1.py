class Patient:
    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_bill_amount(self):
        return self.bill_amount
    def set_bill_amount(self, bill_amount):
        self.bill_amount = bill_amount
    def calculate_bill(self):
        return self.bill_amount
    def display_patient_type(self):
        print("Patient Type: Regular Patient")
    def display_info(self):
        print(f"Patient Name: {self.name}, Bill Amount: {self.bill_amount}")
        self.display_patient_type()

class SeniorPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
        self.discount_percentage = 20
        return self.discount_percentage
    def set_discount_percentage(self, discount_percentage):
        self.discount_percentage = discount_percentage
    def calculate_bill(self):
        discounted_amount = self.bill_amount * (1 - self.discount_percentage / 100)
        return discounted_amount
    def display_patient_type(self):
        print("Patient Type: Senior Patient")
    def display_info(self):
        print(f"Patient Name: {self.name}, Bill Amount: {self.bill_amount}")
        self.display_patient_type()

class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
        self.discount_percentage = 15
        return self.discount_percentage
    def set_discount_percentage(self, discount_percentage):
        self.discount_percentage = discount_percentage
    def calculate_bill(self):
        discounted_amount = self.bill_amount * (1 - self.discount_percentage / 100)
        return discounted_amount
    def display_patient_type(self):
        print("Patient Type: PhilHealth Patient")
    def display_info(self):
        print(f"Patient Name: {self.name}, Bill Amount: {self.bill_amount}")
        self.display_patient_type()

#These are the objects for the class
Patient1 = Patient("Juan Dela Cruz", 15000.00)
SeniorPatient1 = SeniorPatient("Maria Santos", 15000.00 )
PhilHealthPatient1 = PhilHealthPatient("Pedro Reyes", 15000.00)

print("Hospital Billing System")
print("-----------------------")
Patient1.display_info()

SeniorPatient1.display_info()

PhilHealthPatient1.display_info()