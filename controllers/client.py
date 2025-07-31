from bd import queryFunction
from tkinter import messagebox

class Client():
    def __init__(self,nombre,apellido,telefono,dia,hora,activo = True):
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
        
        query = "INSERT INTO clientes(nombre,apellido,telefono,dia,hora) VALUES (?,?,?,?,?)"
        results = queryFunction(query,(self.nombre,self.apellido,self.telefono,self.dia,self.hora),fetch=False)
    
        if results:
            messagebox.showinfo("Éxito","Cliente agregado correctamente.")
            return True
        
    def selectAll(self):
        clientsQuery = "SELECT id,nombre,apellido,telefono,dia,hora FROM clientes"
        return queryFunction(clientsQuery,fetch=True)

    def delete(self, client_id):
        query = "DELETE FROM clientes WHERE id = ?"
        result = queryFunction(query, (client_id,), fetch=False)
        if result is not None:
            messagebox.showinfo("Éxito", "Cliente eliminado correctamente.")
            return True
        else:
            messagebox.showerror("Error", "No se pudo eliminar el cliente.")
            return False
 