import tkinter as tk
from tkinter import messagebox
from ui_elements.base_page import BasePage


class RemoveHospitalItemPage(BasePage):
    def __init__(self, parent, controller, manager):
        super().__init__(parent, controller)
        self.controller = controller
        self.manager = manager

        self.label = tk.Label(self, text="Choose item:", font=("Arial", 24))
        self.label.pack(pady=20)

        self.listbox_frame = tk.Frame(self)
        self.listbox_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.item_listbox = tk.Listbox(
            self.listbox_frame, font=("Arial", 16), width=50, height=10
        )
        self.item_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(
            self.listbox_frame, orient=tk.VERTICAL, command=self.item_listbox.yview
        )
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.item_listbox.config(yscrollcommand=self.scrollbar.set)

        self.removebtn = tk.Button(
            self, text="Remove Item", font=("Arial", 16), command=self.remove_item
        )
        self.removebtn.pack(pady=10)

        self.backbtn = tk.Button(self, text="Back", command=self.go_back)
        self.backbtn.pack(pady=20)

    def go_back(self):
        from ui_elements.select_option_page import SelectOptionPage

        select_page = self.controller.frames[SelectOptionPage]
        select_page.update_list()
        super().go_back(SelectOptionPage)

    def load_hospital(self, hospital):
        self.hospital = hospital
        self.label.config(text=f"Choose item from {hospital._name}:")
        self.item_listbox.delete(0, tk.END)

        items = hospital.get_items()
        if not items:
            self.item_listbox.insert(tk.END, "No items available.")
            self.removebtn.config(state=tk.DISABLED)
        else:
            for item in items:
                self.item_listbox.insert(tk.END, item)
            self.removebtn.config(state=tk.NORMAL)

    def remove_item(self):
        selection = self.item_listbox.curselection()
        if not selection:
            print("No item selected.")
            return

        item_text = self.item_listbox.get(selection[0])

        for item in self.hospital.get_items():
            if str(item) == item_text:
                self.hospital.remove_item(item)
                break
        else:
            print("Item not found in hospital.")
            return

        self.item_listbox.delete(selection[0])

        self.manager.save_hospital(self.hospital)

        tk.messagebox.showinfo(
            "Success", f"Removed {item_text} from {self.hospital._name}."
        )

    def update_list(self):
        self.item_listbox.delete(0, tk.END)
        for item in self.hospital.get_items():
            self.item_listbox.insert(tk.END, item)