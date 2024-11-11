import argparse
from movie_app import MovieApp
from storage.storage_json import StorageJson
from storage.storage_csv import StorageCsv


def main():
    """Main function declaring argument parser to work
    both with command line arguments
    and standard IDE RUN"""
    parser = argparse.ArgumentParser(description="Run the Movie App with a specified storage file")
    parser.add_argument("storage_file", nargs="?", default="data/movies.json",
                        help="Specify the storage file (JSON or CSV)")

    args = parser.parse_args()
    storage_file = args.storage_file

    if storage_file.endswith('.json'):
        storage = StorageJson(storage_file)  # Extension-based storage
    elif storage_file.endswith('.csv'):
        storage = StorageCsv(storage_file)
    else:
        print("Unsupported file format. Use either a .json or .csv file.")
        return

    movie_app = MovieApp(storage)
    movie_app.run()


if __name__ == "__main__":
    main()
