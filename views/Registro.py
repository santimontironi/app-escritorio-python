import tkinter as tk

window = tk.Tk()

window.title("Registrarse")
window.configure(bg="lightblue")
window.geometry("650x400")

contenedor = tk.Frame(window,relief="raised",bd=4)
contenedor.pack(expand=True)  # se centra vertical y horizontalmente

titulo = tk.Label(window, text="Registrarse", font=("Times New Roman", 18, "bold"), bg="lightblue")
titulo.pack(pady=(20,10),anchor="n")

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


button = tk.Button(contenedor, text="Registrar").grid(row=4, column=0, columnspan=2, pady=30)


window.mainloop()