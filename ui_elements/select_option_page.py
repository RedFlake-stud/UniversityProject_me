import tkinter as tk
from ui_elements.base_page import BasePage


class SelectOptionPage(BasePage):
    def __init__(self, parent, controller, manager):
        super().__init__(parent, controller)
        self.controller = controller
        self.manager = manager

        label = tk.Label(
            self, text="Choose Hospital from list:", font=("Arial", 24)
        )
        label.pack(pady=20)

        self.select_listbox = tk.Listbox(self, font=("Arial", 14), height=8)
        self.select_listbox.pack(pady=10)

        label = tk.Label(self, text="Select a function:", font=("Arial", 24))
        label.pack(pady=20)

        self.buttonframe = tk.Frame(self)
        self.buttonframe.columnconfigure(0, weight=6)
        self.buttonframe.columnconfigure(1, weight=5)
        self.buttonframe.rowconfigure(0, weight=1)
        self.buttonframe.rowconfigure(1, weight=1)

        add_btn = tk.Button(
            self.buttonframe,
            text="Add Items",
            height=4,
            font=("Arial", 20),
            command=self.go_to_add_page,
        )
        add_btn.grid(row=0, column=0, sticky="ew")

        remove_btn = tk.Button(
            self.buttonframe,
            text="Remove Items",
            height=4,
            font=("Arial", 20),
            command=self.go_to_remove_page,
        )
        remove_btn.grid(row=0, column=1, sticky="ew")

        delete_btn = tk.Button(
            self.buttonframe,
            text="Delete Hospital",
            height=4,
            font=("Arial", 20),
            command=self.delete_hospital,
        )
        delete_btn.grid(row=1, column=0, columnspan=2, sticky="ew")

        self.buttonframe.pack(fill="x", expand=True)

        backbtn = tk.Button(self, text="Back", command=self.go_back)
        backbtn.pack(pady=10)

    def update_list(self):
        self.select_listbox.delete(0, tk.END)
        for name in self.manager.list_hospitals():
            self.select_listbox.insert(tk.END, name)

    def update_available_hospitals(self):
        self.hospitals_list.delete(0, tk.END)
        for name, hospital in self.manager._hospitals.items():
            if hospital.is_available():
                self.hospitals_list.insert(tk.END, name)

    def go_to_add_page(self):
        from ui_elements.add_hospital_item_page import AddHospitalItemPage
        selection = self.select_listbox.curselection()
        if not selection:
            print("No hospital selected.")
            return
        name = self.select_listbox.get(selection[0])
        hospital = self.manager.get_hospital(name)
        if not hospital:
            print(f"Hospital '{name}' not found.")
            return

        add_page = self.controller.frames[AddHospitalItemPage]
        add_page.load_hospital(hospital)
        self.controller.show_frame(AddHospitalItemPage)

    def go_to_remove_page(self):
        from ui_elements.remove_hospital_item_page import RemoveHospitalItemPage
        selection = self.select_listbox.curselection()
        if not selection:
            print("No hospital selected.")
            return
        name = self.select_listbox.get(selection[0])
        hospital = self.manager.get_hospital(name)
        if not hospital:
            print(f"Hospital '{name}' not found.")
            return

        remove_page = self.controller.frames[RemoveHospitalItemPage]
        remove_page.load_hospital(hospital)
        self.controller.show_frame(RemoveHospitalItemPage)

    def delete_hospital(self):
        selection = self.select_listbox.curselection()
        if not selection:
            print("No hospital selected.")
            return
        name = self.select_listbox.get(selection[0])
        hospital = self.manager.get_hospital(name)
        if not hospital:
            print(f"Hospital '{name}' not found.")
            return

        self.manager.delete_hospital(hospital)
        self.update_list()

    def go_back(self):
        from ui_elements.config_page import ConfigPage
        super().go_back(ConfigPage)