import unittest
from models.staff import Doctor, Nurse


class TestMedicalStaff(unittest.TestCase):
    def test_doctor_creation(self):
        doctor = Doctor("John Doe", 40, "Male", "Cardiology")
        self.assertEqual(doctor._name, "John Doe")
        self.assertEqual(doctor._age, 40)
        self.assertEqual(doctor._gender, "Male")
        self.assertEqual(doctor._specialization, "Cardiology")
        self.assertEqual(doctor._status, "Available")

    def test_doctor_update_status(self):
        doctor = Doctor("John Doe", 40, "Male", "Cardiology")
        doctor.update_status("Unavailable")
        self.assertEqual(doctor._status, "Unavailable")

    def test_nurse_creation(self):
        nurse = Nurse("Jane Smith", 30, "Female")
        self.assertEqual(nurse._name, "Jane Smith")
        self.assertEqual(nurse._age, 30)
        self.assertEqual(nurse._gender, "Female")
        self.assertEqual(nurse._status, "Available")

    def test_nurse_update_status(self):
        nurse = Nurse("Jane Smith", 30, "Female")
        nurse.update_status("Unavailable")
        self.assertEqual(nurse._status, "Unavailable")


if __name__ == "__main__":
    unittest.main()