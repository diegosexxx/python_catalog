



print("Catalogo Albums")

Catalogo_album = {
        "Blonde": {"Artista:": "Frank Ocean" , "Canciones": "17", "Puntuacion del album": "16" }}

album = input("Agregue el nombre del Album: ")
artista = input("Agregue el nombre del artista: ")
canciones = input("Cantidad de canciones: ")
puntuacion = input("Puntuacion del album: ")

Catalogo_album[album] = {
        "Artista": artista,
        "Canciones": canciones,
        "Puntuacion del album": puntuacion
    }

print  (Catalogo_album)
    






















