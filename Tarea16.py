#  Letras o números
# """Ingrese un caracter y determine si es una lectra o numero o otra cosa """


def distinguir(a):
    if a in "1234567890":
        return "{a}  Es un numero"
    elif a in "abcdefghijklmnopqrstuvwxyz":
        return "{a}  Es una letra minuscula"
    elif a in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return " {a} Es una letra Mayuscula"
    else:
        return "No es letra ni numero"


if __name__ == "__main__":
    caract = input("Caracter por favor: ")
    print(" {distinguir(caract)}")
