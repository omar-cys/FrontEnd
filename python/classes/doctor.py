from classes.person import Person


class Doctor(Person):

    def __init__(self, doctor_id, name, age, gender, phone, specialization):

        super().__init__(name, age, gender, phone)

        self.doctor_id = doctor_id
        self.specialization = specialization

    def show_info(self):

        return f"Dr. {self.name} - {self.specialization}"