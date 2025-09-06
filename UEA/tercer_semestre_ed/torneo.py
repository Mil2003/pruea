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
            return 
