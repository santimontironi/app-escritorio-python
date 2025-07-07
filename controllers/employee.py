from bd import queryFunction
from tkinter import messagebox

class Employee:
    def __init__(self,nombre,apellido,correo,clave):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.clave = clave

    def register(self):
        
        repeatEmployee = "SELECT * FROM empleados WHERE correo = ?"
        resultRepeatEmployee = queryFunction(repeatEmployee, (self.correo,), fetch=True)
    
        if resultRepeatEmployee:
            messagebox.showwarning("Error", "Ya existe un empleado con este e-mail, vuelva a intentarlo.")
            return False
        
        query = "INSERT INTO empleados(nombre,apellido,correo,clave) VALUES (?,?,?,?)"
        results = queryFunction(query,(self.nombre,self.apellido,self.correo,self.clave),fetch=False)
    
        if results:
            messagebox.showinfo("Éxito","Empleado registrado correctamente.")
            return True

            
    def login(correo,clave):
        loginQuery = "SELECT * FROM empleados WHERE correo = ? and clave = ?"
        resultsLogin = queryFunction(loginQuery, (correo, clave), fetch=True)
        
        if resultsLogin:
            messagebox.showinfo("Login exitoso","Ha iniciado sesión correctamente")
            return True
        else:
            messagebox.showwarning("Error", "Credenciales incorrectas, vuelva a intentarlo.")
            return False