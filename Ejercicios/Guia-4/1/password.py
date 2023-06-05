def validate_password(password):
    return (tiene_suficiente_longitud(password) and
            tiene_letra_mayuscula(password) and
            tiene_letra_minuscula(password) and
            tiene_numero(password) and
            no_contiene_caracteres_especiales(password))

def tiene_suficiente_longitud(password):
    return len(password) >= 8

def tiene_letra_mayuscula(password):
    return any(c.isupper() for c in password)

def tiene_letra_minuscula(password):
    return any(c.islower() for c in password)

def tiene_numero(password):
    return any(c.isdigit() for c in password)

def no_contiene_caracteres_especiales(password):
    caracteres_especiales = "!@#$%^&*()-_+=<>,.?/|"
    return not any(c in caracteres_especiales for c in password)
