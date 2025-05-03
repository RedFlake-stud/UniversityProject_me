import tkinter as tk
from ui_elements.base_page import BasePage

class ConfigPage(BasePage):
    def __init__(self, parent, controller, manager):
        super().__init__(parent, controller)
        self.controller = controller
        self.manager = manager

        label = tk.Label(self, text="Hospital Editor Mode", font=('Arial', 24)) 
        label.pack(pady=20)

        self.buttonframe = tk.Frame(self)
        self.buttonframe.columnconfigure(0, weight=3)
        self.buttonframe.columnconfigure(1, weight=4)

        select_btn = tk.Button(self.buttonframe, text="Select Hospital and Options", height=6, font=('Arial', 16),
                               command=self.go_to_select)
        select_btn.grid(column=0, row=0, sticky="ew")

        createnew_btn = tk.Button(self.buttonframe, text="Create New Hospital", height=6, font=('Arial', 16),
                               command=self.go_to_create)
        createnew_btn.grid(column=1, row=0, sticky="ew")
        self.buttonframe.pack(fill='x', expand=True)

        backbtn = tk.Button(self, text="Back", command=self.go_back)
        backbtn.pack(pady=10)

    def go_back(self):
        from ui_elements.start_page import StartPage
        super().go_back(StartPage)

    def go_to_select(self):
        from ui_elements.select_option_page import SelectOptionPage
        self.controller.show_frame(SelectOptionPage)

    def go_to_create(self):
        from ui_elements.create_hospital_page import CreateHospitalPage
        self.controller.show_frame(CreateHospitalPage)