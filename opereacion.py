"""se define la clase"""

class leernombres:  #operaciones (identacion)

    def __init__(self,Lista_A,verificar):
        self.Lista_A=Lista_A
        self.verificar=verificar

    def ordenamiento(self):
        self.Lista_A.sort()
        for lista in self.Lista_A:
            # revisamos si tiene un salto de linea al final para quitarlselo.
            if lista[-1] == "\n":
                dato = lista[:-1].split(",")
            else:
                dato = lista.split(", ")

            for linea in dato:
                print(linea)

    def busqueda_1(self):

        palabra = input("escriba un nombre: ")
        for linea in self.Lista_A:
            if palabra in linea:
                self.verificar=True

        if self.verificar == True:
            print(palabra,"se encuentra en la lista")
        else:
            print(palabra,"no se encuentra en la lista")

