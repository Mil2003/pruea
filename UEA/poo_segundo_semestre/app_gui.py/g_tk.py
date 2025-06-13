import tkinter as tk
from tkinter import ttk, messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Datos con Tkinter")
        self.root.geometry("400x400")

        # Etiqueta y campo de entrada
        self.label = tk.Label(root, text="Ingrese un dato:")
        self.label.pack(pady=5)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        # Botón para agregar datos
        self.add_button = tk.Button(root, text="Agregar", command=self.add_data)
        self.add_button.pack(pady=5)

        # Tabla para mostrar los datos
        self.tree = ttk.Treeview(root, columns=("Datos"), show="headings")
        self.tree.heading("Datos", text="Datos ingresados")
        self.tree.pack(pady=5)

        # Botón para limpiar datos
        self.clear_button = tk.Button(root, text="Limpiar", command=self.clear_data)
        self.clear_button.pack(pady=5)

    def add_data(self):
        """Agrega el dato ingresado en la tabla."""
        data = self.entry.get().strip()
        if data:
            self.tree.insert("", "end", values=(data,))
            self.entry.delete(0, tk.END)  # Limpiar campo de texto
        else:
            messagebox.showwarning("Aviso", "El campo está vacío.")

    def clear_data(self):
        """Elimina todos los datos de la tabla."""
        for item in self.tree.get_children():
            self.tree.delete(item)

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
