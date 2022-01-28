class Cargo:
    Secuencia=3
    categorias = [{"Nombre":1, "Cargo":"Asistente"},{"Nombre":2,"Cargo":"Supervisor"},{"Nombre":3, "Cargo":"Gerente"}]
    def __init__(self, Categoria):
        Cargo.Secuencia +=1
        self.codigo=Cargo.secuencia
        self,cargo=Categoria
        def mostrar(self):
            print ("{} - {} - {}".format(self.Codigo,self.Cargo))
            
            
        def datos(self):
            return [self.Codigo,self.Cargo]
        
        def registro(self):
            return {"Codigo": self.Codigo, "Cargo": self.Cargo}

ListaCategoria = []