import tkinter as tk
from controllers.employee import Employee
from views.Dashboard import dashboard_window

def login_window():

    window = tk.Tk()

    window.title("Ingreso")
    window.configure(bg="purple")
    window.geometry("650x400")
    
    
    title = tk.Label(window, text="Ingreso", font=("Times New Roman", 35, "bold", "underline"), bg="lightblue")
    title.pack(pady=(15))
    
    container = tk.Frame(window,relief="raised",bd=4)
    container.pack(expand=True)
    
    tk.Label(container, text="Correo:", font=("Helvetica", 10)).grid(row=2, column=0, padx=10, pady=10)
    entry_email = tk.Entry(container)
    entry_email.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(container, text="Clave:", font=("Helvetica", 10)).grid(row=3, column=0, padx=10, pady=10)
    entry_password = tk.Entry(container, show="*")
    entry_password.grid(row=3, column=1, padx=10, pady=10)
    
    def sendData():
        email = entry_email.get()
        password = entry_password.get()
        
        if Employee.login(email,password):
            window.destroy()
            dashboard_window()


    tk.Button(container, text="Iniciar sesión", bg="lightgreen", command=sendData, font=("Helvetica",10)).grid(row=4, column=0, columnspan=2, padx=20, pady=20)
    
    
    window.mainloop()