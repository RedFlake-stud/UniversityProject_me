import tkinter as tk


class BasePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

    def go_back(self, target_page):
        self.controller.show_frame(target_page)