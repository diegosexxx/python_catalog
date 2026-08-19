

Catalogo_album = {
                "Blonde": {"Artista:": "Frank Ocean" , "Canciones": "17", "Puntuacion del album": "16" }}
while True:
        print("Catalogo Albums")

       

        Catalogo_menu = input(""" Seleccione una opcion:
        1. Agregar album
        2. Ver catalogo completo
        """
        )

        if Catalogo_menu == "1":

                album = input("Agregue el nombre del Album: ")
                artista = input("Agregue el nombre del artista: ")
                canciones = input("Cantidad de canciones: ")
                puntuacion = input("Puntuacion del album: ")

                Catalogo_album[album] = {
                        "Artista": artista,
                        "Canciones": canciones,
                        "Puntuacion del album": puntuacion
                }

        if Catalogo_menu == "2":
                print(Catalogo_album)
                





















