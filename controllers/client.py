from bd import queryFunction
from tkinter import messagebox

class Client():
    def __init__(self,nombre,apellido,telefono,dia,hora,activo):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.dia = dia
        self.hora = hora
        self.activo = activo
        
    def register(self):
        
        repeatClient = "SELECT * FROM clientes WHERE telefono = ? and activo = ?"
        resultRepeatClient = queryFunction(repeatClient, (self.telefono, self.activo), fetch=True)
    
        if resultRepeatClient:
            messagebox.showwarning("Error", "Este empledo ya está activo en el sistema.")
            return False
        
        query = "INSERT INTO clientes(nombre,apellido,telefono,dia,fecha) VALUES (?,?,?,?,?)"
        results = queryFunction(query,(self.nombre,self.apellido,self.telefono,self.dia,self.hora),fetch=False)
    
        if results:
            messagebox.showinfo("Éxito","Cliente agregado correctamente.")
            return True