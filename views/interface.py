from services.film_service import FilmService
from services.screenings_service import ScreeningService

class Interface:
    def __init__(self):
        self.films_service = FilmService()
        self.screening_service = ScreeningService()

    def festivalis(self):
        while True:
            print("\n++++++++++++++++++++")
            print("\n1. Prisijungti")
            print("2. Išeiti - ENTER")
            userORadmin = input("\nPasirinkite veiksmą: ")

            if userORadmin == '1':
                print("fyi: įveskite 'admin', jei norite pasiekti organizatoriaus teises")
                nickname = input("Įveskite savo vardą: ")
                if nickname.lower() == 'admin':
                    self.admin_meniu()
                else:
                    self.vartotojo_meniu()
                    break

            elif userORadmin == '':
                print("Išėjimas iš programos...")
                break

            else:
                print("Netinkamas pasirinkimas. Bandykite dar kartą.")

    def admin_meniu(self):
        while True:
            print("--------------------------------------------------")
            print("\nSveiki atvykę į kino festivalio valdymo sistemą!")
            print("\n++Organizatoriaus Meniu++\n")
            print("1. Pridėti filmą")
            print("2. Pašalinti filmą")
            print("3. Rodyti filmus")
            print("4. Atnaujinti filmą")
            print("5. Surasti filmą")
            print("6. Pridėti seansą")
            print("7. Panaikinti seansą")
            print("8. Rodyti seansus")
            print("\nIšeiti - ENTER\n")
    
            choice = input("Pasirinkite veiksmą: \n")

            if choice == '1':
                film_name = input("Įveskite filmo pavadinimą: ")
                film_duration = int(input("Įveskite trukmę minutėmis: "))
                film_genre = input("Įveskite žanrą: ")
                film_director = input("Įveskite režisierių: ")
                release_date = int(input("Įveskite išleidimo metus: "))
                age_rating = input("Įveskite amžiaus reitingą (pvz., 'N-13'): ")

                self.films_service.add_film(film_name, film_duration, film_genre, film_director, release_date, age_rating)
            
            elif choice == '2':
                del_filmName = input("Įveskite filmo pavadinimą, kurį norite pašalinti: ")
                self.films_service.remove_film(del_filmName)
            
            elif choice == '3':
                self.films_service.displayFilms()

            elif choice == '4':
                pass
            
            elif choice == '5':
                film_exists = input("Norint surasti filmą, įveskite filmo pavadinimą ar filmo režisierių: ")
                self.films_service.search_film(film_exists)

            elif choice == '6':
                while True:
                    try:
                        screeningName_input = input("Įveskite filmo pavadinimą: ")
                        date_input = input("Įveskite datą (YYYY-MM-DD): ")
                        time_input = input("Įveskite laiką (HH:MM): ")
                       
                        self.screening_service.add_screening(screeningName_input, date_input, time_input)
                        break
                    except ValueError: 
                        print("Klaida: neteisingas datos arba laiko formatas. Bandykite dar kartą.")
            
            elif choice == '7':
                screeningName_delete = input("Įveskite seanso pavadinimą, kurį norite pašalinti: ")
                self.screening_service.remove_screening(screeningName_delete)
           
            elif choice == '8':
                self.screening_service.displayScreenings()

            elif choice == '':
                break

            else:
                print("Neteisingas pasirinkimas. Bandykite dar kartą.")

            
    def vartotojo_meniu(nickname):
        print("\n++Kino Festivalio Meniu++\n")
        print("Esu vartotojo meniu")
