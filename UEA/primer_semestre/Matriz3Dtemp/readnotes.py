# Escritura en el archivo de texto
# Abrimos el archivo llamado "my_notes.txt" en modo de escritura ('w').
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales.
    file.write("Primera nota: Aprendiendo manejo de archivos en Python.\n")
    file.write("Segunda nota: Es importante cerrar los archivos después de usarlos.\n")
    file.write("Tercera nota: El método 'with' se encarga de esto automáticamente.\n")

# Lectura del archivo de texto
# Abrimos el archivo "my_notes.txt" en modo de lectura ('r').
with open('my_notes.txt', 'r') as file:
    # Leemos y mostramos cada línea del archivo en la consola.
    line = file.readline()  # Lee la primera línea
    while line:
        print(line.strip())  # Mostramos la línea eliminando saltos de línea innecesarios
        line = file.readline()  # Lee la siguiente línea

# Nota: No necesitamos cerrar manualmente el archivo al usar 'with',
# ya que Python se encarga de ello automáticamente.
