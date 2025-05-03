from hospital_manager import HospitalManager
from app import App

manager = HospitalManager()
manager.load_all_hospitals()

if __name__ == "__main__":
    app = App(manager)
    app.mainloop()