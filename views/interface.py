from services.film_service import FilmService

def festivalis():
    films_service = FilmService()

    while True:
        print("--------------------------------------------------")
        print("\nSveiki atvykę į kino festivalio valdymo sistemą!\n")
        print("1. Pridėti filmą")
        print("2. Pašalinti filmą")
        print("3. Rodyti filmus")
        print("4. Atnaujinti filmą")
        print("5. Surasti filmą")
        print("\nIšeiti - ENTER\n")
        choice = input("Pasirinkite veiksmą: \n")

        if choice == '1':
            film_name = input("Įveskite filmo pavadinimą: ")
            film_duration = int(input("Įveskite trukmę minutėmis: "))
            film_genre = input("Įveskite žanrą: ")
            film_director = input("Įveskite režisierių: ")
            release_date = int(input("Įveskite išleidimo metus: "))
            age_rating = input("Įveskite amžiaus reitingą (pvz., 'N-13'): ")

            films_service.add_film(film_name, film_duration, film_genre, film_director, release_date, age_rating)
        
        elif choice == '2':
            del_filmName = input("Įveskite filmo pavadinimą, kurį norite pašalinti: ")

            films_service.remove_film(del_filmName)
        
        elif choice == '3':
            films_service.display()

        elif choice == '4':
            pass
        
        elif choice == '5':
            film_exists = input("Norint surasti filmą, įveskite filmo pavadinimą ar filmo režisierių: ")
            films_service.search_film(film_exists)

        elif choice == '':
            break

        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")

        
       
