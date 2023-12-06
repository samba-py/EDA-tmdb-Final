# en el main corro todas las funciones 
from requests_api import get_movies_data
from requests_api import get_genre_numbers
from limpieza_datos import clean_data
from eda import visualize_data

api_key = "b2baa22e7bb745f2e4885c9c88051d08"

# Obtengo datos de la API
raw_data = get_movies_data(api_key)

genre_id_name_converter = get_genre_numbers()
print("ya termino la adquisision de los datos necesarios")


# Realiza la limpieza de datos

cleaned_data = clean_data(raw_data,genre_id_name_converter)
print("se realizo correctamente la limpieza de datos")

# R3ealiza el análisis exploratorio de datos y visualizacion
visualize_data(cleaned_data)
print("se realizo correctamente la visualizacion ")
print("FIN")