from datetime import datetime

class Screening:
    def __init__(self, screening_name, date, time):
        self.screening_name = screening_name
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.time = datetime.strptime(time, "%H:%M").time()


    def __str__(self):
        return f"{self.screening_name} - {self.date} {self.time}"