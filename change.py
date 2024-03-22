def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("\n" + "Vuelto")
    print("\n" + "Pesos:")
    print(int(money - expense))
    print("Centavos:")
    vuelto_real=(float(money - expense))
    centavos= ((vuelto_real - int(money - expense))*100)
    print(int(centavos))
change()
