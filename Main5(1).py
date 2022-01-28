
from pydoc import Helper
from Helpers import Departamento, Helpers
from Cargo import Cargo
from Empleados import Empleado, Empleados
import os

def buscategoria(Codigo):
    Cargo = 0
    Codigo = 0
    for Pos in range(0,len(Empleados.Empleados)):
        Cargo = Cargo.Cargo[Pos]
        if Empleados["Codigo"] == Codigo:
            Cargo=Empleados ["Cargo"]
            break
        return Cargo
def buscarDepartamento(departamentos):
    Departamentos = 0
    for pos in range (0,len(Departamentos.Departametnos)):
        departamento=departamentos.Departamentos[pos]
        if Departamentos["Nombre"] ==Departamentos:
            Departamentos=Departamentos["Nombre"]
            break
    return Departamentos
            
            
Helpers=Helpers()
Lista= ["1) Cargo", "2) Helpers", "3) Empleados", "4 Salir"]
Opcion =" "
while Opcion !="4":
    os.system ("cls")
    Opcion = Helpers.Menu(Lista,"Menu Ficha Personal")
    if Opcion == "1":
        Opc1 =" "
        while Opc1 != "3":
            os.system("cls")
            print("*"*20, "Mantenimiento De Cargos","*"*20)
        Opc1 = Helpers.Menu(["1) Ingreso", "2) Consulta", "3) Salir"], "Menu Cargos")
        os.system("cls")
        if Opc1 == "1":
            print("*"*20,"Ingreso De Cargos","*"*20)
            Nombre= input("Nombre De Cargos: ")
            val =len(Nombre)
            Cargo=Cargo(Nombre)
            Cargo=Cargo.Registro()
            Cargo.Cargo.append(Cargo)
            input("\n")
            "Datos Ingresados De Manera Correcta, Presione Una Tecla Para Continuar.."
        elif Opc1 =="2":
          print("*"*20, "Lista De Cargo ","*"*20)  
          print("Codigo"," "*5, "Descripcion"," ")
          for Cargo in Cargo.Cargo:
              Codigo= Cargo ["Codigo"]
              Descripcion= Cargo ["Cargo"]
              Codigo = buscarcargo(Descripcion)
              print(" "*2, Codigo," "*8,Codigo)
              print("*"*59)
              input("\n"
                "Presione Una Tecla Para Continuar..")                 
        elif Opc1 == "3":
            input("Espere!!"
            "\n"  <"Gracias Por Esperar. Presione Una Tecla Para Continuar..." )
            break
        
        elif Opc1 =="2":
            os.system("cls")
            Opc1 = " "
            while Opc1 != 3:
                os.system("cls")
                print("*"*20,"Mantenimiento De Departamentos","*"*20)
                Opc1= Helpers.Menu(["1) ingreso", "2) consulta", "3) salair"],"sub-,menu Departamento")
                os.system("cls")
                if Opc1 =="1":
                    print("*"*20, "ingreso de departamento","*"*20)
                    nombre = input("nombre del departamento: ")
                    val =len(nombre)
                    while not val >5 and val <=20:
                        nombre =input("nombre del departamento:")
                        val = len(nombre)
                        Departamento=Departamento(nombre)
                        Departamento.departamento.append(Departamento)
                        input("\n"
                            "datos ingresados exitosamente, presione una tecla para continuar..")
        elif Opc1== "2":
            print("*"*20, "lista de departamentos","*"*20)
            print("departamento",""*5, "nombre", " ")
            for departamento in departamento.departamentos:
                departamento= departamento["departamento"]
                dnombre=departamento["nombre"]
                nombred= buscarDepartamento(dnombre)
                print(" "*4,departamento, " "*8,nombred)
                print("*"*66)
                input("\n" "presione una trecla para continuar..")
        elif Opc1 == "3":
         input("espere"
               "\n" "presione una tecla para continuar..")
         break
        
        elif Opcion == "3":
            os.system("cls")
            Opc1=""
            while Opc1 !=3:
                os.system("cls")
                print("*"*20, ",manteniemiento de empleados", "*"*20)
                Opc1 = Helpers.menu(["1 )ingreso ", "2) consulta", "3 ) salir"], "sub-menu empleados")
                os.system("cls")
                if Opc1 == "1":
                    print("*"*20,"ingreso de empleados", "*"*20)
                    nombre = input("nombre de empleados: ")
                    val = len(nombre)
                    cedula= input("cedula de empleados ")
                    val = len(cedula)
                    while val !=10:
                        cedula=input("cedula del empleado: ")
                        val =len(cedula)
                        codigocargo=input("cargo del empleado ")
                        cargo= buscarcargo(codigocargo)
                        while cargo != codigocargo:
                            codigocargo= input("cargo del empleado ")
                            cargo=buscarcargo(codigocargo)
                            departamento=input("departamento del empleado ")
                            departamento=buscarDepartamento(departamento)
                            while departamento!=departamento:
                                departamento=input("departamento del empleado ")
                                departamento=buscarDepartamento(departamento)
                                sueldo=float(input("sueldo del empleado: "))
                                while sueldo %1 ==0:                                               
        elif opc1 =="3":       
    os.system("cls")
    Opc1 = ""
    while Opc1 !=3:
        os.system("cls")
        print("*"*20, "mantenimiento de empleados","*"*20)
        Opc1 = Helpers.menud(["1) ingreso", "2) consultar", "3) salir"], "sub-menu emppleados ")
        os.system("cls")
        if Opc1=="1":
            print("*"*20, "ingreso de empleados", "*"*20)
            nombre= input("nombre de empleados: ")
            val= len(nombre)
            cedula= input("cedula del empleado: ")
            val = len(cedula)
            while not val >=3 and val <=20:
                nombre= input("nombre del empleado: ")
                val= len(nombre)
                cedula =input("cedula del empleado: ")
                val = len(cedula)
                while val != 10:
                    cedula =input("cedula del empleado: ")
                    val =len(cedula)
                    codigocargo= buscarcargo(codigocargo)
                    while cargo !=codigocargo:
                        codigocargo = input("cargo del empleado: ")
                        cargo =buscarcargo(codigocargo)
                        departamento = input("departamento del empleado: ")
                        departamento=buscarDepartamento(departamento)
                        while departamento != departamento:
                            departamento= input("departamento del empleado: ")
                            departamento=buscarDepartamento(departamento)
                            sueldo= float(input("sueldo del empleado: "))
                            while sueldo %1 ==0:
                                sueldo=float(input("sueldo del empleado: "))
                                Empleados=Empleados(nombre,cedula,codigocargo,departamento,sueldo)
                                Empleados=Empleados.registro()
                                Empleados.Empleados.append(Empleados)
                                input("\n"
                                      "datos ingresados exitosamente", "presione una tecla para continuar.." )
        elif Opc1 =="2":
            print("*"*35, "lista de empleados", "*"*35)
            print("codigo"," "*6, "nombre"," "*6,"cedula"," "*6,"cargo"," "*6, "departamento"," ",*6, "sueldo")
        for Empleados in Empleados.Empleados:
            codigo= Empleados["codigo"]
            desno=Empleado["nombre"]
            codigo=Empleados["cedula"]
            cargo=Empleados["cargo"]
            buscarcargo=buscarcargo(cargo)
            departamento =Empleados["departamento"]
            buscarDepartamento=buscarDepartamento(departamento)
            sueldo=Empleado["sueldo"]
            print(" "*2,codigo," "*8,desno," "*(10-len(desno)),cedula," "*14-len(cedula)),buscarcargo," "*(11-len(buscarcargo)),buscarDepartamento," "*18-len(buscarcargo))
            print("*"*92)
            input("\n"
                  "presione una tecla para continuar..")
        elif Opc1 =="3":
            input("espere"
                  "gracias por su espera. presione cualquier tecla para continuar..")
            break
        elif opcion =="4":
            print ("gracias pro preferinos")
            
            
            
            
        
            
            
            
            
            
                                
                        
                        
                
                        
       
                
           
                
              
              
              
            
            
        
    

    
  
    
        
 
     
    
  
  

    
    
    
         
    
        
        





































