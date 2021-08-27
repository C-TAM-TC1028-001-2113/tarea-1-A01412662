def main():
    # escribe tu código abajo de esta línea
    mes_anterior = float (input("Dame el saldo del mes anterior: "))
    ingresos = float (input("Dame los ingresos: "))
    egresos = float (input("Dame los egresos: "))
    cheques = int (input("Dame el número de cheques: "))

    sin_interes = (mes_anterior + ingresos - egresos - (cheques * 13))
    con_interes = (sin_interes) - (sin_interes * .075)

    print("El saldo final de la cuenta es:",con_interes)

if __name__ == '__main__':
    main()
