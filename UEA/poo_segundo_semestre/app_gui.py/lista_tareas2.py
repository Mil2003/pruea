import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("400x400")

        # Entrada de nueva tarea
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)
        self.task_entry.bind("<Return>", lambda event: self.add_task())  # Atajo: Enter

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        # Botones
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack()

        self.complete_button = tk.Button(root, text="Completar Tarea", command=self.complete_task)
        self.complete_button.pack()

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack()

        # Atajos de teclado
        root.bind("<c>", lambda event: self.complete_task())  # Atajo: C
        root.bind("<d>", lambda event: self.delete_task())  # Atajo: D
        root.bind("<Delete>", lambda event: self.delete_task())  # Atajo: Supr
        root.bind("<Escape>", lambda event: root.quit())  # Atajo: Escape

    def add_task(self):
        """Añadir nueva tarea a la lista"""
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def complete_task(self):
        """Marcar tarea como completada"""
        try:
            selected_index = self.task_listbox.curselection()[0]
            task_text = self.task_listbox.get(selected_index)

            if not task_text.startswith("[✔] "):  # Evita marcar dos veces
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, f"[✔] {task_text}")
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para completar.")

    def delete_task(self):
        """Eliminar tarea seleccionada"""
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
