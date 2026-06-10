class EmergencyCase:
    def __init__(self, patient_name, temperature, pain_level, symptom):
        self.patient_name = patient_name
        self.temperature = float(temperature)
        self.pain_level = int(pain_level)
        self.symptom = symptom
        self.priority = "Low"

    def calculate_priority(self):
        if self.temperature >= 39 or self.pain_level >= 8 or self.symptom == "Chest Pain":
            self.priority = "Critical"
        elif self.temperature >= 37.5 or self.pain_level >= 5:
            self.priority = "Medium"
        else:
            self.priority = "Low"
        return self.priority

    def show_status(self):
        return f"{self.patient_name} - {self.priority}"