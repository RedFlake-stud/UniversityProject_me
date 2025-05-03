import tkinter as tk
from ui_elements.base_page import BasePage

class AvailableHospitals(BasePage):
    def __init__(self, parent, controller, manager):
        super().__init__(parent, controller)
        self.controller = controller
        self.manager = manager
        
        label = tk.Label(self, text="Available Hospitals:", font=('Arial', 24))
        label.pack(pady=20)

        self.hospitals_list = tk.Listbox(self, font=('Arial', 14), width=50)
        self.hospitals_list.pack(pady=10)

        backbtn = tk.Button(self, text="Back", command=self.go_back)
        backbtn.pack(pady=10)

    def update_available_hospitals(self):
        self.hospitals_list.delete(0, tk.END)
        for name, hospital in self.manager._hospitals.items():
            print(f"Checking availability for {name}: {hospital.is_available()}")
            if hospital.is_available():
                self.hospitals_list.insert(tk.END, name)

    def go_back(self):
        from ui_elements.emergency_page import EmergencyPage
        super().go_back(EmergencyPage)