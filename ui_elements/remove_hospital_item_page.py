import tkinter as tk
from ui_elements.base_page import BasePage

class RemoveHospitalItemPage(BasePage):
    def __init__(self, parent, controller, manager):
        super().__init__(parent, controller)
        self.controller = controller
        self.manager = manager

        self.label = tk.Label(self, text="Choose item:", font=('Arial', 24))
        self.label.pack(pady=20)

        self.item_listbox = tk.Listbox(self, font=('Arial', 16), width=50, height=10)
        self.item_listbox.pack(pady=10)

        self.removebtn = tk.Button(self, text="Remove Item", font=('Arial', 16))
        self.removebtn.pack(pady=10)

        self.backbtn = tk.Button(self, text="Back", command=self.go_back)
        self.backbtn.pack(pady=20)

    def go_back(self):
        from ui_elements.select_option_page import SelectOptionPage
        super().go_back(SelectOptionPage)

    def load_hospital(self, hospital):
        self.hospital = hospital
        self.label.config(text=f"Choose item from {hospital._name}:")
        self.item_listbox.delete(0, tk.END)

        for item in hospital.get_items():
            self.item_listbox.insert(tk.END, item)

        self.removebtn.config(command=self.remove_item)

    def remove_item(self):
        selection = self.item_listbox.curselection()
        if not selection:
            print("No item selected.")
            return

        item = self.item_listbox.get(selection[0])
        self.hospital.remove_item(item)
        self.item_listbox.delete(selection[0])
        print(f"Removed {item} from {self.hospital.name}.")
        self.manager.save_hospital(self.hospital)
        self.manager.save_all_hospitals()

    def update_list(self):
        self.item_listbox.delete(0, tk.END)
        for item in self.hospital.get_items():
            self.item_listbox.insert(tk.END, item)





