import tkinter as tk
from views.AddClient import addClient_window
from controllers.client import Client
from tkinter import ttk
from tkinter import messagebox
import tkinter.simpledialog as simpledialog

def dashboard_window():
    
    from views.Login import login_window

    window = tk.Tk()

    window.title("Panel")
    window.configure(bg="lightgreen")
    window.geometry("700x500")
    
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
        
    def logout(event=None):
        window.destroy()
        login_window()
        
    def delete_selected_client():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Atención", "Por favor seleccioná un cliente.")
            return
        
        confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de que querés eliminar este cliente?")
        if confirm:
            item = tree.item(selected_item)
            client_id = item["values"][0]

            client = Client(None, None, None, None, None)
            success = client.delete(client_id)

            if success:
                tree.delete(selected_item)
                
    def edit_selected_client_simple():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Atención", "Seleccioná un cliente para editar.")
            return

        item_id = selected_item[0] # este es el ID interno del Treeview para la fila
        values = tree.item(item_id)["values"] # valores de cada columna
        client_id = values[0] # se selecciona la primera columna, que es el ID del cliente en la DB

        # Pedir datos uno por uno, precargados con el valor actual
        nombre = simpledialog.askstring("Editar Nombre", "Nombre:", initialvalue=values[1])
        if nombre is None: return
        apellido = simpledialog.askstring("Editar Apellido", "Apellido:", initialvalue=values[2])
        if apellido is None: return
        telefono = simpledialog.askstring("Editar Teléfono", "Teléfono:", initialvalue=values[3])
        if telefono is None: return
        dia = simpledialog.askstring("Editar Día", "Día:", initialvalue=values[4])
        if dia is None: return
        hora = simpledialog.askstring("Editar Hora", "Hora:", initialvalue=values[5])
        if hora is None: return

        cliente = Client(nombre, apellido, telefono, dia, hora)
        if cliente.update(client_id):
            tree.item(item_id, values=(client_id, nombre, apellido, telefono, dia, hora))
    

    btnToAddClient = tk.Label(window, text="Agregar nuevo cliente", fg="blue", cursor="hand2", font=("Helvetica", 10, "underline"))
    btnToAddClient.pack(pady=10)
    btnToAddClient.bind("<Button-1>", toAddClient)
    
    btnDelete = tk.Button(window, text="Eliminar cliente seleccionado", bg="red", fg="white", command=lambda: delete_selected_client())
    btnDelete.pack(pady=5)
    
    btnEdit = tk.Button(window, text="Editar cliente seleccionado", bg="orange", fg="white", command=edit_selected_client_simple)
    btnEdit.pack(pady=5)
    
    btnLogout = tk.Label(window, text="Cerrar sesión", fg="red", cursor="hand2", font=("Helvetica", 10, "underline"))
    btnLogout.pack(anchor="ne", padx=10, pady=10)
    btnLogout.bind("<Button-1>", logout)
    
    
    
    window.mainloop()