class Medical_staff:
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

class Doctor(Medical_staff):
    def __init__(self, name, age, gender, specialization):
        super().__init__(name,age,gender)
        self._specialization = specialization
        self._status = "Available"

    def update_status(self, new_status):
        self._status = new_status

class Nurse(Medical_staff):
    def __init__(self, name, age, gender):
        super().__init__(name,age,gender)
        self._status = "Available"

    def update_status(self, new_status):
        self._status = new_status
