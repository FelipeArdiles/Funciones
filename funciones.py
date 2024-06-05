#import funcionees as fn
#from funcionees import menu

from funcionees import *

menu()
opc=validar_opciones([1,2,3,4])

if opc==1:
    sumar_2_numeros()

elif opc==2:
    num1=validar_numero()
    num2=validar_numero()
    restar_2_numeros(num1,num2)

elif opc==3:
    total = multiplicar_2_números()
    print("Super total de la multiplicación:",total)
else:
    num1=validar_numero
    num2=validar_numero
    total = dividir_2_numeros(num1,num2)
    lista = []
    lista.append(total)
    print(lista)

