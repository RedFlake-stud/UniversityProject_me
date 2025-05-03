import tkinter as tk
from ui_elements.base_page import BasePage

class EmergencyPage(BasePage):
    def __init__(self, parent, controller, manager):
        super().__init__(parent, controller)
        self.controller = controller
        self.manager = manager

        label = tk.Label(self, text="Emergency Mode", font=('Arial', 24))
        label.pack(pady=20)

        show_hospitals_btn = tk.Button(
            self,
            text="Show Available Hospitals",
            font=('Arial', 16),
            command=lambda: self.show_available(controller)
        )
        show_hospitals_btn.pack(pady=10)

        backbtn = tk.Button(self, text="Back", command=self.go_back)
        backbtn.pack(pady=20)

    def show_available(self, controller):
        from ui_elements.available_hospitals import AvailableHospitals
        available_frame = controller.frames[AvailableHospitals]
        available_frame.update_available_hospitals()
        controller.show_frame(AvailableHospitals)

    def go_back(self):
        from ui_elements.start_page import StartPage
        super().go_back(StartPage)
