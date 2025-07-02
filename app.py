from bd import consulta

def registrarEmpleado(nombre,apellido,correo,clave):
    
    empleadoRepetido = "SELECT * FROM empleados WHERE correo = ?"
    resultadoEmpleadoRepetido = consulta(empleadoRepetido, (correo,), fetch=True)
    
    if resultadoEmpleadoRepetido:
        print("Usuario repetido")
        return
        
    query = "INSERT INTO empleados(nombre,apellido,correo,clave) VALUES (?,?,?,?)"
    resultados = consulta(query,(nombre,apellido,correo,clave),fetch=False)
    
    if resultados:
        print("Empleado registrado:")
            
registrarEmpleado("nachito","rosales","nachitos@gmail.com","123")


