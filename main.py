# en el main corro todas las funciones 
from requests_api import get_movies_data
from limpieza_datos import clean_data
#from eda import visualize_data

api_key = "b2baa22e7bb745f2e4885c9c88051d08"

# Obtengo datos de la API
raw_data = get_movies_data(api_key)

# Realiza la limpieza de datos

cleaned_data = clean_data(raw_data)
print(cleaned_data["genre_ids"].head(10))


# R3ealiza el análisis exploratorio de datos y visualizacion
#visualize_data(cleaned_data)