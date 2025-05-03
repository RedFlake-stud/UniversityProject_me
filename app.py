import tkinter as tk
from ui_elements.start_page import StartPage
from ui_elements.emergency_page import EmergencyPage
from ui_elements.config_page import ConfigPage
from ui_elements.available_hospitals import AvailableHospitals
from ui_elements.add_hospital_item_page import AddHospitalItemPage
from ui_elements.create_hospital_page import CreateHospitalPage
from ui_elements.select_option_page import SelectOptionPage
from ui_elements.remove_hospital_item_page import RemoveHospitalItemPage


class App(tk.Tk):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager

        self.title("Emergency Helper")
        self.geometry("1000x750")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)


        self.frames = {}

        for F in (StartPage, EmergencyPage, ConfigPage, AvailableHospitals, AddHospitalItemPage, 
                  CreateHospitalPage, SelectOptionPage, RemoveHospitalItemPage):
            frame = F(self.container, self, self.manager)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)  

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        if hasattr(frame, "update_list"):
            frame.update_list()
        frame.tkraise()