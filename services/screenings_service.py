from models.seansas import Screening
from services.data_handler import load_screeningData, save_screeningData
from config import screenings_path
from datetime import datetime

class ScreeningService:
    def __init__(self):
        self.screenings_list = load_screeningData(screenings_path)

    # def screening_exists(self, date, time):

    #     for screen in self.screenings_list:
    #             if (screen.date == date and screen.time == time):
    #                 print("Ieškomas seansas buvo rastas sąraše")
    #                 return True
    #     return False  
 
    def add_screening(self, screening_name, date, time):
        # if self.screening_exists(date, time):
        #     print("Toks seansas jau egzistuoja!")
        #     return 
        screening = Screening(screening_name, date, time)
        self.screenings_list.append(screening)
        save_screeningData(screenings_path, self.screenings_list)
        print("Filmo seansas buvo sėkmingai pridėtas!")
    
    def remove_screening(self, screening_id):
        screening_to_remove = None
        for screening in self.screenings_list:
            if screening.screening_name.lower() == screening_id.lower():
                screening_to_remove = screening
                break
        if screening_to_remove:
            self.screenings_list.remove(screening_to_remove)
            save_screeningData(screenings_path, self.screenings_list)
            print(f"Seansas '{screening_id}' buvo pašalintas.")
        else:
            print(f"Seansas'{screening_id}' sąraše nerastas.") 

    def displayScreenings(self):
        for index in range(len(self.screenings_list)):
            print(f"{index+1}. {self.screenings_list[index]}")
    
    def update_screening():
        pass
