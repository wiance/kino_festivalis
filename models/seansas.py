class Seansas:
    def __init__(self, film, date, time):
        self.film = film
        self.date = date
        self.time = time

    def __str__(self):
        return f"{self.film_name} - {self.date} {self.time}, {self.vieta} ({self.laisvos_vietos} laisvų vietų)"