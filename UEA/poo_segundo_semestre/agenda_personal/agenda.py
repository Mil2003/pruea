import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

# Función para agregar un evento a la lista
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_desc.get()

    if fecha and hora and descripcion:
        tree.insert("", "end", values=(fecha, hora, descripcion))
        entry_fecha.set_date("")  # Reiniciar DateEntry
        entry_hora.delete(0, tk.END)
        entry_desc.delete(0, tk.END)
    else:
        messagebox.showwarning("Campos Vacíos", "Por favor, llena todos los campos.")

# Función para eliminar el evento seleccionado
def eliminar_evento():
    seleccionado = tree.selection()
    if seleccionado:
        confirmacion = messagebox.askyesno("Confirmar", "¿Deseas eliminar el evento seleccionado?")
        if confirmacion:
            tree.delete(seleccionado)
    else:
        messagebox.showwarning("Selecciona un Evento", "Por favor, selecciona un evento para eliminar.")

# Crear la ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("500x400")

# Crear un frame para los campos de entrada
frame_inputs = tk.Frame(root, padx=10, pady=10)
frame_inputs.pack(fill="x")

# Campos de entrada
tk.Label(frame_inputs, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
entry_fecha = DateEntry(frame_inputs, width=12, background='darkblue', foreground='white', borderwidth=2)
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
entry_hora = tk.Entry(frame_inputs)
entry_hora.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
entry_desc = tk.Entry(frame_inputs)
entry_desc.grid(row=2, column=1, padx=5, pady=5)

# Botón para agregar evento
btn_agregar = tk.Button(frame_inputs, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=3, column=0, columnspan=2, pady=10)

# Crear el TreeView para mostrar eventos
frame_lista = tk.Frame(root, padx=10, pady=10)
frame_lista.pack(fill="both", expand=True)

tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack(fill="both", expand=True)

# Botón para eliminar evento
btn_eliminar = tk.Button(root, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.pack(pady=5)

# Botón para salir
btn_salir = tk.Button(root, text="Salir", command=root.quit)
btn_salir.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()
