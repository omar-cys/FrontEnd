class Appointment:

    def __init__(self, appointment_id, patient, doctor, date, time):

        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
        self.status = "Booked"

    def cancel_appointment(self):

        self.status = "Cancelled"

    def show_appointment(self):

        return f"{self.patient.name} with Dr. {self.doctor.name} at {self.time}"