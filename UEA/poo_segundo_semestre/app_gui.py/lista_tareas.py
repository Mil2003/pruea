import tkinter as tk
from tkinter import messagebox

# Funciones de la aplicación
def agregar_tarea(event=None):
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)  # Agrega la tarea a la lista
        entrada_tarea.delete(0, tk.END)  # Limpia el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía")

def marcar_completada():
    try:
        index = lista_tareas.curselection()[0]  # Obtener índice de la tarea seleccionada
        tarea = lista_tareas.get(index)

        # Si la tarea ya está marcada, la restauramos
        if tarea.startswith("✔ "):
            nueva_tarea = tarea[2:]  
        else:
            nueva_tarea = "✔ " + tarea  # Añadir un check (✔) al inicio

        lista_tareas.delete(index)
        lista_tareas.insert(index, nueva_tarea)  # Reinsertar con el cambio

    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada")

def eliminar_tarea():
    try:
        index = lista_tareas.curselection()[0]
        lista_tareas.delete(index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x400")

# Crear widgets
entrada_tarea = tk.Entry(ventana, width=40)
boton_agregar = tk.Button(ventana, text="Añadir Tarea", command=agregar_tarea)
boton_completar = tk.Button(ventana, text="Marcar como Completada", command=marcar_completada)
boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
lista_tareas = tk.Listbox(ventana, width=50, height=15)

# Organizar widgets en la ventana
entrada_tarea.pack(pady=10)
boton_agregar.pack(pady=5)
lista_tareas.pack(pady=10)
boton_completar.pack(pady=5)
boton_eliminar.pack(pady=5)

# Vincular tecla "Enter" para agregar tarea
ventana.bind("<Return>", agregar_tarea)

# Ejecutar la aplicación
ventana.mainloop()
