import threading
import time

def tarea_numeros():
    for i in range(1, 6):
        print(f"Número: {i}")
        time.sleep(1)

def tarea_letras():
    for letra in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letra: {letra}")
        time.sleep(1)

# Creación de hilos
hilo1 = threading.Thread(target=tarea_numeros)
hilo2 = threading.Thread(target=tarea_letras)
# Inicio de los hilos
hilo1.start()
hilo2.start()
# Esperar a que ambos hilos terminen
hilo1.join()
hilo2.join()

print("Ambos hilos han terminado su ejecución.")
