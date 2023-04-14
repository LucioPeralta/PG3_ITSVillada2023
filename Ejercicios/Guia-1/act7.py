def es_numero_step(numero):
    numero_str = str(numero)  # se converte el número a una cadena de caracteres
    longitud = len(numero_str)
    
    if longitud < 2:  # un numero de un solo digito no puede ser un numero step
        return False
    
    es_ascendente = True
    es_descendente = True
    
    for i in range(1, longitud):
        if int(numero_str[i]) != int(numero_str[i-1]) + 1:
            es_ascendente = False
        
        if int(numero_str[i]) != int(numero_str[i-1]) - 1:
            es_descendente = False
        
        if not es_ascendente and not es_descendente:  # si el numero no es ni ascendente ni descendente, no es un numero step
            return False
    
    return True

numero = input("Escribe un número: ")

if es_numero_step(numero):
    print(f"{numero} es un número Step.")
else:
    print(f"{numero} no es un número Step.")
