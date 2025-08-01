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
        
        checkClient = "SELECT * FROM clientes WHERE dia = ? AND hora = ? AND activo = ?"
        result = queryFunction(checkClient, (self.dia, self.hora, True), fetch=True)
        
        if result:
            messagebox.showwarning("Error", "Ya hay un cliente con ese día y hora activos.")
            return False
        
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
        
    def update(self, client_id):
        
        check_query = """
            SELECT * FROM clientes 
            WHERE dia = ? AND hora = ? AND activo = ? AND id != ?
        """
        result = queryFunction(check_query, (self.dia, self.hora, True, client_id), fetch=True)

        if result:
            messagebox.showwarning("Error", "Ya existe un cliente con ese día y hora activos.")
            return False

        query = """
        UPDATE clientes 
        SET nombre = ?, apellido = ?, telefono = ?, dia = ?, hora = ?
        WHERE id = ?
        """
        result = queryFunction(query, (self.nombre, self.apellido, self.telefono, self.dia, self.hora, client_id), fetch=False)
        
        if result is not None:
            messagebox.showinfo("Éxito", "Cliente actualizado correctamente.")
            return True
        else:
            messagebox.showerror("Error", "No se pudo actualizar el cliente.")
            return False
        












        
 