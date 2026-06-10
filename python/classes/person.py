class Person:

    def __init__(self, name, age, gender, phone):

        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone

    def show_info(self):

        return f"Name: {self.name}, Age: {self.age}"