from bd import queryFunction
from tkinter import messagebox

class Client():
    def __init__(self,nombre,apellido,telefono,turno,activo):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.turno = turno
        self.activo = activo
        
    def register(self):
        
        repeatClient = "SELECT * FROM clientes WHERE telefono = ? and activo = ?"
        resultRepeatClient = queryFunction(repeatClient, (self.telefono, self.activo), fetch=True)
    
        if resultRepeatClient:
            messagebox.showwarning("Error", "Este empledo ya está activo en el sistema.")
            return False
        
        query = "INSERT INTO clientes(nombre,apellido,telefono,turno) VALUES (?,?,?,?)"
        results = queryFunction(query,(self.nombre,self.apellido,self.telefono,self.turno),fetch=False)
    
        if results:
            messagebox.showinfo("Éxito","Cliente agregado correctamente.")
            return True