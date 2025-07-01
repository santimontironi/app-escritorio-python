from bd import consulta

def ver_empleados():
    query = "SELECT * FROM empleados"
    resultados = consulta(query)
    
    if resultados:
        for fila in resultados:
            print(fila)
    else:
        print("No se encontraron resultados.")
            
ver_empleados()

