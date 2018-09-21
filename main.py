
from opereacion import *

archivo = open('lista.txt', 'r')
leer_fila = archivo.readlines()
archivo.close()
print("nombres desosdernados")

for lista in leer_fila:
    # revisamos si tiene un salto de linea al final para quitarlselo.
    if lista[-1]=="\n":
        dato=lista[:-1].split(",")
    else:
        dato=lista.split(", ")

    for linea in dato:
        print(linea)


print("\n1.- ordenamiento de nombres: ")
print ("2.-Busqueda de nombres")
opcion=int(input("seleccione una opcion: "))
b=False
prototipo=leernombres(leer_fila,b)

if opcion==1:
    prototipo.ordenamiento()
elif opcion==2:
    prototipo.busqueda_1()
else:
    print("opcion incorrecta...")


