# import os
# os.system("cls")
class Calculo:
    pass

class Gerente:
    def __init__(self):
        x=20
        pass
    
    def menu(self,Opciones,Titulo):
        print(Titulo)
        for Opcion in Opciones:
            opcion = input("Elija Ocion [1...{}]: ".format(len(Opciones)))
            return Opcion
        