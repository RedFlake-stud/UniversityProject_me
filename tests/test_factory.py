import unittest
from models.factory import Factory
from models.staff import Doctor, Nurse
from models.room import Room


class TestFactory(unittest.TestCase):
    def test_create_doctor(self):
        doctor = Factory.create_doctor("John Doe", 40, "Male", "Cardiology")
        self.assertIsInstance(doctor, Doctor)
        self.assertEqual(doctor._specialization, "Cardiology")
        self.assertEqual(doctor._status, "Available")

    def test_create_nurse(self):
        nurse = Factory.create_nurse("Jane Smith", 30, "Female")
        self.assertIsInstance(nurse, Nurse)
        self.assertEqual(nurse._status, "Available")

    def test_create_room(self):
        room = Factory.create_room("101", 2, 1)
        self.assertIsInstance(room, Room)
        self.assertEqual(room._room_number, "101")
        self.assertEqual(room._capacity, 2)
        self.assertEqual(room._patient_amount, 1)


if __name__ == "__main__":
    unittest.main()