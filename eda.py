import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#defino funcion para realizar las visualizaciones y el analisis

def visualize_data(df):
    df['release_date'] = pd.to_datetime(df['release_date'])
    df['release_month'] = df['release_date'].dt.month

#  relacion entre mes de lanzamiento y popularidad
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x='release_month', y='popularity', data=df, alpha=0.5, legend=False)  
    plt.title('Relación entre el Mes de Lanzamiento y la Popularidad')
    plt.xlabel('Mes de Lanzamiento')
    plt.ylabel('Popularidad')
    

 #    relacion entre mes de lanzamiento y voto promedio
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x='release_month', y='vote_average', data=df, alpha=0.5, legend=False)
    plt.title('Relación entre el Mes de Lanzamiento y la Puntuación Promedio')
    plt.xlabel('Mes de Lanzamiento')
    plt.ylabel('Puntuación Promedio')
    



    df_genre_exploded = df['genre_ids'].explode().astype('category')

# Explorar la distribución de géneros
    plt.figure(figsize=(12, 6))
    sns.countplot(x=df_genre_exploded, order=df_genre_exploded.value_counts().index, legend=False)
    plt.title('Distribución de Géneros')
    plt.xlabel('Género')
    plt.ylabel('Número de Películas')
    plt.xticks(rotation=45, ha='right')
    

    df_exploded = df.explode('genre_ids')

    # Convertir 'popularity' a tipo numérico
    df_exploded['popularity'] = pd.to_numeric(df_exploded['popularity'], errors='coerce')

    # Ordenar los géneros por popularidad promedio de manera descendente
    sorted_genres = df_exploded.groupby('genre_ids')['popularity'].mean().sort_values(ascending=False).index

    # Crear el gráfico de barras
    plt.figure(figsize=(12, 6))
    sns.barplot(x='genre_ids', y='popularity', data=df_exploded, order=sorted_genres)
    plt.title('Popularidad Promedio por Género')
    plt.xlabel('Género')
    plt.ylabel('Popularidad Promedio')
    plt.xticks(rotation=45, ha='right')
   
    plt.show()

    
    return 

    