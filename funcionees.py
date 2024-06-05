def sumar_2_numeros():
    num1 = validar_numero()
    num2 = validar_numero()
    total=num1+num2
    print("FUNCIÓN:El total de la suma es:",total)

def restar_2_numeros(p_num1, p_num2):
    total = p_num1 - p_num2
    print("El total de la resta es:",total)

def multiplicar_2_números():
    num1 = validar_numero()
    num2 = validar_numero()
    total = num1*num2
    return total

def dividir_2_numeros(p_num:int, p_num2:int):
    total = p_num/p_num2
    return total

def validar_numero():
    while True:
        try:
            num=float(input("Ingrese número: "))
            break
        except:
            print("ERROR! debe ingresar un número entero")
    return num


def menu():
    print("""\tMenú
    1)Sumar 2 números
    2)Restar 2 números
    3)Multiplicar 2 números
    4)Dividir 2 números""")

def validar_opciones(opciones):
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in opciones:
                break
            else:
                print("ERROR! Opción incorrecta")
        except:
            ("ERROR! debe ingresar un número entero")
    return opc
