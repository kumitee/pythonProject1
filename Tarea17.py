# Escriba un programa que simule una calculadora básica,
# este puede realizar operación de suma, resta, multiplicación y división

def suma(a,b):
    return a+b


def resta(a,b):
    return a-b


def multi(a,b):
    return a*b

def div(a,b):
    return a/b


if __name__ == "__main__":
    numUno = int(input("Primer Numero: "))
    numDos = int(input("Segundo Numero: "))

    print("Selecione la operacion aritmetica:")
    print(" 1....Suma\n")
    print(" 2.....Resta\n")
    print("3.....Multiplicar\n")
    print("4.....Dividir\n")
    selT = input("Seleccion: ")
    if selT == "1":
        print(suma(numUno,numDos))
    elif selT == "2":
        print(resta(numUno,numDos))
    elif selT == "3":
        print(multi(numUno,numDos))
    elif selT == "4":
        print(div(numUno,numDos))


print("error")