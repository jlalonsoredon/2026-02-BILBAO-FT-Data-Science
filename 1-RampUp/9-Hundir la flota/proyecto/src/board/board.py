import numpy as np
import string
from ..utils.constants import GRAFICS
from ..utils.constants import NUM_SHIPS
from ..utils.constants import SIZE_SHIPS
from ..game.ship import Ship
import src.utils.helpers as helpers
from ..utils.constants import HEADER

class Board:

    def __init__(self, size=10):
        self.size = size
        self.grid = self._crear_tablero()

    def _crear_tablero(self):
        # Inicializar matriz de enteros
        tablero = np.zeros((self.size + 1, self.size + 1), dtype=object)

        # coordenadas horizontales (números como strings)
        tablero[0, 1:] = [f"{i:2}" for i in range(1, self.size + 1)]

        # coordenadas verticales (letras)
        tablero[1:, 0] = list(string.ascii_uppercase[:self.size])

        # casillas vacías (números enteros)
        tablero[1:, 1:] = 0
        
        return tablero
    
    def put_ships(self, tablero_user, tablero_pc):
        # Colocar barcos automáticamente para el usuario
        for ship in NUM_SHIPS:
            for _ in range(NUM_SHIPS[ship]):
                nuevo_barco = Ship(ship, SIZE_SHIPS[ship], tablero_user)
                print(f"Coloca tu {nuevo_barco}")
                nuevo_barco.generate_random_position(tablero_user)
                print(f"{nuevo_barco} colocado en {nuevo_barco.position}")
                for (fila, col) in nuevo_barco.position:
                    tablero_user[fila, col] = SIZE_SHIPS[ship]  # Marcar la posición del barco con su tamaño
                self.mostrar_dos_tableros(tablero_user, tablero_pc)  # Mostrar el tablero después de colocar cada barco
        return tablero_user
    
    def put_ships_manual(self, tablero_user, tablero_pc):
        # Colocar barcos manualmente para el usuario
        for ship in NUM_SHIPS:
            for _ in range(NUM_SHIPS[ship]):
                nuevo_barco = Ship(ship, SIZE_SHIPS[ship], tablero_user)
                print(f"\nColoca tu {nuevo_barco}")
                nuevo_barco.place(nuevo_barco.position, tablero_user)
                print(f"{nuevo_barco} colocado en {nuevo_barco.position}")
                for (fila, col) in nuevo_barco.position:
                    tablero_user[fila, col] = SIZE_SHIPS[ship]  # Marcar la posición del barco con su tamaño
                self.mostrar_dos_tableros(tablero_user, tablero_pc)  # Mostrar el tablero después de colocar cada barco
        return tablero_user
    
    def put_ships_pc(self, tablero_pc):
        # Colocar barcos automáticamente para la PC
        for ship in NUM_SHIPS:
            for _ in range(NUM_SHIPS[ship]):
                nuevo_barco = Ship(ship, SIZE_SHIPS[ship], tablero_pc)
                nuevo_barco.generate_random_position(tablero_pc)
                for (fila, col) in nuevo_barco.position:
                    tablero_pc[fila, col] = SIZE_SHIPS[ship]  # Marcar la posición del barco con su tamaño
        return tablero_pc
    
    @staticmethod
    def mostrar_dos_tableros(tablero1, tablero2, size=10):
        helpers.limpiar_consola()
        print(HEADER)
        # cabecera
        print("   TU TABLERO".ljust(60) + "TABLERO DISPAROS")

        # números
        header_numbers = " ".join(f"{i:>3}" for i in range(1, size+1))
        header_row = "   " + header_numbers
        print(header_row + "     " + header_row)

        # Crear una copia de tablero2 con barcos ocultos
        import numpy as np
        tablero2_oculto = tablero2.copy()
        # Reemplazar barcos (1-4) con 0 (vacío)
        for i in range(tablero2_oculto.shape[0]):
            for j in range(tablero2_oculto.shape[1]):
                # Solo reemplazar si es un número entero entre 1 y 4
                if isinstance(tablero2_oculto[i, j], (int, np.integer)) and 1 <= tablero2_oculto[i, j] <= 4:
                    tablero2_oculto[i, j] = 0

        # filas
        for i in range(size):
            #imprime el eje de coordenadas alfabético (A, B, C a J)
            letra = chr(ord("A") + i)
            
            # Si el tablero tiene encabezado (11x11), accede a tablero[i+1]
            # Si es solo datos (10x10), accede a tablero[i]
            fila_index = i + 1 if tablero1.shape[0] == 11 else i
            # Para cada celda en la fila, mostrar el gráfico correspondiente o el número si no hay gráfico definido en GRAFICS
            fila1 = "".join(f"{GRAFICS.get(int(celda), str(celda)):>3}" for celda in tablero1[fila_index][1:])
            fila2 = "".join(f"{GRAFICS.get(int(celda), str(celda)):>3}" for celda in tablero2_oculto[fila_index][1:])

            print(f" {letra} {fila1}     {letra} {fila2}")
    
    def disparar(self, row, col):
        """
        Realiza un disparo en las coordenadas (row, col).
        Devuelve True si hay barco, False si es agua.
        row, col son índices 0-9 del tablero real
        """
        # Convertir a índices de la matriz (sumar 1 para saltar encabezados)
        matriz_row = row + 1
        matriz_col = col + 1
        
        # Verificar si ya se disparó aquí
        celda_actual = int(self.grid[matriz_row, matriz_col])
        if celda_actual in [6, 5]:  # Ya disparado (impacto o agua)
            print("Ya disparaste aquí!")
            return None
        
        # Comprobar si hay barco (tu tabla tiene lo que necesites)
        # Asumiendo que un barco es cualquier cosa que no sea vacío
        if celda_actual != 0:  # Hay barco
            self.grid[matriz_row, matriz_col] = 6  # Marcar impacto
            return True
        else:
            self.grid[matriz_row, matriz_col] = 5  # Marcar agua
            return False
    
    def have_ships(self):
        """Comprueba si aún hay barcos sin hundir"""
        # Buscar cualquier celda con valor de barco (1-4)
        return np.any((self.grid >= 1) & (self.grid <= 4))

    def get_ship_count(self):
        """Devuelve el número de células de barco restantes"""
        # Contar celdas con valores 1-4 (barcos)
        return np.sum((self.grid >= 1) & (self.grid <= 4))
    
def validar_coordenadas(coordenadas):
    """Valida que las coordenadas ingresadas sean correctas (ej: A5)"""
    if len(coordenadas) < 2:
        raise ValueError("Formato inválido. Usa letra+número (ej: A5)")
    
    fila = coordenadas[0]
    col = coordenadas[1:]

    if not fila.isalpha() or not col.isdigit():
        raise ValueError("Formato inválido. Usa letra+número (ej: A5)")
    
    fila_index = ord(fila) - ord('A')
    col_index = int(col) - 1
    #print(f"Coordenadas convertidas a índices: ({fila_index}, {col_index})")
    if not (0 <= fila_index <= 10 and 0 <= col_index <= 10):
        raise ValueError("Coordenadas fuera del rango. Usa A-J y 1-10")
    
    return fila_index, col_index

