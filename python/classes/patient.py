from classes.person import Person


class Patient(Person):

    def __init__(self, patient_id, name, age, gender, phone, symptoms, allergies):

        super().__init__(name, age, gender, phone)

        self.patient_id = patient_id
        self.symptoms = symptoms
        self.allergies = allergies

    def show_info(self):

        return f"Patient ID: {self.patient_id}, Name: {self.name}"