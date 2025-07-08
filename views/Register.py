import tkinter as tk
from controllers.employee import Employee
from views.Dashboard import dashboard_window
from views.Login import login_window
from PIL import Image, ImageTk 

def register_window():

    window = tk.Tk()
    
    window.title("Registrarse")
    window.geometry("700x400")
    
    # sec carga y se dimensiona la imagen
    bg_image = Image.open("assets/img/fondoRegistro.jpeg")
    bg_image = bg_image.resize((700, 400))
    bg_photo = ImageTk.PhotoImage(bg_image)

    # se coloca la imagen de fondo
    bg_label = tk.Label(window, image=bg_photo)
    bg_label.image = bg_photo  
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    title = tk.Label(window, text="Registro", font=("Times New Roman", 35, "bold", "underline"), bg="lightblue")
    title.pack(pady=(15))

    container = tk.Frame(window,relief="raised",bd=4)
    container.pack(expand=True)  # se centra vertical y horizontalmente
        
    tk.Label(container, text="Nombre:", font=("Helvetica", 10)).grid(row=0, column=0, padx=10, pady=10)
    entry_name = tk.Entry(container)
    entry_name.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(container, text="Apellido:", font=("Helvetica", 10)).grid(row=1, column=0, padx=10, pady=10)
    entry_surname = tk.Entry(container)
    entry_surname.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(container, text="Correo:", font=("Helvetica", 10)).grid(row=2, column=0, padx=10, pady=10)
    entry_email = tk.Entry(container)
    entry_email.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(container, text="Clave:", font=("Helvetica", 10)).grid(row=3, column=0, padx=10, pady=10)
    entry_password = tk.Entry(container, show="*")
    entry_password.grid(row=3, column=1, padx=10, pady=10)
    
    def sendData():
        name = entry_name.get()
        surname = entry_surname.get()
        email = entry_email.get()
        password = entry_password.get()
        
        newEmployee = Employee(name,surname,email,password)
        
        if newEmployee.register():
            window.destroy()
            dashboard_window()


    tk.Button(container, text="Registrarse", bg="lightgreen", command=sendData, font=("Helvetica",10)).grid(row=4, column=0, columnspan=2, padx=20, pady=20)
    
    def clickLogin(event=None):
        window.destroy()
        login_window()
    
    or_login = tk.Label(window, text="O inicie sesión", fg="blue", cursor="hand2", font=("Helvetica", 10, "underline"))
    or_login.pack()

    or_login.bind("<Button-1>", clickLogin)


    window.mainloop()