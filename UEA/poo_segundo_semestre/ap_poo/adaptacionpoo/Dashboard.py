import os
import subprocess
import time
from colorama import Fore, Style, init

# Inicializar colorama para Windows
init(autoreset=True)

def mostrar_codigo(ruta_script):
    """Muestra el contenido del código del script seleccionado."""
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n{Fore.CYAN}--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print(Fore.RED + "El archivo no se encontró.")
    except Exception as e:
        print(Fore.RED + f"Ocurrió un error al leer el archivo: {e}")

def ejecutar_codigo(ruta_script):
    """Ejecuta el script seleccionado y lo registra en el historial."""
    try:
        with open("historial.txt", "a") as log:
            log.write(f"Ejecutado: {ruta_script} - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])

    except Exception as e:
        print(Fore.RED + f"Ocurrió un error al ejecutar el código: {e}")

def mostrar_menu():
    """Muestra el menú principal con las unidades disponibles."""
    ruta_base = os.path.dirname(__file__)
    unidades = {str(i + 1): carpeta for i, carpeta in enumerate(
        [f.name for f in os.scandir(ruta_base) if f.is_dir()])}

    while True:
        print(Fore.CYAN + "\n📌 Menu Principal - Dashboard")
        for key in unidades:
            print(Fore.YELLOW + f"{key} - {unidades[key]}")
        print(Fore.RED + "0 - Salir")

        eleccion_unidad = input(Fore.GREEN + "Elige una unidad o '0' para salir: ")
        if eleccion_unidad == '0':
            print(Fore.RED + "Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
        else:
            print(Fore.RED + "Opción no válida. Intenta de nuevo.")

def mostrar_sub_menu(ruta_unidad):
    """Muestra las subcarpetas dentro de una unidad."""
    if not os.path.exists(ruta_unidad):
        print(Fore.RED + "No existen subcarpetas en esta unidad.")
        return

    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]
    
    while True:
        print(Fore.CYAN + "\n📂 Submenú - Selecciona una subcarpeta")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(Fore.YELLOW + f"{i} - {carpeta}")
        print(Fore.RED + "0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una opción: ")
        if eleccion_carpeta == '0':
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
                else:
                    print(Fore.RED + "Opción no válida.")
            except ValueError:
                print(Fore.RED + "Opción no válida.")

def mostrar_scripts(ruta_sub_carpeta):
    """Muestra los scripts disponibles en la subcarpeta y permite ejecutarlos o crear nuevos."""
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print(Fore.CYAN + "\n📜 Scripts disponibles:")
        for i, script in enumerate(scripts, start=1):
            print(Fore.YELLOW + f"{i} - {script}")
        print(Fore.RED + "0 - Regresar al submenú")
        print(Fore.GREEN + "N - Crear un nuevo script")

        eleccion_script = input("Elige una opción: ")
        if eleccion_script == '0':
            break
        elif eleccion_script.lower() == 'n':
            crear_nuevo_script(ruta_sub_carpeta)
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input(Fore.GREEN + "¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                else:
                    print(Fore.RED + "Opción no válida.")
            except ValueError:
                print(Fore.RED + "Opción no válida.")

def crear_nuevo_script(ruta_sub_carpeta):
    """Crea un nuevo script vacío en la subcarpeta seleccionada."""
    nombre_script = input(Fore.GREEN + "Nombre del nuevo script (sin .py): ") + ".py"
    ruta_nuevo_script = os.path.join(ruta_sub_carpeta, nombre_script)

    if os.path.exists(ruta_nuevo_script):
        print(Fore.RED + "El script ya existe.")
    else:
        with open(ruta_nuevo_script, 'w') as f:
            f.write("# Nuevo script creado desde el Dashboard\n\n")
        print(Fore.GREEN + f"Script {nombre_script} creado con éxito.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
