class MedicalRecord:
    def __init__(self, record_id, patient_name, diagnosis, treatment, notes):
        self.record_id = record_id
        self.patient_name = patient_name
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.notes = notes

    def show_record(self):
        return f"{self.patient_name} - {self.diagnosis} - {self.treatment}"