class BedManagement:
    def __init__(self):
        self.beds = {
            "ICU": {"total": 5, "occupied": 0},
            "Emergency": {"total": 8, "occupied": 0},
            "Normal": {"total": 20, "occupied": 0}
        }

    def assign_bed(self, department):
        if self.beds[department]["occupied"] < self.beds[department]["total"]:
            self.beds[department]["occupied"] += 1
            return "Bed Assigned"
        return "No Beds Available"

    def release_bed(self, department):
        if self.beds[department]["occupied"] > 0:
            self.beds[department]["occupied"] -= 1
            return "Bed Released"
        return "No Beds to Release"

    def show_beds(self):
        return self.beds