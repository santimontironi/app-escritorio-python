import tkinter as tk
from views.AddClient import addClient_window
from controllers.client import Client
from tkinter import ttk

def dashboard_window():

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

    tree.pack(fill="both", expand=True)

    def load_clients():
        client = Client(None, None, None, None, None)
        clients = client.selectAll()

        if clients:
            for row in clients:
                tree.insert("", tk.END, values=row)

    load_clients()
    
    def toAddClient(event=None):
        window.destroy()
        addClient_window()
    
    btnToAddClient = tk.Label(window, text="Agregar nuevo cliente", fg="blue", cursor="hand2", font=("Helvetica", 10, "underline"))
    btnToAddClient.pack()

    btnToAddClient.bind("<Button-1>", toAddClient)
    
    window.mainloop()