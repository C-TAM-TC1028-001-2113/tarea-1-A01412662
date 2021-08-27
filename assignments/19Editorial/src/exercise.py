from typing import TYPE_CHECKING


def main():
    # escribe tu código abajo de esta línea
    num_paginas = int (input("Dame el número de palabras : "))

    costo = ((num_paginas / 475) * 60)+ 60
    costo_variaspag = costo - (costo * .10)
    costo_unapag = 60- (60*.10)


    print ("El costo de la publicación es:",costo_variaspag)






if __name__ == '__main__':
    main()
