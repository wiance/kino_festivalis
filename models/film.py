class Film:
    def __init__(self, film_name, film_duration, film_genre, film_director, release_date, age_rating):
        self.film_name = film_name
        self.film_duration = film_duration
        self.film_genre = film_genre
        self.film_director = film_director
        self.release_date = release_date
        self.age_rating = age_rating

    def __repr__(self):
        return f"{self.film_name} ({self.release_date}), {self.film_duration} min, {self.film_director}, rež. {self.film_director}, reitingas: {self.age_rating}"