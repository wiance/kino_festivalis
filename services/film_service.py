from models.film import Film
from services.data_handler import load_data, save_data
from config import films_path

class FilmService:
    def __init__(self):
        self.film_list = load_data(films_path)
    def add_film(self, film_name, film_duration, film_genre, film_director, release_date, age_rating):

        film = Film(film_name, film_duration, film_genre, film_director, release_date, age_rating)
        self.film_list.append(film)
        save_data(films_path, self.film_list)
        print("Filmas sėkmingai pridėtas!")

    def remove_film(self):
        remove_filmname = input("Įveskite filmo pavadinimą, kurį norite pašalinti: ")
        

        # new_all_films = []
        # for filmas in self.all_films:
        #     if ?? != remove_filmname.lower():
    def display(self):
        for index in range(len(self.film_list)):
            print(f"{index+1}. {self.film_list[index]}")
            

            # TEST GITHUB

        




