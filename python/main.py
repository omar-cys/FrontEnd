import flet as ft
from classes.patient import Patient
from classes.doctor import Doctor
from classes.appointment import Appointment
from classes.emergency_case import EmergencyCase
from classes.bed_management import BedManagement
from classes.medical_record import MedicalRecord

doctors = [
    Doctor(1, "Omar", 30, "Male", "0775566288", "Open Heart"),
    Doctor(2, "Hala", 32, "Female", "0776655288", "Eyes"),
    Doctor(3, "Mohammad", 45, "Male", "0771122334", "Pediatrics"),
    Doctor(4, "Sarah", 29, "Female", "0772233445", "Dermatology"),
    Doctor(5, "Karim", 38, "Male", "0773344556", "Orthopedics"),
    Doctor(6, "Layan", 35, "Female", "0774455667", "Neurology"),
]

patients = []
appointments = []
emergency_cases = []
medical_records = []
assigned_beds = {}
bed_system = BedManagement()
available_times = ["10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM"]

def main(page: ft.Page):
    page.title = "Hospital Management System"
    page.window_width = 1250
    page.window_height = 820
    page.bgcolor = "#EAF6FF"
    page.scroll = "auto"
    page.padding = 0

    body = ft.Column(spacing=25, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    patient_name = ft.TextField(label="Patient Name", width=380, color="black", border_radius=15)
    patient_age = ft.TextField(label="Age", width=380, color="black", border_radius=15)
    patient_gender = ft.Dropdown(label="Gender", width=380, border_radius=15, options=[ft.dropdown.Option("Male"), ft.dropdown.Option("Female")])
    patient_phone = ft.TextField(label="Phone", width=380, color="black", border_radius=15)

    patient_symptoms = ft.Dropdown(
        label="Symptoms",
        width=380,
        border_radius=15,
        options=[
            ft.dropdown.Option("Headache"),
            ft.dropdown.Option("Fever"),
            ft.dropdown.Option("Chest Pain"),
            ft.dropdown.Option("Cough"),
            ft.dropdown.Option("Diabetes"),
            ft.dropdown.Option("Eye Pain"),
        ]
    )

    patient_allergies = ft.Dropdown(
        label="Allergies",
        width=380,
        border_radius=15,
        options=[
            ft.dropdown.Option("None"),
            ft.dropdown.Option("Penicillin"),
            ft.dropdown.Option("Dust"),
            ft.dropdown.Option("Food Allergy"),
        ]
    )

    medication = ft.Dropdown(
        label="Medication",
        width=380,
        border_radius=15,
        options=[
            ft.dropdown.Option("None"),
            ft.dropdown.Option("Penicillin"),
            ft.dropdown.Option("Ibuprofen"),
            ft.dropdown.Option("Aspirin"),
            ft.dropdown.Option("Insulin"),
        ]
    )

    doctor_dropdown = ft.Dropdown(
        label="Choose Doctor",
        width=380,
        border_radius=15,
        options=[ft.dropdown.Option(f"Dr. {d.name} - {d.specialization}") for d in doctors]
    )

    appointment_date = ft.TextField(label="Appointment Date", width=380, color="black", border_radius=15, hint_text="04/06/2026")
    appointment_time = ft.Dropdown(label="Available Times", width=380, border_radius=15, options=[ft.dropdown.Option(t) for t in available_times])

    temperature = ft.TextField(label="Temperature", width=380, color="black", border_radius=15, hint_text="37.5")
    pain_level = ft.Dropdown(label="Pain Level", width=380, border_radius=15, options=[ft.dropdown.Option(str(i)) for i in range(1, 11)])

    diagnosis_field = ft.Dropdown(
        label="Diagnosis",
        width=380,
        border_radius=15,
        options=[
            ft.dropdown.Option("Heart Disease"),
            ft.dropdown.Option("Migraine"),
            ft.dropdown.Option("Diabetes"),
            ft.dropdown.Option("Eye Infection"),
            ft.dropdown.Option("Flu"),
            ft.dropdown.Option("General Checkup"),
        ]
    )

    treatment_field = ft.Dropdown(
        label="Treatment",
        width=380,
        border_radius=15,
        options=[
            ft.dropdown.Option("Heart Medication"),
            ft.dropdown.Option("Pain Killers"),
            ft.dropdown.Option("Insulin"),
            ft.dropdown.Option("Eye Drops"),
            ft.dropdown.Option("Antibiotics"),
            ft.dropdown.Option("Rest and Follow-up"),
        ]
    )

    notes_field = ft.TextField(label="Notes", width=380, color="black", border_radius=15)

    bed_department = ft.Dropdown(
        label="Bed Department",
        width=380,
        border_radius=15,
        options=[
            ft.dropdown.Option("ICU"),
            ft.dropdown.Option("Emergency"),
            ft.dropdown.Option("Normal"),
        ]
    )

    recommended_text = ft.Text("", size=17, weight="bold", color="#D32F2F")
    triage_result = ft.Text("", size=17, weight="bold", color="#D32F2F")
    drug_warning = ft.Text("", size=17, weight="bold", color="#D32F2F")
    bed_message = ft.Text("", size=17, weight="bold", color="#01579B")
    record_message = ft.Text("", size=17, weight="bold", color="#D32F2F")

    appointment_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Patient", color="black")),
            ft.DataColumn(ft.Text("Doctor", color="black")),
            ft.DataColumn(ft.Text("Date", color="black")),
            ft.DataColumn(ft.Text("Time", color="black")),
            ft.DataColumn(ft.Text("Status", color="black")),
        ],
        rows=[]
    )

    emergency_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Patient", color="black")),
            ft.DataColumn(ft.Text("Symptom", color="black")),
            ft.DataColumn(ft.Text("Temp", color="black")),
            ft.DataColumn(ft.Text("Pain", color="black")),
            ft.DataColumn(ft.Text("Priority", color="black")),
        ],
        rows=[]
    )

    records_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Patient", color="black")),
            ft.DataColumn(ft.Text("Diagnosis", color="black")),
            ft.DataColumn(ft.Text("Treatment", color="black")),
            ft.DataColumn(ft.Text("Notes", color="black")),
        ],
        rows=[]
    )

    bed_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Department", color="black")),
            ft.DataColumn(ft.Text("Total", color="black")),
            ft.DataColumn(ft.Text("Occupied", color="black")),
            ft.DataColumn(ft.Text("Available", color="black")),
        ],
        rows=[]
    )

    def find_patient_by_name(name):
        for p in patients:
            if p.name.lower() == name.lower():
                return p
        return None

    def patient_has_appointment(name):
        for app in appointments:
            if app.patient.name.lower() == name.lower():
                return True
        return False

    def get_recommended_doctor(symptom):
        if symptom == "Chest Pain":
            return "Omar", "Possible heart problem", "Critical"
        if symptom == "Eye Pain":
            return "Hala", "Possible eye infection", "Medium"
        if symptom in ["Fever", "Cough"]:
            return "Mohammad", "Possible infection", "Medium"
        if symptom == "Headache":
            return "Layan", "Possible neurological issue", "Medium"
        if symptom == "Diabetes":
            return "Mohammad", "Blood sugar follow-up", "Medium"
        return None, "Unknown", "Low"

    def doctor_load(name):
        count = 0
        for app in appointments:
            if app.doctor.name == name:
                count += 1
        if count >= 4:
            return "High Load"
        elif count >= 2:
            return "Medium Load"
        return "Low Load"

    def doctor_card(d, recommended_name=None):
        is_recommended = d.name == recommended_name
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(f"Dr. {d.name}", size=22, weight="bold", color="#01579B"),
                    ft.Text(f"Specialization: {d.specialization}", color="black", size=15),
                    ft.Text(f"Phone: {d.phone}", color="black", size=15),
                    ft.Text(f"Load: {doctor_load(d.name)}", color="#D32F2F" if doctor_load(d.name) == "High Load" else "black", size=15),
                    ft.Container(height=3, bgcolor="#D32F2F", visible=is_recommended),
                    ft.Text("Recommended Doctor", color="#D32F2F", weight="bold", visible=is_recommended),
                ],
                spacing=6
            ),
            width=300,
            height=175,
            bgcolor="#FFEBEE" if is_recommended else "white",
            border_radius=18,
            padding=20,
            shadow=ft.BoxShadow(spread_radius=1, blur_radius=12, color="#90CAF9")
        )

    def doctors_grid(recommended_name=None):
        return ft.Column(
            [
                ft.Row([doctor_card(d, recommended_name) for d in doctors[0:3]], spacing=25, alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([doctor_card(d, recommended_name) for d in doctors[3:6]], spacing=25, alignment=ft.MainAxisAlignment.CENTER),
            ],
            spacing=25,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def update_available_times(e=None):
        if not doctor_dropdown.value or not appointment_date.value:
            appointment_time.options = [ft.dropdown.Option(t) for t in available_times]
            appointment_time.value = None
            page.update()
            return

        selected_name = doctor_dropdown.value.split(" - ")[0].replace("Dr. ", "")
        booked = []

        for app in appointments:
            if app.doctor.name == selected_name and app.date == appointment_date.value:
                booked.append(app.time)

        appointment_time.options = [ft.dropdown.Option(t) for t in available_times if t not in booked]
        appointment_time.value = None
        page.update()

    def suggest_doctor(e):
        name, diagnosis, priority = get_recommended_doctor(patient_symptoms.value)

        if not name:
            recommended_text.value = "Choose symptom first"
            show_doctors()
            return

        for d in doctors:
            if d.name == name:
                recommended_text.value = f"Recommended: Dr. {d.name} - {d.specialization} | {diagnosis} | Priority: {priority}"
                doctor_dropdown.value = f"Dr. {d.name} - {d.specialization}"

        show_doctors(name)

    def check_drug_alert():
        if patient_allergies.value == "Penicillin" and medication.value == "Penicillin":
            drug_warning.value = "Warning: Patient is allergic to Penicillin!"
        elif patient_symptoms.value == "Chest Pain" and medication.value == "Ibuprofen":
            drug_warning.value = "Warning: Ibuprofen may not be suitable for chest pain cases."
        else:
            drug_warning.value = "No drug interaction warning."

    def analyze_triage(e):
        if not patient_name.value or not temperature.value or not pain_level.value or not patient_symptoms.value:
            triage_result.value = "Fill patient name, symptom, temperature, and pain level."
            page.update()
            return

        case = EmergencyCase(patient_name.value, temperature.value, pain_level.value, patient_symptoms.value)
        priority = case.calculate_priority()
        emergency_cases.append(case)
        refresh_emergency_table()
        triage_result.value = f"Triage Result: {priority}"
        page.update()

    def refresh_emergency_table():
        emergency_table.rows.clear()
        priority_order = {"Critical": 1, "Medium": 2, "Low": 3}
        sorted_cases = sorted(emergency_cases, key=lambda c: priority_order[c.priority])

        for case in sorted_cases:
            emergency_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(case.patient_name, color="black")),
                        ft.DataCell(ft.Text(case.symptom, color="black")),
                        ft.DataCell(ft.Text(str(case.temperature), color="black")),
                        ft.DataCell(ft.Text(str(case.pain_level), color="black")),
                        ft.DataCell(ft.Text(case.priority, color="red" if case.priority == "Critical" else "black")),
                    ]
                )
            )

    def refresh_bed_table():
        bed_table.rows.clear()
        beds = bed_system.show_beds()

        for dep, data in beds.items():
            bed_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(dep, color="black")),
                        ft.DataCell(ft.Text(str(data["total"]), color="black")),
                        ft.DataCell(ft.Text(str(data["occupied"]), color="black")),
                        ft.DataCell(ft.Text(str(data["total"] - data["occupied"]), color="black")),
                    ]
                )
            )

    def assign_bed(e):
        if not patient_name.value:
            bed_message.value = "Enter patient name first."
            page.update()
            return

        if not find_patient_by_name(patient_name.value):
            bed_message.value = "Patient not found in system."
            page.update()
            return

        if not patient_has_appointment(patient_name.value):
            bed_message.value = "Patient has no appointment."
            page.update()
            return

        if patient_name.value.lower() in assigned_beds:
            bed_message.value = "Patient already has a bed."
            page.update()
            return

        if not bed_department.value:
            bed_message.value = "Choose department first."
            page.update()
            return

        result = bed_system.assign_bed(bed_department.value)

        if result == "Bed Assigned":
            assigned_beds[patient_name.value.lower()] = bed_department.value

        bed_message.value = result
        refresh_bed_table()
        page.update()

    def release_bed(e):
        if not patient_name.value:
            bed_message.value = "Enter patient name first."
            page.update()
            return

        if patient_name.value.lower() not in assigned_beds:
            bed_message.value = "This patient does not have a bed."
            page.update()
            return

        department = assigned_beds[patient_name.value.lower()]
        bed_message.value = bed_system.release_bed(department)
        del assigned_beds[patient_name.value.lower()]
        refresh_bed_table()
        page.update()

    def suggest_treatment(e):
        if not patient_name.value:
            record_message.value = "Enter patient name first."
            page.update()
            return

        if not find_patient_by_name(patient_name.value):
            record_message.value = "Patient not found in system."
            page.update()
            return

        if not diagnosis_field.value:
            record_message.value = "Choose diagnosis first."
            page.update()
            return

        if diagnosis_field.value == "Heart Disease":
            treatment_field.value = "Heart Medication"
        elif diagnosis_field.value == "Migraine":
            treatment_field.value = "Pain Killers"
        elif diagnosis_field.value == "Diabetes":
            treatment_field.value = "Insulin"
        elif diagnosis_field.value == "Eye Infection":
            treatment_field.value = "Eye Drops"
        elif diagnosis_field.value == "Flu":
            treatment_field.value = "Antibiotics"
        else:
            treatment_field.value = "Rest and Follow-up"

        record_message.value = "Treatment suggested successfully."
        page.update()

    def add_medical_record(e):
        if not patient_name.value:
            record_message.value = "Enter patient name first."
            page.update()
            return

        found_patient = find_patient_by_name(patient_name.value)

        if not found_patient:
            record_message.value = "Patient not found in system."
            page.update()
            return

        if not diagnosis_field.value or not treatment_field.value:
            record_message.value = "Choose diagnosis and treatment."
            page.update()
            return

        record = MedicalRecord(
            len(medical_records) + 1,
            found_patient.name,
            diagnosis_field.value,
            treatment_field.value,
            notes_field.value
        )

        medical_records.append(record)

        records_table.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(record.patient_name, color="black")),
                    ft.DataCell(ft.Text(record.diagnosis, color="black")),
                    ft.DataCell(ft.Text(record.treatment, color="black")),
                    ft.DataCell(ft.Text(record.notes, color="black")),
                ]
            )
        )

        diagnosis_field.value = None
        treatment_field.value = None
        notes_field.value = ""
        record_message.value = "Medical record added successfully."
        page.update()

    def book_appointment(e):
        if not patient_name.value or not patient_age.value or not patient_gender.value or not patient_phone.value or not patient_symptoms.value or not patient_allergies.value or not medication.value or not doctor_dropdown.value or not appointment_date.value or not appointment_time.value:
            page.snack_bar = ft.SnackBar(ft.Text("Please fill all fields!"))
            page.snack_bar.open = True
            page.update()
            return

        check_drug_alert()

        selected_doctor = None
        for d in doctors:
            if doctor_dropdown.value == f"Dr. {d.name} - {d.specialization}":
                selected_doctor = d

        for app in appointments:
            if app.doctor.name == selected_doctor.name and app.date == appointment_date.value and app.time == appointment_time.value:
                page.snack_bar = ft.SnackBar(ft.Text("Doctor already booked at this time!"))
                page.snack_bar.open = True
                update_available_times()
                return

        patient = Patient(len(patients) + 1, patient_name.value, patient_age.value, patient_gender.value, patient_phone.value, patient_symptoms.value, patient_allergies.value)
        patients.append(patient)

        appointment = Appointment(len(appointments) + 1, patient, selected_doctor, appointment_date.value, appointment_time.value)
        appointments.append(appointment)

        appointment_table.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(patient.name, color="black")),
                    ft.DataCell(ft.Text(selected_doctor.name, color="black")),
                    ft.DataCell(ft.Text(appointment.date, color="black")),
                    ft.DataCell(ft.Text(appointment.time, color="black")),
                    ft.DataCell(ft.Text(appointment.status, color="black")),
                ]
            )
        )

        page.snack_bar = ft.SnackBar(ft.Text("Appointment booked successfully!"))
        page.snack_bar.open = True

        saved_doctor = doctor_dropdown.value
        saved_date = appointment_date.value

        patient_name.value = ""
        patient_age.value = ""
        patient_gender.value = None
        patient_phone.value = ""
        patient_symptoms.value = None
        patient_allergies.value = None
        medication.value = None
        doctor_dropdown.value = saved_doctor
        appointment_date.value = saved_date
        appointment_time.value = None
        recommended_text.value = ""

        update_available_times()
        show_appointments()

    def stat_card(title, value, color):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(title, color="white", size=16, weight="bold"),
                    ft.Text(str(value), color="white", size=28, weight="bold"),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            width=200,
            padding=20,
            border_radius=20,
            bgcolor=color
        )

    def header():
        return ft.Container(
            content=ft.Row(
                [
                    ft.Row(
                        [
                            ft.Container(
                                content=ft.Icon(ft.Icons.LOCAL_HOSPITAL, color="white", size=35),
                                bgcolor="#0288D1",
                                width=60,
                                height=60,
                                border_radius=30,
                            ),
                            ft.Column(
                                [
                                    ft.Text("SilverCare Hospital", size=28, weight="bold", color="#01579B", text_align="center"),
                                    ft.Text("Professional Healthcare System", size=14, color="black", text_align="center"),
                                ],
                                spacing=2,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            )
                        ],
                        spacing=15,
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            ft.ElevatedButton("Home", icon=ft.Icons.HOME, on_click=lambda e: show_home()),
                            ft.ElevatedButton("Doctors", icon=ft.Icons.MEDICAL_SERVICES, on_click=lambda e: show_doctors()),
                            ft.ElevatedButton("Booking", icon=ft.Icons.CALENDAR_MONTH, on_click=lambda e: show_booking()),
                            ft.ElevatedButton("Emergency", icon=ft.Icons.WARNING, on_click=lambda e: show_emergency()),
                            ft.ElevatedButton("Records", icon=ft.Icons.FOLDER, on_click=lambda e: show_records()),
                            ft.ElevatedButton("Beds", icon=ft.Icons.BED, on_click=lambda e: show_beds()),
                            ft.ElevatedButton("Dashboard", icon=ft.Icons.DASHBOARD, on_click=lambda e: show_dashboard()),
                        ],
                        spacing=8,
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            ),
            bgcolor="white",
            padding=25,
            margin=30,
            border_radius=25,
            shadow=ft.BoxShadow(spread_radius=1, blur_radius=20, color="#90CAF9")
        )

    def intro_box():
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("Welcome to SilverCare Hospital", size=30, weight="bold", color="#01579B", text_align="center"),
                    ft.Text(
                        "A modern hospital system for appointments, triage, emergency queue, medical records, bed management, drug alerts, and statistics dashboard.",
                        size=17,
                        color="black",
                        text_align="center"
                    ),
                    ft.Row(
                        [
                            ft.Container(ft.Text("Smart Triage", color="white", weight="bold"), bgcolor="#0288D1", padding=15, border_radius=15),
                            ft.Container(ft.Text("Emergency Queue", color="white", weight="bold"), bgcolor="#00ACC1", padding=15, border_radius=15),
                            ft.Container(ft.Text("AI Symptom Checker", color="white", weight="bold"), bgcolor="#26A69A", padding=15, border_radius=15),
                        ],
                        spacing=15,
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ],
                spacing=15,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            bgcolor="white",
            padding=30,
            width=1000,
            border_radius=25,
            shadow=ft.BoxShadow(spread_radius=1, blur_radius=20, color="#90CAF9")
        )

    def booking_form():
        return ft.Container(
            content=ft.Column(
                [
                    patient_name,
                    patient_age,
                    patient_gender,
                    patient_phone,
                    patient_symptoms,
                    ft.ElevatedButton("Suggest Doctor", icon=ft.Icons.MEDICAL_SERVICES, on_click=suggest_doctor, style=ft.ButtonStyle(bgcolor="#EF5350", color="white")),
                    recommended_text,
                    patient_allergies,
                    medication,
                    drug_warning,
                    doctor_dropdown,
                    appointment_date,
                    ft.ElevatedButton("Show Available Times", icon=ft.Icons.ACCESS_TIME, on_click=update_available_times, style=ft.ButtonStyle(bgcolor="#0288D1", color="white")),
                    appointment_time,
                    ft.ElevatedButton("Book Appointment", icon=ft.Icons.CALENDAR_MONTH, on_click=book_appointment, style=ft.ButtonStyle(bgcolor="#29B6F6", color="white", padding=20)),
                ],
                spacing=14,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            bgcolor="white",
            border_radius=25,
            padding=30,
            width=460,
            shadow=ft.BoxShadow(spread_radius=1, blur_radius=20, color="#90CAF9")
        )

    def emergency_form():
        return ft.Container(
            content=ft.Column(
                [
                    patient_name,
                    patient_symptoms,
                    temperature,
                    pain_level,
                    ft.ElevatedButton("Analyze Triage", icon=ft.Icons.WARNING, on_click=analyze_triage, style=ft.ButtonStyle(bgcolor="#D32F2F", color="white")),
                    triage_result,
                ],
                spacing=14,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            bgcolor="white",
            border_radius=25,
            padding=30,
            width=460,
            shadow=ft.BoxShadow(spread_radius=1, blur_radius=20, color="#90CAF9")
        )

    def records_form():
        return ft.Container(
            content=ft.Column(
                [
                    patient_name,
                    diagnosis_field,
                    ft.ElevatedButton("Suggest Treatment", icon=ft.Icons.MEDICAL_SERVICES, on_click=suggest_treatment, style=ft.ButtonStyle(bgcolor="#26A69A", color="white")),
                    treatment_field,
                    notes_field,
                    record_message,
                    ft.ElevatedButton("Add Medical Record", icon=ft.Icons.ADD, on_click=add_medical_record, style=ft.ButtonStyle(bgcolor="#0288D1", color="white")),
                ],
                spacing=14,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            bgcolor="white",
            border_radius=25,
            padding=30,
            width=460,
            shadow=ft.BoxShadow(spread_radius=1, blur_radius=20, color="#90CAF9")
        )

    def beds_form():
        return ft.Container(
            content=ft.Column(
                [
                    patient_name,
                    bed_department,
                    ft.Row(
                        [
                            ft.ElevatedButton("Assign Bed", icon=ft.Icons.ADD, on_click=assign_bed, style=ft.ButtonStyle(bgcolor="#0288D1", color="white")),
                            ft.ElevatedButton("Release Bed", icon=ft.Icons.REMOVE, on_click=release_bed, style=ft.ButtonStyle(bgcolor="#EF5350", color="white")),
                        ],
                        spacing=10,
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    bed_message,
                ],
                spacing=14,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            bgcolor="white",
            border_radius=25,
            padding=30,
            width=460,
            shadow=ft.BoxShadow(spread_radius=1, blur_radius=20, color="#90CAF9")
        )

    def footer():
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("SilverCare Hospital", size=24, weight="bold", color="#01579B", text_align="center"),
                    ft.Text("Contact: 0778932299 | Location: Irbid, Jordan", color="black", text_align="center"),
                    ft.Text("Emergency Service Available 24/7", color="black", text_align="center"),
                    ft.Text("© 2026 3MOR Hospital Management System", color="gray", text_align="center"),
                ],
                spacing=8,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            bgcolor="white",
            padding=35,
            margin=35,
            width=750,
            border_radius=30,
            shadow=ft.BoxShadow(spread_radius=1, blur_radius=18, color="#B3E5FC")
        )

    def set_body(items):
        body.controls.clear()
        body.controls.extend(items)
        page.update()

    def show_home():
        set_body([
            header(),
            intro_box(),
            ft.Text("Available Doctors", size=30, weight="bold", color="#0277BD", text_align="center"),
            doctors_grid(),
            ft.Divider(),
            ft.Text("Book Appointment", size=32, weight="bold", color="#0277BD", text_align="center"),
            booking_form(),
            footer()
        ])

    def show_doctors(recommended_name=None):
        set_body([header(), ft.Text("Available Doctors", size=34, weight="bold", color="#0277BD"), doctors_grid(recommended_name), footer()])

    def show_booking():
        set_body([header(), ft.Text("Book Appointment", size=34, weight="bold", color="#0277BD"), booking_form(), footer()])

    def show_appointments():
        set_body([header(), ft.Text("Appointments", size=34, weight="bold", color="#0277BD"), ft.Container(content=appointment_table, bgcolor="white", border_radius=25, padding=25, width=700), footer()])

    def show_emergency():
        set_body([header(), ft.Text("Emergency Triage", size=34, weight="bold", color="#D32F2F"), emergency_form(), ft.Container(content=emergency_table, bgcolor="white", border_radius=25, padding=25, width=850), footer()])

    def show_records():
        set_body([header(), ft.Text("Medical Records", size=34, weight="bold", color="#0277BD"), records_form(), ft.Container(content=records_table, bgcolor="white", border_radius=25, padding=25, width=850), footer()])

    def show_beds():
        refresh_bed_table()
        set_body([header(), ft.Text("Bed Management", size=34, weight="bold", color="#0277BD"), beds_form(), ft.Container(content=bed_table, bgcolor="white", border_radius=25, padding=25, width=750), footer()])

    def show_dashboard():
        critical_count = 0
        for case in emergency_cases:
            if case.priority == "Critical":
                critical_count += 1

        occupied = 0
        beds = bed_system.show_beds()
        for dep in beds:
            occupied += beds[dep]["occupied"]

        set_body([
            header(),
            ft.Text("Hospital Statistics Dashboard", size=34, weight="bold", color="#0277BD"),
            ft.Row(
                [
                    stat_card("Patients", len(patients), "#0288D1"),
                    stat_card("Appointments", len(appointments), "#00ACC1"),
                    stat_card("Critical Cases", critical_count, "#D32F2F"),
                    stat_card("Medical Records", len(medical_records), "#7B1FA2"),
                    stat_card("Occupied Beds", occupied, "#26A69A"),
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER,
                wrap=True
            ),
            doctors_grid(),
            footer()
        ])

    page.add(ft.Container(content=body, padding=25, bgcolor="#EAF6FF", expand=True))
    show_home()

ft.run(main)