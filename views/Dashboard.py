import tkinter as tk
from views.AddClient import addClient_window

def dashboard_window():

    window = tk.Tk()

    window.title("Panel")
    window.configure(bg="lightgreen")
    window.geometry("700x400")
    
    title = tk.Label(window, text="Panel", font=("Times New Roman", 35, "bold", "underline"), bg="lightblue")
    title.pack(pady=(15))
    
    container = tk.Frame(window,relief="raised",bd=4)
    container.pack(expand=True)
    
    def toAddClient(event=None):
        window.destroy()
        addClient_window()
    
    btnToAddClient = tk.Label(window, text="Agregar nuevo cliente", fg="blue", cursor="hand2", font=("Helvetica", 10, "underline"))
    btnToAddClient.pack()

    btnToAddClient.bind("<Button-1>", toAddClient)
    
    window.mainloop()