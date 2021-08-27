def main():
    # escribe tu código abajo de esta línea
    mensajes = int (input("Dame el número de mensajes: "))
    megas = float (input("Dame el número de megas: "))
    minutos = int (input("Dame el número de minutos: "))

    costo = (mensajes*.80)+(megas*.80)+(minutos*.80)
    print("El costo mensual es:",costo)




if __name__ == '__main__':
    main()
