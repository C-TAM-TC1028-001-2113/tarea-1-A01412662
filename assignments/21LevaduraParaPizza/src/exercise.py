def main():
    # escribe tu código abajo de esta línea
    gramos = float(input("Dame la harina en gramos: "))

    levadura = float ()

    levadura = (gramos* 50) / 1000

    levadura = round(levadura, 1)
    
    print ("Necesitas estos gramos de levadura:",levadura)


if __name__ == '__main__':
    main()
