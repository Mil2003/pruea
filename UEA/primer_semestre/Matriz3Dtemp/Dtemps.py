# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades
# Segunda dimensión: Semanas
# Tercera dimensión: Días de la semana
temperaturas = [
    [   # Ciudad A
        [   # Semana 1
            {"dia": "Lunes", "temperatura": 22},
            {"dia": "Martes", "temperatura": 24},
            {"dia": "Miércoles", "temperatura": 26},
            {"dia": "Jueves", "temperatura": 23},
            {"dia": "Viernes", "temperatura": 27},
            {"dia": "Sábado", "temperatura": 25}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temperatura": 21},
            {"dia": "Martes", "temperatura": 23},
            {"dia": "Miércoles", "temperatura": 25},
            {"dia": "Jueves", "temperatura": 22},
            {"dia": "Viernes", "temperatura": 26},
            {"dia": "Sábado", "temperatura": 24}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temperatura": 20},
            {"dia": "Martes", "temperatura": 22},
            {"dia": "Miércoles", "temperatura": 24},
            {"dia": "Jueves", "temperatura": 21},
            {"dia": "Viernes", "temperatura": 25},
            {"dia": "Sábado", "temperatura": 23}
        ]
    ],
    [   # Ciudad B
        [   # Semana 1
            {"dia": "Lunes", "temperatura": 15},
            {"dia": "Martes", "temperatura": 17},
            {"dia": "Miércoles", "temperatura": 19},
            {"dia": "Jueves", "temperatura": 16},
            {"dia": "Viernes", "temperatura": 18},
            {"dia": "Sábado", "temperatura": 20}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temperatura": 14},
            {"dia": "Martes", "temperatura": 16},
            {"dia": "Miércoles", "temperatura": 18},
            {"dia": "Jueves", "temperatura": 15},
            {"dia": "Viernes", "temperatura": 17},
            {"dia": "Sábado", "temperatura": 19}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temperatura": 13},
            {"dia": "Martes", "temperatura": 15},
            {"dia": "Miércoles", "temperatura": 17},
            {"dia": "Jueves", "temperatura": 14},
            {"dia": "Viernes", "temperatura": 16},
            {"dia": "Sábado", "temperatura": 18}
        ]
    ],
    [   # Ciudad C
        [   # Semana 1
            {"dia": "Lunes", "temperatura": 28},
            {"dia": "Martes", "temperatura": 30},
            {"dia": "Miércoles", "temperatura": 32},
            {"dia": "Jueves", "temperatura": 29},
            {"dia": "Viernes", "temperatura": 33},
            {"dia": "Sábado", "temperatura": 31}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temperatura": 27},
            {"dia": "Martes", "temperatura": 29},
            {"dia": "Miércoles", "temperatura": 31},
            {"dia": "Jueves", "temperatura": 28},
            {"dia": "Viernes", "temperatura": 32},
            {"dia": "Sábado", "temperatura": 30}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temperatura": 26},
            {"dia": "Martes", "temperatura": 28},
            {"dia": "Miércoles", "temperatura": 30},
            {"dia": "Jueves", "temperatura": 27},
            {"dia": "Viernes", "temperatura": 31},
            {"dia": "Sábado", "temperatura": 29}
        ]
    ],
    [   # Ciudad D
        [   # Semana 1
            {"dia": "Lunes", "temperatura": 10},
            {"dia": "Martes", "temperatura": 12},
            {"dia": "Miércoles", "temperatura": 14},
            {"dia": "Jueves", "temperatura": 11},
            {"dia": "Viernes", "temperatura": 13},
            {"dia": "Sábado", "temperatura": 15}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temperatura": 9},
            {"dia": "Martes", "temperatura": 11},
            {"dia": "Miércoles", "temperatura": 13},
            {"dia": "Jueves", "temperatura": 10},
            {"dia": "Viernes", "temperatura": 12},
            {"dia": "Sábado", "temperatura": 14}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temperatura": 8},
            {"dia": "Martes", "temperatura": 10},
            {"dia": "Miércoles", "temperatura": 12},
            {"dia": "Jueves", "temperatura": 9},
            {"dia": "Viernes", "temperatura": 11},
            {"dia": "Sábado", "temperatura": 13}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for i, ciudad in enumerate(temperaturas):
    print(f"Ciudad {chr(65 + i)}:")
    for j, semana in enumerate(ciudad):
        total_temp = 0
        for dia in semana:
            total_temp += dia['temperatura']
        promedio_temp = total_temp / len(semana)
        print(f"  Promedio de temperatura en la Semana {j + 1}: {promedio_temp:.1f}°C")
    print()
