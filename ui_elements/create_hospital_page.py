import tkinter as tk
from hospital_manager import Hospital
from ui_elements.base_page import BasePage

class CreateHospitalPage(BasePage):
    def __init__(self, parent, controller, manager):
        super().__init__(parent, controller)
        self.controller = controller
        self.manager = manager

        label = tk.Label(self, text="Create a new hospital", font=('Arial', 24))
        label.pack(pady=20)

        self.newname = tk.Entry(self, font=('Arial', 20))
        self.newname.pack()

        submitbutton = tk.Button(self, text="Submit", font=('Arial', 20), command=self.create)
        submitbutton.pack(pady=20)

        backbtn = tk.Button(self, text="Back", font=('Arial', 16),
                            command=self.go_back)
        backbtn.pack(pady=40)

    def create(self):
        from ui_elements.config_page import ConfigPage
        name = self.newname.get()
        if not name:
            print("Please enter a name.")
            return

        if self.manager.get_hospital(name):
            print("Hospital already exists.")
            return

        hospital = Hospital(name)                
        self.manager.add_hospital(hospital)           
        print(f"Hospital '{name}' created and saved.")

        self.controller.show_frame(ConfigPage)

    def go_back(self):
        from ui_elements.config_page import ConfigPage
        super().go_back(ConfigPage)