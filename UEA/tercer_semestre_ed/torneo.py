# archivo: torneo.py
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional, Dict, Set, List, Tuple
from time import perf_counter
import timeit
import json
import csv
import os

# -----------------------------
# MODELO DE DATOS
# -----------------------------

@dataclass(frozen=True)
class Jugador:
    id: str
    nombre: str
    edad: int
    posicion: str
    equipo: Optional[str] = None  # nombre del equipo o None

class Torneo:
    def __init__(self) -> None:
        # Mapa equipo -> conjunto de IDs de jugadores
        self.equipos: Dict[str, Set[str]] = {}
        # Mapa jugador_id -> Jugador
        self.jugadores: Dict[str, Jugador] = {}
        # Conjunto de nombres de equipos (para unicidad, consultas rápidas)
        self.nombres_equipos: Set[str] = set()
        # Índice opcional: posicion -> set de jugador_id (para consultas por posición)
        self.posiciones_idx: Dict[str, Set[str]] = {}

    # -------------------------
    # Operaciones sobre Equipos
    # -------------------------
    def crear_equipo(self, nombre: str) -> bool:
        nombre = nombre.strip()
        if not nombre or nombre in self.nombres_equipos:
            return False
        self.nombres_equipos.add(nombre)
        self.equipos[nombre] = set()
        return True

    def eliminar_equipo(self, nombre: str, reasignar_a: Optional[str] = None) -> bool:
        if nombre not in self.nombres_equipos:
            return False
        jugadores_equipo = self.equipos.get(nombre, set())
        if reasignar_a is not None:
            if reasignar_a not in self.nombres_equipos:
                return False
            for jid in list(jugadores_equipo):
                self.transferir_jugador(jid, reasignar_a)
        else:
            # Quitar equipo de cada jugador
            for jid in list(jugadores_equipo):
                j = self.jugadores[jid]
                self.jugadores[jid] = Jugador(**{**asdict(j), 'equipo': None})
            self.equipos[nombre].clear()
        # Remover equipo
        del self.equipos[nombre]
        self.nombres_equipos.remove(nombre)
        return True

    # -------------------------
    # Operaciones sobre Jugadores
    # -------------------------
    def registrar_jugador(self, id: str, nombre: str, edad: int, posicion: str, equipo: Optional[str] = None) -> bool:
        id = id.strip()
        posicion = posicion.strip().upper()
        if not id or id in self.jugadores:
            return False
        if equipo is not None and equipo not in self.nombres_equipos:
            return False
        jugador = Jugador(id=id, nombre=nombre.strip(), edad=int(edad), posicion=posicion, equipo=equipo)
        self.jugadores[id] = jugador
        # Índices
        self.posiciones_idx.setdefault(posicion, set()).add(id)
        if equipo is not None:
            self.equipos[equipo].add(id)
        return True

    def eliminar_jugador(self, id: str) -> bool:
        if id not in self.jugadores:
            return False
        j = self.jugadores.pop(id)
        # Remover de índice por posición
        pos_set = self.posiciones_idx.get(j.posicion)
        if pos_set:
            pos_set.discard(id)
            if not pos_set:
                del self.posiciones_idx[j.posicion]
        # Remover de equipo
        if j.equipo:
            self.equipos[j.equipo].discard(id)
        return True

    def transferir_jugador(self, id: str, nuevo_equipo: str) -> bool:
        if id not in self.jugadores or nuevo_equipo not in self.nombres_equipos:
            return False
        j = self.jugadores[id]
        if j.equipo == nuevo_equipo:
            return True
        # Quitar del equipo anterior
        if j.equipo:
            self.equipos[j.equipo].discard(id)
        # Agregar al nuevo equipo
        self.equipos[nuevo_equipo].add(id)
        # Actualizar jugador (dataclass inmutable -> recrear)
        self.jugadores[id] = Jugador(**{**asdict(j), 'equipo': nuevo_equipo})
        return True

    def actualizar_jugador(self, id: str, **kwargs) -> bool:
        if id not in self.jugadores:
            return False
        j = self.jugadores[id]
        data = {**asdict(j)}
        for k, v in kwargs.items():
            if k == 'posicion' and isinstance(v, str):
                v = v.strip().upper()
                # actualizar índice por posición
                old = data['posicion']
                if old != v:
                    s = self.posiciones_idx.get(old, set())
                    s.discard(id)
                    if not s:
                        self.posiciones_idx.pop(old, None)
                    self.posiciones_idx.setdefault(v, set()).add(id)
            data[k] = v
        # si cambia equipo, mantener consistencia
        if 'equipo' in kwargs:
            nuevo_eq = kwargs['equipo']
            if nuevo_eq is not None and nuevo_eq not in self.nombres_equipos:
                return False
            # mover entre equipos
            old_eq = j.equipo
            if old_eq != nuevo_eq:
                if old_eq:
                    self.equipos[old_eq].discard(id)
                if nuevo_eq:
                    self.equipos[nuevo_eq].add(id)
        self.jugadores[id] = Jugador(**data)
        return True

    # -------------------------
    # Consultas / Reportería
    # -------------------------
    def listar_equipos(self) -> List[str]:
        return sorted(self.nombres_equipos)

    def listar_jugadores(self, equipo: Optional[str] = None) -> List[Jugador]:
        if equipo is None:
            return sorted(self.jugadores.values(), key=lambda j: (j.equipo or '', j.nombre))
        if equipo not in self.nombres_equipos:
            return []
        return sorted((self.jugadores[jid] for jid in self.equipos[equipo]), key=lambda j: j.nombre)

    def buscar_por_nombre(self, patron: str) -> List[Jugador]:
        p = patron.strip().lower()
        return sorted((j for j in self.jugadores.values() if p in j.nombre.lower()), key=lambda j: j.nombre)

    def jugadores_por_posicion(self, posicion: str) -> List[Jugador]:
        pos = posicion.strip().upper()
        ids = self.posiciones_idx.get(pos, set())
        return sorted((self.jugadores[jid] for jid in ids), key=lambda j: j.nombre)

    def top_equipos_por_tamano(self, k: int = 5) -> List[Tuple[str, int]]:
        pares = [(eq, len(ids)) for eq, ids in self.equipos.items()]
        pares.sort(key=lambda t: (-t[1], t[0]))
        return pares[:k]

    def resumen(self) -> Dict[str, int]:
        return {
            'num_equipos': len(self.nombres_equipos),
            'num_jugadores': len(self.jugadores),
            'promedio_jugadores_por_equipo': int(round(sum(len(v) for v in self.equipos.values()) / max(1, len(self.equipos))))
        }

    # -------------------------
    # Persistencia ligera
    # -------------------------
    def exportar_json(self, ruta: str) -> None:
        data = {
            'equipos': {k: sorted(list(v)) for k, v in self.equipos.items()},
            'jugadores': {k: asdict(v) for k, v in self.jugadores.items()}
        }
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def importar_json(self, ruta: str) -> None:
        with open(ruta, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.__init__()
        # reconstruir
        for eq in data['equipos'].keys():
            self.crear_equipo(eq)
        for jid, jd in data['jugadores'].items():
            self.registrar_jugador(
                id=jd['id'], nombre=jd['nombre'], edad=jd['edad'],
                posicion=jd['posicion'], equipo=jd.get('equipo')
            )

    def exportar_jugadores_csv(self, ruta: str) -> None:
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, 'w', encoding='utf-8', newline='') as f:
            w = csv.writer(f)
            w.writerow(['id', 'nombre', 'edad', 'posicion', 'equipo'])
            for j in self.listar_jugadores():
                w.writerow([j.id, j.nombre, j.edad, j.posicion, j.equipo or ''])

# -----------------------------
# CLI SENCILLA
# -----------------------------

def menu():
    print("\n=== Torneo de Fútbol – Gestión (sets & dicts) ===")
    print("1) Crear equipo")
    print("2) Registrar jugador")
    print("3) Transferir jugador")
    print("4) Listar equipos")
    print("5) Listar jugadores (por equipo/opcional)")
    print("6) Buscar jugador por nombre")
    print("7) Reporte: top equipos por tamaño")
    print("8) Resumen general")
    print("9) Exportar JSON / CSV")
    print("10) Importar desde JSON")
    print("0) Salir")


def ejecutar_cli():
    t = Torneo()
    while True:
        menu()
        op = input("Opción: ").strip()
        if op == '1':
            nombre = input("Nombre del equipo: ")
            ok = t.crear_equipo(nombre)
            print("Equipo creado" if ok else "No se pudo crear (ya existe o nombre inválido)")
        elif op == '2':
            jid = input("ID jugador: ").strip()
            nombre = input("Nombre: ").strip()
            edad = int(input("Edad: ").strip())
            pos = input("Posición (GK/DF/MF/FW): ").strip()
            eq = input("Equipo (opcional): ").strip() or None
            ok = t.registrar_jugador(jid, nombre, edad, pos, eq)
            print("Jugador registrado" if ok else "No se pudo registrar (ID duplicado o equipo inexistente)")
        elif op == '3':
            jid = input("ID jugador: ").strip()
            dest = input("Nuevo equipo: ").strip()
            ok = t.transferir_jugador(jid, dest)
            print("Transferencia ok" if ok else "No se pudo transferir")
        elif op == '4':
            print("Equipos:")
            for e in t.listar_equipos():
                print(f"- {e} ({len(t.equipos[e])} jugadores)")
        elif op == '5':
            eq = input("Equipo (vacío= todos): ").strip() or None
            js = t.listar_jugadores(eq)
            if not js:
                print("Sin jugadores")
            for j in js:
                print(f"{j.id} – {j.nombre} ({j.posicion}) – Equipo: {j.equipo}")
        elif op == '6':
            patron = input("Buscar nombre contiene: ").strip()
            for j in t.buscar_por_nombre(patron):
                print(f"{j.id} – {j.nombre} ({j.posicion}) – Equipo: {j.equipo}")
        elif op == '7':
            k = int(input("Top k = ").strip() or 5)
            for eq, n in t.top_equipos_por_tamano(k):
                print(f"{eq}: {n} jugadores")
        elif op == '8':
            print(t.resumen())
        elif op == '9':
            ruta_json = input("Ruta JSON (./salida/torneo.json): ").strip() or "./salida/torneo.json"
            ruta_csv = input("Ruta CSV (./salida/jugadores.csv): ").strip() or "./salida/jugadores.csv"
            t.exportar_json(ruta_json)
            t.exportar_jugadores_csv(ruta_csv)
            print("Exportado.")
        elif op == '10':
            ruta = input("Ruta JSON: ").strip()
            t.importar_json(ruta)
            print("Importado.")
        elif op == '0':
            break
        else:
            print("Opción inválida")

# -----------------------------
# BENCHMARK SINTÉTICO
# -----------------------------

def _poblar(t: Torneo, n_equipos: int, n_jugadores: int):
    for i in range(n_equipos):
        t.crear_equipo(f"Equipo_{i}")
    posiciones = ["GK", "DF", "MF", "FW"]
    for j in range(n_jugadores):
        eq = f"Equipo_{j % max(1, n_equipos)}"
        t.registrar_jugador(
            id=f"J{j}", nombre=f"Jugador {j}", edad=18 + (j % 20),
            posicion=posiciones[j % 4], equipo=eq
        )

def benchmark(n_equipos: int = 100, n_jugadores: int = 10_000) -> dict:
    t = Torneo()
    _poblar(t, n_equipos, n_jugadores)

    # Medir operaciones críticas
    start = perf_counter(); _ = "J0" in t.jugadores; t1 = perf_counter() - start
    start = perf_counter(); t.crear_equipo("Equipo_X"); t2 = perf_counter() - start
    start = perf_counter(); t.registrar_jugador("JX", "Demo X", 25, "MF", "Equipo_0"); t3 = perf_counter() - start
    start = perf_counter(); t.transferir_jugador("J1", "Equipo_1"); t4 = perf_counter() - start

    # Uso de timeit para medias
    stmt = "'J500' in t.jugadores"
    tries = 10000
    avg_lookup = timeit.timeit(stmt=stmt, number=tries, globals={'t': t}) / tries

    return {
        'lookup_una_vez': t1,
        'crear_equipo': t2,
        'registrar_jugador': t3,
        'transferir_jugador': t4,
        'avg_lookup_timeit': avg_lookup,
        'n_equipos': n_equipos, 'n_jugadores': n_jugadores
    }


if __name__ == '__main__':
    # Descomenta una de las dos líneas según lo que quieras probar
    # ejecutar_cli()

    # Benchmark rápido
    res = benchmark(50, 5000)
    print("Resultado benchmark:", json.dumps(res, indent=2))
