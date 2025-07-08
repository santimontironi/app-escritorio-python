import tkinter as tk
from views.AddClient import addClient_window
from controllers.client import Client
from tkinter import ttk

def dashboard_window():
    
    from views.Login import login_window

    window = tk.Tk()

    window.title("Panel")
    window.configure(bg="lightgreen")
    window.geometry("700x400")
    
    title = tk.Label(window, text="Panel", font=("Times New Roman", 35, "bold", "underline"), bg="lightblue")
    title.pack(pady=(15))
    
    container = tk.Frame(window, relief="raised", bd=4, width=700)
    container.pack()
    
    tree = ttk.Treeview(container, columns=("ID", "Nombre", "Apellido", "Teléfono", "Día", "Hora"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Apellido", text="Apellido")
    tree.heading("Teléfono", text="Teléfono")
    tree.heading("Día", text="Día")
    tree.heading("Hora", text="Hora")

    tree.column("ID", width=40, anchor="center", stretch=False)
    tree.column("Nombre", width=120, anchor="center", stretch=False)
    tree.column("Apellido", width=120, anchor="center", stretch=False)
    tree.column("Teléfono", width=130, anchor="center", stretch=False)
    tree.column("Día", width=100, anchor="center", stretch=False)
    tree.column("Hora", width=100, anchor="center", stretch=False)

    tree.pack()

    def load_clients():
        client = Client(None, None, None, None, None)
        clients = client.selectAll()

        if clients:
            for row in clients:
                id, nombre, apellido, telefono, dia, hora = row
                
                # formatear 'dia' si es datetime.date
                if hasattr(dia, 'strftime'):
                    dia = dia.strftime("%Y-%m-%d")
                
                # Convertir 'hora' a string por si acaso
                hora = str(hora)
                
                tree.insert("", tk.END, values=(id, nombre, apellido, telefono, dia, hora))

    load_clients()
    
    def toAddClient(event=None):
        window.destroy()
        addClient_window()
    
    btnToAddClient = tk.Label(window, text="Agregar nuevo cliente", fg="blue", cursor="hand2", font=("Helvetica", 10, "underline"))
    btnToAddClient.pack(pady=10)

    btnToAddClient.bind("<Button-1>", toAddClient)
    
    def logout(event=None):
        window.destroy()
        login_window()
    
    btnLogout = tk.Label(window, text="Cerrar sesión", fg="red", cursor="hand2", font=("Helvetica", 10, "underline"))
    btnLogout.pack(anchor="ne", padx=10, pady=10)

    btnLogout.bind("<Button-1>", logout)
    
    window.mainloop()