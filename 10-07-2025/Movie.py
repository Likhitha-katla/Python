import requests
def Movie(title):
    api_key = "641f48d5"
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"
    movie_data_json = requests.get(url)
    if movie_data_json.status_code == 200:
            movie_data = movie_data_json.json()
            if movie_data.get("Response") == "True":
                print(movie_data)
                print("Title: ",movie_data["Title"])
                print("Year: ",movie_data["Year"])
                print("Reeased Date: ",movie_data["Released"])
                print("Director: ",movie_data["Director"])
                print("Writer: ",movie_data["Writer"])
                print("Language: ",movie_data["Language"])
            else:
                print("Movie not found!")
    else:
        print("Failed to fetch data. Status code:", movie_data.status_code)

movie_name = input("enter the movie name")
Movie(movie_name)