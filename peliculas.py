if __name__ == '__main__':
    import mariadb
    import csv

    # Establecer los parámetros de conexión
    config = {
        'user': 'psi_grupo7',
        'password': '1234',
        'host': '195.235.211.197',
        'port': 3306,
        'database': 'psi_grupo7'
    }

    # Conectar a la base de datos
    conn = mariadb.connect(**config)
    cursor = conn.cursor()

    # Abrir el archivo CSV
    with open('tmdb_5000_movies.csv', 'r', encoding='utf-8') as archivo_csv:
        datos_csv = csv.DictReader(archivo_csv)

        for datos in datos_csv:
            # Obtener los valores de cada columna del archivo CSV
            titulo = datos['title']
            año = int(datos['release_date'].split('-')[0])
            genero = datos['genres']
            sinopsis = datos['overview']
            duracion = int(datos['runtime'])
            presupuesto = float(datos['budget'])
            idioma_original = datos['original_language']
            titulo_original = datos['original_title']
            resumen = datos['overview']
            popularidad = float(datos['popularity'])
            companias_produccion = datos['production_companies']
            paises_produccion = datos['production_countries']
            fecha_estreno = datos['release_date']
            ingresos = float(datos['revenue'])
            idiomas_hablados = datos['spoken_languages']
            estado_pelicula = datos['status']
            eslogan = datos['tagline']
            promedio_votos = float(datos['vote_average'])
            cantidad_votos = int(datos['vote_count'])

            # Ejecutar la consulta de inserción
            sql = "INSERT INTO peliculas (titulo, año, genero, sinopsis, duracion, presupuesto, idioma_original, titulo_original, resumen, popularidad, companias_produccion, paises_produccion, fecha_estreno, ingresos, idiomas_hablados, estado_pelicula, eslogan, promedio_votos, cantidad_votos) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            valores = (
                titulo, año, genero, sinopsis, duracion, presupuesto, idioma_original, titulo_original, resumen,
                popularidad, companias_produccion, paises_produccion, fecha_estreno, ingresos,
                idiomas_hablados, estado_pelicula, eslogan, promedio_votos, cantidad_votos
            )
            cursor.execute(sql, valores)
            conn.commit()

    # Cerrar la conexión a la base de datos
    cursor.close()
    conn.close()
