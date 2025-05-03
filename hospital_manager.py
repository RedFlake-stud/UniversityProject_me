import os
from models.factory import Factory

class HospitalManager:
    def __init__(self, data_dir="hospital_data"):
        self._hospitals = {}
        self._data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)

    def add_hospital(self, hospital):
        self._hospitals[hospital._name] = hospital
        self.save_hospital(hospital)

    def get_hospital(self, name):
        return self._hospitals.get(name, None)

    def list_hospitals(self):
        return list(self._hospitals.keys())

    def save_hospital(self, hospital):
        filename = os.path.join(self._data_dir, f"{hospital._name}.txt")
        hospital._filename = filename
        hospital.save_to_file()

    def load_all_hospitals(self):
        for file in os.listdir(self._data_dir):
            if file.endswith(".txt"):
                name = file[:-4]
                hospital = Hospital(name)
                hospital._filename = os.path.join(self._data_dir, file)
                hospital.load_from_file()  
                self._hospitals[name] = hospital

class Hospital:
    def __init__(self, name):
        self._name = name
        self._doctors = []
        self._nurses = []
        self._rooms = []

    def add_doctor(self, doctor):
        for doctors in self._doctors:
            if doctors._name == doctor._name:
                print(f"Doctor already exists. Updating data instead...")
                self.remove_doctor(doctors)
        self._doctors.append(doctor)
        self.save_to_file()

    def add_nurse(self, nurse):
        for nurses in self._nurses:
            if nurses._name == nurse._name:
                print(f"Nurse already exists. Updating data instead...")
                self.remove_nurse(nurses)
        self._nurses.append(nurse)
        self.save_to_file()

    def add_room(self, room):
        for rooms in self._rooms:
            if rooms._name == room._room_number:
                print(f"Room already exists. Updating data instead...")
                self.remove_nurse(rooms)
        
        self._rooms.append(room)
        self.save_to_file()

    def is_available(self):
        available_doctors = [d for d in self._doctors if d._status == "Available"]
        available_nurses = [n for n in self._nurses if n._status == "Available"]
        rooms_with_space = [r for r in self._rooms if r._patient_amount < r._capacity]

        return (
            len(available_doctors) >= 1
            and len(available_nurses) >= 2
            and len(rooms_with_space) >= 1
        )

    def save_to_file(self):
        with open(self._filename, 'w') as f:
            f.write(f"{self._name}\n")
            f.write("[Doctors]\n")
            for d in self._doctors:
                f.write(f"{d._name},{d._age},{d._gender},{d._specialization},{d._status}\n")
            f.write("[Nurses]\n")
            for n in self._nurses:
                f.write(f"{n._name},{n._age},{n._gender},{n._status}\n")
            f.write("[Rooms]\n")
            for r in self._rooms:
                f.write(f"{r._room_number},{r._capacity},{r._patient_amount}\n")
    
    def load_from_file(self):
        if not os.path.exists(self._filename):
            return

        with open(self._filename, 'r') as f:
            section = None
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                elif line == "[Doctors]":
                    section = "doctors"
                elif line == "[Nurses]":
                    section = "nurses"
                elif line == "[Rooms]":
                    section = "rooms"
                elif section == "doctors":
                    name, age, gender, spec, status = line.split(",")
                    doctor = Factory.create_doctor(name, int(age), gender, spec, status)
                    self._doctors.append(doctor)
                elif section == "nurses":
                    name, age, gender, status = line.split(",")
                    nurse = Factory.create_nurse(name, int(age), gender, status)
                    self._nurses.append(nurse)
                elif section == "rooms":
                    room_num, capacity, patients = line.split(",")
                    room = Factory.create_room(room_num, int(capacity), int(patients))
                    self._rooms.append(room)

    def remove_doctor(self, doctor):
        self._doctors.remove(doctor)
        self.save_to_file()

    def remove_nurse(self, nurse):
        self._nurses.remove(nurse)
        self.save_to_file()

    def remove_room(self, room):
        self._rooms.remove(room)
        self.save_to_file()

    def get_items(self):
        return self._doctors + self._nurses + self._rooms
    