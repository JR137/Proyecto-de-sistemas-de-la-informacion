if __name__=='__main__':
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

    # Obtener el género a buscar
    genero_buscado = "Action"  # Reemplaza con el género que desees buscar

    # Consulta para obtener las películas del género especificado
    query = f"SELECT * FROM peliculas WHERE genero LIKE '%\"name\": \"{genero_buscado}\"%'"

    # Ejecutar la consulta
    cursor.execute(query)

    # Obtener los resultados
    resultados = cursor.fetchall()

    # Mostrar las películas encontradas
    for pelicula in resultados:
        print("ID Película:", pelicula[0])
        print("---")

    # Cerrar la conexión
    conn.close()
