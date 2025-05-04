import tkinter as tk
from models.factory import Factory
from ui_elements.base_page import BasePage

ELEMENTS = ["Doctor", "Nurse", "Room"]


class AddHospitalItemPage(BasePage):
    def __init__(self, parent, controller, manager):
        super().__init__(parent, controller)
        self.controller = controller
        self.manager = manager
        self.hospital = None

        self.title_label = tk.Label(self, text="", font=("Arial", 24))
        self.title_label.pack(pady=20)

        self.elements = ELEMENTS
        self.selection_var = tk.IntVar(value=0)
        self.selection_var.trace_add("write", self.load_selection)

        for index, element in enumerate(self.elements):
            radio = tk.Radiobutton(
                self, text=element, variable=self.selection_var, value=index
            )
            radio.pack()

        self.textframe = tk.Frame(self)
        self.textframe.pack(fill="both", expand=False, pady=10)

        save_btn = tk.Button(self, text="Save Entry", command=self.save_entry)
        save_btn.pack(pady=10)

        back_btn = tk.Button(self, text="Back", command=self.go_back)
        back_btn.pack(pady=10)

    def go_back(self):
        from ui_elements.select_option_page import SelectOptionPage
        super().go_back(SelectOptionPage)

    def load_selection(self, *args):
        for widget in self.textframe.winfo_children():
            widget.destroy()

        self.entries = {}
        selection = self.selection_var.get()

        if selection == 0:  # Doctor
            fields = ["Name", "Age", "Specialization", "Gender"]
            for col, label in enumerate(fields):
                tk.Label(self.textframe, text=label).grid(row=0, column=col, sticky="ew")
                entry = tk.Entry(self.textframe)
                entry.grid(row=1, column=col, sticky="ew")
                self.entries[label.lower()] = entry

            tk.Label(self.textframe, text="Availability").grid(
                row=0, column=len(fields), sticky="ew"
            )
            self.avail_var = tk.StringVar(value="Available")
            avail_frame = tk.Frame(self.textframe)
            avail_frame.grid(row=1, column=len(fields), sticky="ew")

            tk.Radiobutton(
                avail_frame, text="Available", variable=self.avail_var, value="Available"
            ).pack(side="left")
            tk.Radiobutton(
                avail_frame,
                text="Unavailable",
                variable=self.avail_var,
                value="Unavailable",
            ).pack(side="left")

        elif selection == 1:  # Nurse
            fields = ["Name", "Age", "Gender"]
            for col, label in enumerate(fields):
                tk.Label(self.textframe, text=label).grid(row=0, column=col, sticky="ew")
                entry = tk.Entry(self.textframe)
                entry.grid(row=1, column=col, sticky="ew")
                self.entries[label.lower()] = entry

        else:  # Room
            fields = ["Room Number", "Capacity", "Patient Count"]
            for col, label in enumerate(fields):
                tk.Label(self.textframe, text=label).grid(row=0, column=col, sticky="ew")
                entry = tk.Entry(self.textframe)
                entry.grid(row=1, column=col, sticky="ew")
                self.entries[label.lower()] = entry

        for i in range(len(fields) + 1):
            self.textframe.columnconfigure(i, weight=1)

    def load_hospital(self, hospital):
        self.hospital = hospital
        self.title_label.config(text=f"Editing Hospital: {hospital._name}")
        self.load_selection()

    def save_entry(self):
        if not self.hospital:
            return

        selection = self.selection_var.get()

        if selection == 0:  # Doctor
            try:
                name = self.entries["name"].get()
                age = int(self.entries["age"].get())
                spec = self.entries["specialization"].get()
                gender = self.entries["gender"].get()
                status = self.avail_var.get()
                doctor = Factory.create_doctor(name, age, gender, spec, status)
                self.hospital.add_doctor(doctor)
                print(f"Doctor '{name}' saved.")
            except Exception as e:
                print("Error adding doctor:", e)

        elif selection == 1:  # Nurse
            try:
                name = self.entries["name"].get()
                age = int(self.entries["age"].get())
                gender = self.entries["gender"].get()
                nurse = Factory.create_nurse(name, age, gender)
                self.hospital.add_nurse(nurse)
                print(f"Nurse '{name}' saved.")
            except Exception as e:
                print("Error adding nurse:", e)

        else:  # Room
            try:
                room_number = self.entries["room number"].get()
                capacity = int(self.entries["capacity"].get())
                patient_count = int(self.entries["patient count"].get())
                room = Factory.create_room(room_number, capacity, patient_count)
                self.hospital.add_room(room)
                print(f"Room '{room_number}' saved.")
            except Exception as e:
                print("Error adding room:", e)