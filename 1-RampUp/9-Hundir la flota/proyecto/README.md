# 🎮 Hundir la Flota

Un juego interactivo de **Hundir la Flota** (Battleship) implementado en Python, donde puedes jugar contra la máquina con opción de colocación manual o automática de barcos.

## 📋 Características

- ✅ Juego completo de Hundir la Flota
- ✅ Dos modos de colocación de barcos:
  - **Automático**: Los barcos se colocan de forma aleatoria
  - **Manual**: El jugador ingresa las coordenadas de cada barco
- ✅ Interfaz clara en consola con emojis
- ✅ Validación de coordenadas y movimientos
- ✅ Tableros ocultos del enemigo (solo se muestran impactos y agua)
- ✅ Turnos alternados entre jugador y máquina

## 🎯 Barcos del Juego

| Barco | Tamaño | Cantidad |
|-------|--------|----------|
| 🚤 Fragata | 1 casilla | 4 |
| 🛥️ Patrullera | 2 casillas | 3 |
| 🚢 Crucero | 3 casillas | 2 |
| ⛴️ Acorazado | 4 casillas | 1 |

## 🕹️ Símbolos del Juego

- 🟡 Agua sin disparar
- 🌊 Agua (disparo fallido)
- 💥 Impacto (barco tocado)

## 📦 Requisitos

- Python 3.7+
- NumPy
- Sistema operativo: Windows, macOS o Linux

## 🚀 Instalación

1. **Clonar el repositorio:**
```bash
git clone https://github.com/jlalonsoredon/hundir_la_flota.git
cd hundir_la_flota
```

2. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

O si prefieres instalar manualmente:
```bash
pip install numpy
```

## 🎮 Cómo Jugar

1. **Ejecutar el juego:**
```bash
python main.py
```

2. **Elegir modo de colocación:**
   - **Opción 1**: Colocación automática
   - **Opción 2**: Colocación manual (ingresarás las coordenadas)

3. **Durante el juego:**
   - El tablero izquierdo es **tu tablero** (tus barcos y defensa)
   - El tablero derecho es **tablero de disparos** (enemigo)
   - Ingresa coordenadas en formato: `A5`, `B10`, `J1`, etc.
   - Las letras (A-J) representan filas
   - Los números (1-10) representan columnas

4. **Objetivo:**
   - ¡Hundir todos los barcos del enemigo antes de que hundan los tuyos!

## 📂 Estructura del Proyecto

```
.
├── main.py                 # Punto de entrada del juego
├── README.md              # Este archivo
├── requirements.txt       # Dependencias del proyecto
├── src/
│   ├── __init__.py
│   ├── board/            # Módulo de tableros
│   │   ├── __init__.py
│   │   ├── board.py      # Clase Board (tablero)
│   ├── game/             # Módulo de lógica del juego
│   │   ├── __init__.py
│   │   ├── game.py       # Mecánica principal del juego
│   │   ├── ship.py       # Clase Ship (barco)
│   │   └── turn.py       # Funciones de turno y validación
│   ├── players/          # Módulo de jugadores
│   │   ├── __init__.py
│   │   ├── player.py     # Clase Player (jugador)
│   │   └── ai_player.py  # Clase AIPlayer (máquina)
│   ├── utils/            # Utilidades y constantes
│   │   ├── __init__.py
│   │   ├── constants.py  # Constantes (gráficos, barcos, etc.)
│   │   └── helpers.py    # Funciones auxiliares
│   └── __pycache__/      # Cache de Python (se genera automáticamente)
└── tests/                 # Pruebas unitarias
    ├── test_board.py
    ├── test_game.py
    └── test_ship.py
```

## 🔧 Clases Principales

### `Board`
Gestiona el tablero del juego. Métodos principales:
- `_crear_tablero()`: Crea una matriz 11x11 con encabezados
- `put_ships()`: Coloca barcos automáticamente
- `put_ships_manual()`: Coloca barcos manualmente
- `put_ships_pc()`: Coloca barcos de la máquina
- `mostrar_dos_tableros()`: Muestra ambos tableros en la consola
- `disparar()`: Realiza un disparo
- `have_ships()`: Verifica si quedan barcos
- `get_ship_count()`: Devuelve cantidad de barcos restantes

### `Ship`
Representa un barco. Métodos principales:
- `__init__(name, size, table)`: Inicializa el barco
- `place()`: Coloca manualmente el barco ingresando coordenadas
- `generate_random_position()`: Genera una posición aleatoria válida
- `ship_orientation()`: Pregunta la orientación (H/V)
- `validar_coordenadas()`: Valida el formato de coordenadas

### `Turn`
Funciones para gestionar los turnos:
- `obtener_coordenadas_usuario()`: Obtiene input del usuario
- `disparar_a_maquina()`: Genera disparo aleatorio de la máquina
- `validar_coordenadas()`: Valida coordenadas y rangos
- `comprobar_acierto()`: Verifica si fue acierto o fallo

## 🎮 Gameplay

### Pantalla Inicial
```
¿Cómo deseas colocar tus barcos?
1. Automáticamente (aleatorio)
2. Manualmente (ingresa las coordenadas)

Selecciona 1 o 2: 1
```

### Durante el Juego
```
   TU TABLERO                                TABLERO DISPAROS
   1   2   3   4   5   6   7   8   9  10     1   2   3   4   5   6   7   8   9  10
A 🟡  🟡 🚤 🚤  🟡  🟡  🟡  🟡  🟡  🟡     A 🟡  🟡  🟡  🟡  🟡  🟡  🟡  🟡  🟡  🟡
B 🟡  🚢 🚢  🚢  🟡  🟡  🟡  🟡  🟡  🟡     B 🟡  🟡  🟡  🟡  🟡  🟡  🟡  🟡  🟡  🟡
...

Turno del jugador: Dispara a coordenadas del enemigo
Introduce las coordenada (ej: A5): A1
```

## 💡 Características Técnicas

- **Orientación de barcos**: Horizontal (H) o Vertical (V)
- **Validación de coordenadas**: Formato A-J (letras) y 1-10 (números)
- **Prevención de sobreposición**: Los barcos no pueden superponerse
- **Límites del tablero**: Se validan los rangos válidos (1-10, A-J)
- **Historial de disparos**: Se evita disparar en la misma posición dos veces
- **Tableros ocultos**: Los barcos enemigos permanecen ocultos hasta que son tocados
- **Matriz NumPy**: Uso de arrays NumPy para eficiencia y facilidad de índices

## 🐛 Solución de Problemas

| Problema | Solución |
|----------|----------|
| `ModuleNotFoundError: No module named 'numpy'` | Ejecuta `pip install numpy` |
| Barcos saliendo del tablero (manual) | Verifica que las coordenadas + tamaño no excedan 10 |
| Entrada inválida rechazada | Usa formato correcto: `A5`, `J10`, etc. (mayúscula + número) |
| El juego no inicia | Asegúrate de estar en la carpeta raíz y Python 3.7+ |

## 📝 Notas de Desarrollo

- El proyecto usa **NumPy** para las matrices de tableros
- Los tableros son matrices 11x11:
  - Fila 0 y Columna 0 contienen encabezados (coordenadas)
  - Las filas 1-10 y columnas 1-10 contienen el juego
- **Valores de celda**:
  - `0`: Agua/Vacío
  - `1-4`: Barcos (según tamaño)
  - `5`: Agua disparada
  - `6`: Impacto
- Se emplean **emojis Unicode** 🟡🌊💥🚤🛥️🚢⛴️ para mejor visualización

## 🎯 Reglas del Juego

1. Ambos jugadores colocan sus barcos (manual o automático)
2. El jugador humano intenta hundir los barcos enemigos
3. Después de cada disparo del jugador, la máquina dispara
4. El juego continúa hasta que uno de los dos hunde todos los barcos del enemigo
5. Los barcos no pueden tocarse ni superponerse
6. No se puede disparar dos veces en la misma posición

## 👨‍💻 Autor

Creado como práctica de programación en Python por **Jose Luis Alonso** 
- Conceptos: POO, Estructuras de datos, Lógica de juegos, NumPy

## 📄 Licencia

Libre para uso educativo y personal.

---

¡Disfruta del juego! 🎮⚓

Para más información, bugs o sugerencias, crea un issue en el repositorio.
