import unittest
from hospital_manager import Hospital
from models.staff import Doctor, Nurse
from models.room import Room


class TestHospital(unittest.TestCase):
    def setUp(self):
        self.hospital = Hospital("Test Hospital", filename="test_hospital.txt")

    def test_add_doctor(self):
        doctor = Doctor("John Doe", 40, "Male", "Cardiology")
        self.hospital.add_doctor(doctor)
        self.assertIn(doctor, self.hospital._doctors)

    def test_add_nurse(self):
        nurse = Nurse("Jane Smith", 30, "Female")
        self.hospital.add_nurse(nurse)
        self.assertIn(nurse, self.hospital._nurses)

    def test_add_room(self):
        room = Room("101", 2, 1)
        self.hospital.add_room(room)
        self.assertIn(room, self.hospital._rooms)

    def test_is_available(self):
        doctor = Doctor("John Doe", 40, "Male", "Cardiology")
        nurse1 = Nurse("Jane Smith", 30, "Female")
        nurse2 = Nurse("Alice Brown", 35, "Female")
        room = Room("101", 2, 1)

        self.hospital.add_doctor(doctor)
        self.hospital.add_nurse(nurse1)
        self.hospital.add_nurse(nurse2)
        self.hospital.add_room(room)

        self.assertTrue(self.hospital.is_available())


if __name__ == "__main__":
    unittest.main()