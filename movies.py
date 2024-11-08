import statistics
import random
import movies_storage


def press_to_continue():  # Self-explanatory
    print()
    input("Press anything to continue... \n")


def exit_program():  # exit prompt
    print("Bye!")


def list_movies():
    """1. Listing all the movies"""
    movies = movies_storage.get_movies()
    total_movies = 0
    for _ in movies:
        total_movies += 1
    print(f"{total_movies} movies in total")
    for movie, details in movies.items():
        rating = details["rating"]
        year = details["year"]
        print(f"{movie} ({year}): {rating}")


def add_movie():
    """Adding a new movie and its details in the database
     checking if the movie doesn't already exist before continuing"""
    movies = movies_storage.get_movies()
    while True:
        add_name = input("Please enter the name of the movie u wanna add: ")
        if len(add_name) == 0:
            print("Movie title can not be empty")

        elif add_name in movies:
            print(f"Movie {add_name} already exist in the database ")

        else:
            while True:
                try:
                    add_rating = float(input("Please enter it's rating: "))
                    break
                except ValueError:
                    print("Invalid input! Please enter a number")
            while True:
                try:
                    add_year = int(input("Please enter the year of the movie: "))
                    break
                except ValueError:
                    print("Invalid input! Year should be a number")
            movies_storage.add_movie(add_name, add_year, add_rating)
            print(f"\nMovie {add_name} successfully added to the database")
            break


def delete_movie():
    """3. Deleting a movie, if the movie only exists."""

    delete = input("Which movie shall be deleted? ")

    movies_storage.delete_movie(delete)


def update_movie():
    """Update the rating of an existing movie in the database"""

    update_title = input("Which movie shall be updated? ")

    update_rating = float(input("Please enter the updated rating: "))
    movies_storage.update_movie(update_title, update_rating)


def stats():
    """Showing the user the statistics of the movie database such as
    average rating, median rating, best rated movie and the worst rated one"""
    movies = movies_storage.get_movies()

    ratings = [details["rating"] for details in movies.values()]
    movie_names = list(movies.keys())

    average_rating = statistics.mean(ratings)
    median_rating = statistics.median(ratings)
    best_movie = movie_names[ratings.index(max(ratings))]
    worst_movie = movie_names[ratings.index(min(ratings))]

    print(f"Average rating: {round(average_rating, 2)}")
    print(f"Median rating: {round(median_rating, 2)}")
    print(f"Best Movie: {best_movie}, {max(ratings)}")
    print(f"Worst Movie: {worst_movie}, {min(ratings)}")


def random_movie():
    """Picks a random movie for the user"""
    movies = movies_storage.get_movies()
    movie, details = random.choice(list(movies.items()))

    rating = details["rating"]
    year = details["year"]
    print(f"Tonight's choice is: {movie} ({year}), rated at: {rating}")


def search_movie():
    """Searches a movie based of the users input, very sensitive"""
    movies = movies_storage.get_movies()

    search_input = input("Please enter part of movie's name: ").lower()

    for movie, details in movies.items():
        rating = details["rating"]
        year = details["year"]
        if search_input in movie.lower():
            print(f"{movie} ({year}): {rating}")


# def rating_sorted_movies():
# movies_sorting = sorted(movies.items(), key=lambda item: item[1], reverse=True)
# for movie, rating in movies_sorting:
# print(f"{movie}, {rating}")
def rating_sorted_movies():
    """ Display a sorted version of the ratings in the movie database in descending order
    bubble sorting, going through the rating over and over and pushing the lower rating at the end(descending)"""
    movies = movies_storage.get_movies()

    movies_sorting = list(movies.items())

    for i in range(len(movies_sorting)):
        for j in range(len(movies_sorting) - 1):
            if movies_sorting[j][1]["rating"] < movies_sorting[j + 1][1]["rating"]:
                movies_sorting[j], movies_sorting[j + 1] = movies_sorting[j + 1], movies_sorting[j]

    for movie, details in movies_sorting:
        print(f"{movie} ({details["year"]}), {details["rating"]}")


def year_sorted_movies():

    """ User asked what type of order he wants and program sorts them accordingly
    bubble sorting used, this time year is pushed around according to the users wishes"""
    movies = movies_storage.get_movies()
    print("\nHow would you like the movies to be sorted?\n ")
    while True:  # not letting the user use any other form or number except the ints 1 and 2.
        try:

            user_choice = int(input("Press 1 for ascending order | Press 2 for descending order\n"))
            if user_choice != 1 and user_choice != 2:
                print("Invalid input! Please enter a number between 1 & 2")
            else:
                break

        except ValueError:
            print("Invalid Input! Please enter a number")

    movies_sorting = list(movies.items())

    for i in range(len(movies_sorting)):
        for j in range(len(movies_sorting) - 1):
            if user_choice == 1:
                if movies_sorting[j][1]["year"] > movies_sorting[j + 1][1]["year"]:
                    movies_sorting[j], movies_sorting[j + 1] = movies_sorting[j + 1], movies_sorting[j]
            elif user_choice == 2:
                if movies_sorting[j][1]["year"] < movies_sorting[j + 1][1]["year"]:
                    movies_sorting[j], movies_sorting[j + 1] = movies_sorting[j + 1], movies_sorting[j]

    for movie, details in movies_sorting:
        print(f"{movie} rated at: {details["rating"]}, made in {details["year"]}")


def main():
    """Main data structure, user picks a number of the action he wants to do
    Program is always running and updating with the users decisions.
    Press 0 to Exit
    Function Pointers used. User has to enter a valid number from 0 to 9 and only that to execute the action """
    menu_actions = {
        0: exit_program,
        1: list_movies,
        2: add_movie,
        3: delete_movie,
        4: update_movie,
        5: stats,
        6: random_movie,
        7: search_movie,
        8: rating_sorted_movies,
        9: year_sorted_movies
    }

    while True:
        print("********** My Movies Database **********")
        print("")
        print("Menu:")
        print("0. Exit")
        print("1. List movies")
        print("2. Add movie")
        print("3. Delete Movie")
        print("4. Update movie")
        print("5. Stats")
        print("6. Random movie")
        print("7. Search movie")
        print("8. Movies sorted by rating")
        print("9. Movies sorted by year")
        print("")
        try:

            user_input = int(input("Enter Choice (0-9): "))
            print("")

            if user_input in menu_actions:

                menu_actions[user_input]()

                if user_input != 0:
                    press_to_continue()
                if user_input == 0:
                    break
            else:
                print("Invalid choice, please enter a number between 0 and 9.")
                press_to_continue()

        except ValueError:
            print("\nInvalid input, please enter a number.\n")
            press_to_continue()


if __name__ == "__main__":
    main()
