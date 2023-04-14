while True:
    try:
        numero = int(input("Ingrese un numero: "))
        numero2 = int(input("Ingrese otro numero: "))
        
        resultado = numero+numero2
        print(resultado)

    except ValueError:
        print("El valor ingresado no es valido")

    finally:
        seguir = input("Desea seguir? (si/no): ")
        

        if seguir == "no":
            break
