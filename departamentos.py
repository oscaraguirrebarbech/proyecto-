class Departamentos: 
    Secuencia=2
    departamentos =[{"Departamentos":1, "Nombre":"bienestar", "Departamentos":2, "Nombre":"Salud"}]
    def __int__(self,Descripcion):
        Departamentos.Secuencia +=2
        self.Codigo= Departamentos.Secuencia
        self.departamentos=Descripcion
    def Registro(self):
        return {"Departamentos":self.Codigo, "Nombre":self.departamentos}
    
