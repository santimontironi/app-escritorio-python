# 💇‍♀️ Turnero de Clientes para Peluquería

Este proyecto es un **trabajo integrador final del tercer año de la Tecnicatura en Desarrollo de Software**. Se trata de una aplicación de escritorio que permite gestionar turnos de clientes para una peluquería, desarrollada en **Python** utilizando la biblioteca estándar **Tkinter** para la interfaz gráfica (GUI), y **SQL Server** como sistema de gestión de base de datos.

La app permite realizar operaciones **CRUD**: crear, consultar, actualizar y eliminar turnos.

---

## 🧠 Tecnologías y Conceptos Utilizados

- **Lenguaje:** Python 3
- **Interfaz Gráfica:** Tkinter
- **Base de Datos:** SQL Server
- **Conector:** pyodbc
- **Programación Orientada a Objetos (POO)**
- Estructuras de control (condicionales, bucles)
- Modularización con funciones

---

## 🗂️ Funcionalidades del Sistema

La aplicación permite:

- Registrar nuevos turnos
- Consultar turnos existentes
- Modificar turnos (cambiar fecha, hora, cliente o servicio)
- Eliminar turnos registrados

### Campos manejados por cada turno:

- 🧑 Nombre del cliente  
- ✂️ Servicio solicitado  
- 📅 Fecha del turno  
- 🕒 Hora del turno  

---

## 🛠️ Instalación y Ejecución

### 1. Requisitos previos

- Tener instalado Python 3.x
- Tener instalado SQL Server (cualquier edición)
- Crear la base de datos `turnero` en SQL Server
- Instalar el conector `pyodbc`:

```bash
pip install pyodbc
🧾 Clonar el proyecto
git clone https://github.com/tu_usuario/turnero-peluqueria.git
cd turnero-peluqueria
