class Room:
    def __init__(self, room_number, capacity, patients):
        self._room_number = room_number
        self._capacity = capacity
        self._is_occupied = False
        self._patient_amount = patients

    def occupy_room(self):
        if self._patient_amount >= self._capacity:
            print("Room is occupied.")
        else:
            print("Room has space left.")
        print(f"{self._patient_amount}/{self._capacity}")
        self.update_is_occupied()

    def update_patient_amount(self, new_patient_amount):
        self._patient_amount = new_patient_amount

    def update_is_occupied(self):
        if self._patient_amount >= self._capacity:
            self._is_occupied = True
        else:
            self._is_occupied = False

    def __str__(self):
        return f"Room: {self._room_number} (Capacity: {self._capacity}) (Patients: {self._patient_amount})"