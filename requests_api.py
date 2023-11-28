import requests
import pandas as pd


def get_movies_data(api_key):
    base_url = "https://api.themoviedb.org/3"

    #request para recibir base de datos de tmdbm
    #se guarda en formato json en una variable data
    response = requests.get(f"{base_url}/movie/popular?api_key={api_key}")
    data = response.json()
    return data["results"]

def get_genre_numbers():
    url = "https://api.themoviedb.org/3/genre/movie/list?language=en"

    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiMmJhYTIyZTdiYjc0NWYyZTQ4ODVjOWM4ODA1MWQwOCIsInN1YiI6IjY1NjU1MTJiMTU2Y2M3MDEwY2IzMDdmYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.cmkm6KkxfZ6aC88PWLwgN23ypsl-yCtja6LnOhutFXI"}

    response = requests.get(url, headers=headers)
    genre_id_text = response.json()


    print(response.text)
    print(genre_id_text)
    return response


