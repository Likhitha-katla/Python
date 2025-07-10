import requests
def Movie(title):
    api_key = "641f48d5"
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"
    movie_data_json = requests.get(url)
    # print(movie_data.status_code)
    movie_data = movie_data_json.json()
    print(movie_data)
    print("Title: ",movie_data["Title"])
    print("Year: ",movie_data["Year"])
    print("Reeased Date: ",movie_data["Released"])
    print("Director: ",movie_data["Director"])
    print("Writer: ",movie_data["Writer"])
    print("Language: ",movie_data["Language"])

movie_name = input("enter the movie name")
Movie(movie_name)