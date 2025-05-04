from models.staff import Doctor, Nurse
from models.room import Room


class Factory:
    @staticmethod
    def create_doctor(name, age, gender, specialization, status="Available"):
        doctor = Doctor(name, age, gender, specialization)
        doctor.update_status(status)
        return doctor

    @staticmethod
    def create_nurse(name, age, gender, status="Available"):
        nurse = Nurse(name, age, gender)
        nurse.update_status(status)
        return nurse

    @staticmethod
    def create_room(room_number, capacity, patients):
        return Room(room_number, capacity, patients)