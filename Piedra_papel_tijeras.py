import random
# Ventana de Seleccion
while True:
    aleatorio = random.randrange(0, 3)
    Computador_Elije = ""
    print ("-------------Yᵒᵘ Oᶰˡʸ Lᶤᵛᵉ Oᶰᶜᵉ---------------------------------")
    print ("------------------------Yᵒᵘ Oᶰˡʸ Lᶤᵛᵉ Oᶰᶜᵉ-----------------------")
    print ("Seleciones una jugada")
    print("1)Piedra")
    print("2)Papel")
    print("3)Tijera")
    print ("4)Salir del Juego")
    opcion = input("Elija una Jugada:")

    # modo de interaccion con el Juego utilizamos el control FLow
    Jugador_Elije=""
    if opcion == "1":
        Jugador_Elije = "piedra"
    elif opcion == "2":
        Jugador_Elije = "papel"
    elif opcion == "3":
        Jugador_Elije = "tijera"
    elif opcion == "4":
        print ("----------┬┴┬┴┤(･_├┬┴┬┴-----------------------------------")
        print ("-------Hasta Pronto ／人◕ __ ◕人＼---┬┴┬┴┤(･_├┬┴┬┴--------")
        break
    else:
        print ("por favor elegir valores validos de las opciones mostradas del 1 al 3")
    
    if Jugador_Elije:
        print("Tu elejiste : ", Jugador_Elije)

        # modo de interaccion con el juego de la Maquina

        if aleatorio == 0:
            Computador_Elije = "piedra"
        elif aleatorio == 1:
            Computador_Elije = "papel"
        elif aleatorio == 2:
            Computador_Elije = "tijera"
        print("El computador ha elijido: ", Computador_Elije)
        print(".!!!! ")

        # modo de interaccion del juego ganas pierdes o empate

        if Computador_Elije == "papel" and Jugador_Elije == "piedra":
            print("perdiste, papel es envuelto por piedra (╥﹏╥)")
        elif Computador_Elije == "tijera" and Jugador_Elije == "papel":
            print("perdiste, Tijera corta el papel  (╥﹏╥)")
        elif Computador_Elije == "piedra" and Jugador_Elije == "tijera":
            print("perdiste, Piedra pisa a la tijera  (╥﹏╥)")
        if Computador_Elije == "piedra" and Jugador_Elije == "papel":
            print("Ganaste, papel envuelve a la piedra \(^-^)/ ")
        elif Computador_Elije == "papel" and Jugador_Elije == "tijera":
            print("Ganaste, Tijera corta el papel \(^-^)/ ")
        elif Computador_Elije == "tijera" and Jugador_Elije == "piedra":
            print("Ganaste, Piedra pisa a la tijera \(^-^)/ ")
        elif Computador_Elije == Jugador_Elije:
            print("Empate¯\_(ツ)_/¯ " + (Computador_Elije))