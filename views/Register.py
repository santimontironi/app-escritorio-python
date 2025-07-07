import tkinter as tk
from controllers.employee import Employee
from views.Dashboard import dashboard_window

def register_window():

    window = tk.Tk()

    window.title("Registrarse")
    window.configure(bg="lightblue")
    window.geometry("650x400")

    titulo = tk.Label(window, text="Registro", font=("Times New Roman", 35, "bold"), bg="lightblue")
    titulo.pack(pady=(15))

    contenedor = tk.Frame(window,relief="raised",bd=4)
    contenedor.pack(expand=True)  # se centra vertical y horizontalmente
        
    tk.Label(contenedor, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
    entry_nombre = tk.Entry(contenedor)
    entry_nombre.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(contenedor, text="Apellido:").grid(row=1, column=0, padx=10, pady=10)
    entry_apellido = tk.Entry(contenedor)
    entry_apellido.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(contenedor, text="Correo:").grid(row=2, column=0, padx=10, pady=10)
    entry_correo = tk.Entry(contenedor)
    entry_correo.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(contenedor, text="Clave:").grid(row=3, column=0, padx=10, pady=10)
    entry_clave = tk.Entry(contenedor, show="*")
    entry_clave.grid(row=3, column=1, padx=10, pady=10)
    
    def sendData():
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        correo = entry_correo.get()
        clave = entry_clave.get()
        
        newEmployee = Employee(nombre,apellido,correo,clave)
        
        if newEmployee.register():
            window.destroy()
            dashboard_window()


    tk.Button(contenedor, text="Registrarse", bg="lightgreen", command=sendData).grid(row=4, column=0, columnspan=2, padx=20, pady=20)


    window.mainloop()