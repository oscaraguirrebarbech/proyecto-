from Cargo import Cargo

class Empleado:
    secuencia =3 
    Empleados = [ {"Codigo": 1, "Nombre": "Oscar", "Cedula": "0951802511", "Cargo": 1, "Gerente": 1, "Sueldo": "800.00"},
                  {"Codigo": 2, "Nombre": "Cesar", "Cedula": "0951804475", "Cargo": 2, "SubGerente": 2, "Suelo": "700.00" },
                  {"Codigo": 3, "Nombre": "Angel", "cedula": "0951808377", "Cargo": 3, "TalentoHumano": 3, "Sueldo": "600.00"}
                  
                  ]
    def __init__(self,Nombre,Cedula,CodGerente,CodCargo,Sueldo):
           Empleado.secuencia +=1
           self.Codigo =Empleado.Secuencia 
           self.Nombre =Nombre
           self.Cedula =Cedula 
           self.Cargo =CodCargo
           self.Gerente=CodGerente
           self.Sueldo =Sueldo
           
    def Mostrar(self):
      print("{} - {} - {} - {} - {}".format(self.Codigo,self.Nombre,self.cargo,self.Gerente,self.Sueldo,))
    
    def Registro(self):
      return {"Codigo": self.Codigo, "Nombre": self.Nombre, "Cedula": self.cedula, "Cargo": self.Cargo, "Gerente": self.Gerente, "SUELDO": self.Sueldo}
    