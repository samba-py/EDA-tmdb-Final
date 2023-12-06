import pandas as pd
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

# defino funcion para realizar limpieza de datos
def clean_data(raw_data,genre_id_text):
    #############
    df = pd.DataFrame(raw_data)
    # aca falta agregar las lineas de codigo para realizar la limpieza de datos
    null_counts = df.isnull().sum()

    # Muestra la cantidad de valores nulos por columna
    #print("Valores nulos por columna:")
    #print(null_counts)
    #hay un solo null en baackdrop_path
    df.dropna(inplace=True)
    null_counts = df.isnull().sum()
    #print(null_counts)

    #eliminado los datos nulos, veo el tipo de dato de cada columna
    #print("Tipos de datos por columna:")
    #print(df.dtypes)

    df['release_date'] = pd.to_datetime(df['release_date'])
    df['release_date'] = df['release_date'].dt.strftime('%Y-%m-%d')
    df['genre_ids'] = df['genre_ids'].apply(lambda x: x.split(',') if isinstance(x, str) else x)
    #############


    #############
    #funcion para cambiar los id de cada genero por el equivalente a texto
    id_to_text_mapping = {genre['id']: genre['name'] for genre in genre_id_text['genres']}

    # Función para mapear IDs a texto
    def map_ids_to_text(ids):
        return [id_to_text_mapping[id] for id in ids]

    # Aplicar la función a la columna 'genre_ids' en el DataFrame df
    df['genre_ids'] = df['genre_ids'].apply(map_ids_to_text)

    # Imprimir los primeros resultados
    #print("**************")
    #print(df['genre_ids'].head(10))
    #print("Tipos de datos por columna:")
    #print(df.dtypes)
    ################


    ################
    #hago una impresion general para ver el contenido de cada columna 
    




    #####################3
    columns_to_drop = ['backdrop_path', 'id', 'overview', 'poster_path', 'video']

    # Eliminar las columnas
    df = df.drop(columns=columns_to_drop, axis=1)

    

    #######################
    for column in df.columns:
    # Imprimir el nombre de la columna
        print(f'Columna: {column}')
    
    # Imprimir los primeros 10 datos de la columna
        for value in df[column].head(10):
            print(value)

    # Separador para mayor claridad
        print('\n' + '='*30 + '\n')

    #######################


    return df

