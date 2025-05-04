class MedicalStaff:
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender


class Doctor(MedicalStaff):
    def __init__(self, name, age, gender, specialization):
        super().__init__(name, age, gender)
        self._specialization = specialization
        self._status = "Available"

    def update_status(self, new_status):
        self._status = new_status

    def __str__(self):
        return f"Doctor: {self._name} ({self._specialization})"


class Nurse(MedicalStaff):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self._status = "Available"

    def update_status(self, new_status):
        self._status = new_status

    def __str__(self):
        return f"Nurse: {self._name}"