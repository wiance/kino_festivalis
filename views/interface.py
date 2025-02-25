from services.film_service import FilmService

def festivalis():
    films_service = FilmService()
    print("Sveiki atvykę į kino festivalio valdymo sistemą!")
    

    film_name = input("Įveskite filmo pavadinimą: ")
    film_duration = int(input("Įveskite trukmę minutėmis: "))
    film_genre = input("Įveskite žanrą: ")
    film_director = input("Įveskite režisierių: ")
    release_date = int(input("Įveskite išleidimo metus: "))
    age_rating = input("Įveskite amžiaus reitingą (pvz., 'N-13'): ")

    films_service.add_film(film_name, film_duration, film_genre, film_director, release_date, age_rating)

    films_service.display()
