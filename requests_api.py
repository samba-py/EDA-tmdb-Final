import requests
import pandas as pd


def get_movies_data(api_key):
    base_url = "https://api.themoviedb.org/3"

    #request para recibir base de datos de tmdbm
    #se guarda en formato json en una variable data
    response = requests.get(f"{base_url}/movie/popular?api_key={api_key}")
    data = response.json()
    return data["results"]

