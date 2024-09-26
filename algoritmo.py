if __name__=='__main__':
    import numpy as np
    import pandas as pd
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    import mariadb

    # Establecer los parámetros de conexión
    config = {
        'user': 'psi_grupo7',
        'password': '1234',
        'host': '195.235.211.197',
        'port': 3306,
        'database': 'psi_grupo7'
    }

    # Establecer la conexión a la base de datos
    conn = mariadb.connect(**config)
    cursor = conn.cursor()

    # Consulta SQL para obtener los datos de las películas
    query = "SELECT id_pelicula, titulo, sinopsis, genero FROM peliculas"

    # Ejecutar la consulta y obtener los resultados
    cursor.execute(query)
    results = cursor.fetchall()

    # Crear un DataFrame con los resultados
    columns = ['id_pelicula', 'titulo', 'sinopsis', 'genero']
    movies = pd.DataFrame(results, columns=columns)

    # Cerrar la conexión a la base de datos
    cursor.close()
    conn.close()


    def convert(text):
        L = []
        for i in eval(text):
            L.append(i['name'])
        return L


    movies['genero'] = movies['genero'].apply(convert)


    def collapse(L):
        L1 = []
        for i in L:
            L1.append(i.replace(" ", ""))
        return L


    movies['genero'] = movies['genero'].apply(collapse)

    movies['sinopsis'] = movies['sinopsis'].apply(lambda x: x.split())
    movies['tags'] = movies['sinopsis'] + movies['genero']

    new = movies[['titulo', 'tags']]
    new['tags'] = new['tags'].apply(lambda x: " ".join(x))

    cv = CountVectorizer(max_features=5000, stop_words='english')
    vector = cv.fit_transform(new['tags']).toarray()

    similarity = cosine_similarity(vector)


    def recommend(movie, genre):
        genre_movies = movies[movies['genero'].apply(lambda x: genre in x)]
        index = genre_movies[genre_movies['titulo'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        for i in distances[1:6]:
            print(genre_movies.iloc[i[0]].titulo)


    recommend('Batman', 'Action')
