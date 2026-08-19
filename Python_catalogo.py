

Catalogo_album = {
                "Blonde": {"Artista": "Frank Ocean" , "Canciones": "17", "Puntuacion del album": "16" }}




while True:
        print("""

        \n CATALOGO ALBUMS

        """)

       

        Catalogo_menu = input(""" Seleccione una opcion:
        1. Agregar album
        2. Ver catalogo completo
        3. Modificar atributo existente
        4. Salir
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

        elif Catalogo_menu == "2":

                print(Catalogo_album)

        elif Catalogo_menu == "3":
                while True:
                        album_a_editar = input("Que album desea editar?: ")

                        if album_a_editar in Catalogo_album:
                                print("""Que atributo desea editar?
                                1. Album
                                2. Artista
                                3. Numero de canciones
                                4. Puntuacion del album  """)

                                atributo_a_editar = input()

                                if atributo_a_editar == "1":
                                        Nombreart_nuevo = input("Que nombre desea poner al album?: ")
                                        Catalogo_album[Nombreart_nuevo] = Catalogo_album.pop(album_a_editar)
                                        print("Catalogo actualizado")
                                        break

                                elif atributo_a_editar == "2":
                                        artista_nuevo = input("Nuevo artista: ")
                                        Catalogo_album[album_a_editar]["Artista"] = artista_nuevo
                                        print("Catalogo actualizado")
                                        break

                                elif atributo_a_editar == "3":
                                        num_nuevo = input("Nuevo num de canciones: ")
                                        Catalogo_album[album_a_editar]["Canciones"] = num_nuevo
                                        print("Catalogo actualizado")
                                        break

                                elif atributo_a_editar == "4":
                                        punt_nuevo = input("Nuevo num de canciones: ")
                                        Catalogo_album[album_a_editar]["Puntuacion del album"] = punt_nuevo
                                        print("Catalogo actualizado")
                                        break

                                else:
                                        print("""
                                        \nOpcion no disponible: Seleccione entre 1 a 4""")

                        else:
                                print("""
                                Album no encontrado
                                """)

        elif Catalogo_menu == "4":
                break

        else:
                print("""
                \nOpcion no disponible: Seleccione entre 1 a 4""")
                        
                





















