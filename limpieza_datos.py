import pandas as pd

# defino funcion para realizar limpieza de datos
def clean_data(raw_data):
    df = pd.DataFrame(raw_data)
    # aca falta agregar las lineas de codigo para realizar la limpieza de datos
    null_counts = df.isnull().sum()

    # Muestra la cantidad de valores nulos por columna
    print("Valores nulos por columna:")
    print(null_counts)
    #hay un solo null en baackdrop_path
    df.dropna(inplace=True)
    null_counts = df.isnull().sum()
    print(null_counts)

    #eliminado los datos nulos, veo el tipo de dato de cada columna
    print("Tipos de datos por columna:")
    print(df.dtypes)

    df['release_date'] = pd.to_datetime(df['release_date'])
    df['genre_ids'] = df['genre_ids'].apply(lambda x: x.split(',') if isinstance(x, str) else x)

    #seguir aca con los cambios
    
    print("Tipos de datos por columna:")
    print(df.dtypes)
    return df

