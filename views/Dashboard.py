import tkinter as tk

def dashboard_window():

    window = tk.Tk()

    window.title("Panel")
    window.configure(bg="lightgreen")
    window.geometry("700x400")
    
    title = tk.Label(window, text="Panel", font=("Times New Roman", 35, "bold", "underline"), bg="lightblue")
    title.pack(pady=(15))
    
    container = tk.Frame(window,relief="raised",bd=4)
    container.pack(expand=True)
    
    
    
    window.mainloop()