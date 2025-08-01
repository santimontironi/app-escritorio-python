import tkinter as tk
from controllers.client import Client
from tkcalendar import DateEntry

def addClient_window():

    from views.Dashboard import dashboard_window

    window = tk.Tk()

    window.title("Agregar cliente")
    window.configure(bg="brown")
    window.geometry("700x450")

    title = tk.Label(window, text="Agregar cliente", font=("Times New Roman", 35, "bold", "underline"), bg="lightblue")
    title.pack(pady=10)

    container = tk.Frame(window,relief="raised",bd=4)
    container.pack(expand=True) 
        
    tk.Label(container, text="Nombre:", font=("Helvetica", 10)).grid(row=0, column=0, padx=10, pady=10)
    entry_name = tk.Entry(container)
    entry_name.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(container, text="Apellido:", font=("Helvetica", 10)).grid(row=1, column=0, padx=10, pady=10)
    entry_surname = tk.Entry(container)
    entry_surname.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(container, text="Telefono", font=("Helvetica", 10)).grid(row=2, column=0, padx=10, pady=10)
    entry_telefono = tk.Entry(container)
    entry_telefono.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(container, text="Dia", font=("Helvetica", 10)).grid(row=3, column=0, padx=10, pady=10)
    entry_dia = DateEntry(container, date_pattern="yyyy-mm-dd")
    entry_dia.grid(row=3, column=1, padx=10, pady=10)
    
    tk.Label(container, text="Hora", font=("Helvetica", 10)).grid(row=4, column=0, padx=10, pady=10)
    entry_hora = tk.Entry(container)
    entry_hora.grid(row=4, column=1, padx=10, pady=10)
    
    def sendData():
        name = entry_name.get()
        surname = entry_surname.get()
        telefono = entry_telefono.get()
        dia = entry_dia.get()
        hora = entry_hora.get()
        
        newClient = Client(name,surname,telefono,dia,hora)
        
        if newClient.register():
            window.destroy()
            dashboard_window()


    tk.Button(container, text="Agregar cliente", bg="lightgreen", command=sendData, font=("Helvetica",10)).grid(row=5, column=0, columnspan=2, padx=20, pady=20)
    
    def clickBack(event=None):
        window.destroy()
        dashboard_window()
    
    goBack = tk.Label(window, text="Volver", fg="white", cursor="hand2", font=("Helvetica", 12, "underline"))
    goBack.configure(bg=window["bg"])
    goBack.pack(pady=12)

    goBack.bind("<Button-1>", clickBack)

    window.mainloop()