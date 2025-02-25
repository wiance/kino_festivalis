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

    def remove_film(self, remove_filmName):
        film_to_remove = None
        for film in self.film_list:
            if film.film_name.lower() == remove_filmName.lower():
                film_to_remove = film
                break
    
        if film_to_remove:
            self.film_list.remove(film_to_remove)
            save_data(films_path, self.film_list)
            print(f"Filmas '{remove_filmName}' buvo pašalintas.")
        else:
            print(f"Filmas '{remove_filmName}' sąraše nerastas.")

    def search_film(self, wanted):
        for film in self.film_list:
            if film.film_name.lower() == wanted.lower() or film.film_director.lower() == wanted.lower():
                print("Šis filmas yra sąraše")
                return  # Nutraukti ciklą ir funkciją
        print("Ieškomas filmas nerastas")  

    def display(self):
        for index in range(len(self.film_list)):
            print(f"{index+1}. {self.film_list[index]}")
            

        




