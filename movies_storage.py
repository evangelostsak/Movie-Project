import json


def get_movies():
    """reading the movie file database"""
    try:
        with open("data.json", "r") as file:
            data = file.read()
            movies = json.loads(data)
    except FileNotFoundError:
        movies = {}
        print("Error loading movie database")

    return movies


def save_movies(movies):
    """Saves the changes made in the json file"""
    with open("data.json", "w") as file:
        json.dump(movies, file, indent=4)


def add_movie(title, year, rating):
    """Add a new movie to the json file"""
    movies = get_movies()
    movies[title] = {"year": year, "rating": rating}
    save_movies(movies)


def delete_movie(title):
    """Deletes movie from json file"""
    movies = get_movies()
    if title in movies:
        del movies[title]
        print(f"\nMovie {title} deleted successfully")
        save_movies(movies)
    else:
        print(f"No movie with title {title} found in the database")


def update_movie(title, rating):
    """updates the year or rating in the movie database (json)"""
    movies = get_movies()
    if title in movies:
        movies[title]["rating"] = rating
        save_movies(movies)

    else:
        print(f"Movie {title} not found!")
