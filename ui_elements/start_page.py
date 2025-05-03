import tkinter as tk

class StartPage(tk.Frame):
    def __init__(self, parent, controller, manager):
        super().__init__(parent)
        self.controller = controller
        self.manager = manager

        label = tk.Label(self, text="Main Menu", font=('Arial', 30))
        label.pack(pady=50)

        buttonframe = tk.Frame(self)
        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=1)
        buttonframe.rowconfigure(0, weight=3)
        buttonframe.rowconfigure(1, weight=2)

        btn1 = tk.Button(buttonframe, text="Emergency Mode", height=6, font=('Arial', 20),
                         command=self.go_to_emergency)
        btn1.grid(row=0, column=0, sticky="ew")
        
        btn2 = tk.Button(buttonframe, text="Configure Hospital", height=6, font=('Arial', 20),
                         command=self.go_to_config)
        btn2.grid(row=0, column=1, sticky="ew")

        anotherbtn = tk.Button(buttonframe, text="Exit", height=3, font=('Arial', 20), command=controller.destroy)
        anotherbtn.grid(row=1, column=0, columnspan=2, sticky="ew")
        buttonframe.pack(fill='x', expand=True)

    def go_to_emergency(self):
        from ui_elements.emergency_page import EmergencyPage
        self.controller.show_frame(EmergencyPage)

    def go_to_config(self):
        from ui_elements.config_page import ConfigPage
        self.controller.show_frame(ConfigPage)