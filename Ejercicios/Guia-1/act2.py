print("Calculadora de años biciestos")

año = int(input("Escriba un año para saber si es biciesto o no?"))

resultado = año % 4 == 0 and año % 100 != 0 or año % 400 == 0

if resultado == 1:
    print(f"{año} es un año bisiesto")
else:
    print(f"{año} no es un año bisiesto")