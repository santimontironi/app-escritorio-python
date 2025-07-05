from bd import queryFunction

class Employee:
    def __init__(self,nombre,apellido,correo,clave):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.clave = clave
        
    def checkEmployee(self):
        repeatEmployee = "SELECT * FROM empleados WHERE correo = ?"
        resultRepeatEmployee = queryFunction(repeatEmployee (self.correo,), fetch=True)
    
        if resultRepeatEmployee:
            print("Usuario repetido")
            return

    def register(self):
        query = "INSERT INTO empleados(nombre,apellido,correo,clave) VALUES (?,?,?,?)"
        resultados = queryFunction(query,(self.nombre,self.apellido,self.correo,self.clave),fetch=False)
    
        if resultados:
            print("Empleado registrado:")

            
