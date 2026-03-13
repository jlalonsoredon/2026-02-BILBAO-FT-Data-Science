import random
class Ship:
    '''
    En esta clase se definen los barcos y la colocación de estos en el trablero.
    '''
    name = ''
    size = 0
    position = []
    def __init__(self, name, size, table):
        self.name = name
        self.size = size
        self.table = table
    def __str__(self):        
        return f'{self.name} de tamaño {self.size}'
    
    def place(self, position, table):
        self.position = position
        orientation = self.ship_orientation()
        while True:
            try:
                coordenadas = input("Introduce las coordenada (ej: A5): ").upper().strip()
                coordenadas = self.validar_coordenadas(coordenadas, self.table)
                if coordenadas in self.position:
                    raise ValueError("Ya colocaste un barco aquí! Introduce otras coordenadas.")
                elif orientation == 'H' and (coordenadas[1] + self.size - 1 > 10):
                    raise ValueError("El barco no cabe horizontalmente en esa posición. Introduce otras coordenadas.")
                elif orientation == 'V' and (coordenadas[0] + self.size - 1 > 10):
                    raise ValueError("El barco no cabe verticalmente en esa posición. Introduce otras coordenadas.")
                elif orientation == 'H' and any(table[coordenadas[0], col] != 0 for col in range(coordenadas[1], coordenadas[1] + self.size)):
                    raise ValueError("Ya hay un barco en esa posición horizontalmente. Introduce otras coordenadas.")
                elif orientation == 'V' and any(table[fila, coordenadas[1]] != 0 for fila in range(coordenadas[0], coordenadas[0] + self.size)):
                    raise ValueError("Ya hay un barco en esa posición verticalmente. Introduce otras coordenadas.")

                else:
                    break
            except ValueError as e:
                print(f"Error: {e}")
        fila = coordenadas[0]
        col = coordenadas[1]
        if orientation == 'H':
            self.position = [(fila, col + i) for i in range(self.size)]
        else:
            self.position = [(fila + i, col) for i in range(self.size)]
            
    def generate_random_position(self, table):
        while True:
            orientation = random.choice(['H', 'V'])
            if orientation == 'H':
                row = random.randint(1, 10)
                col = random.randint(1, 11 - self.size)  # Evitar salirse del tablero
                coordenadas = [(row, col + i) for i in range(self.size)]
                # Verificar si todos los espacios están vacíos
                if all(table[row, col + i] == 0 for i in range(self.size)):
                    self.position = coordenadas
                    return coordenadas
            else:  # 'V'
                row = random.randint(1, 11 - self.size)  # Evitar salirse del tablero
                col = random.randint(1, 10)
                coordenadas = [(row + i, col) for i in range(self.size)]
                # Verificar si todos los espacios están vacíos
                if all(table[row + i, col] == 0 for i in range(self.size)):
                    self.position = coordenadas
                    return coordenadas

    def ship_orientation(self):
        while True:
            orientation = input(f"¿Quieres colocar el {self.name} de {self.size} casillas de forma horizontal (H) o vertical (V)? ").upper()
            if orientation in ['H', 'V']:
                break
            else:
                print("Entrada no válida. Por favor, ingresa 'H' para horizontal o 'V' para vertical.")
        return orientation
    
    def validar_coordenadas(self, coordenadas, table):
        """Valida el formato de las coordenadas ingresadas por el usuario (string como 'A5')"""
        if len(coordenadas) < 2:
            raise ValueError("Formato inválido. Usa letra+número (ej: A5)")
            
        fila = ord(coordenadas[0]) - ord('A')  # Convertir letra a índice (A=0, B=1, etc)
        col = int(coordenadas[1:])  # Convertir número a índice (1=0, 2=1, etc)
        fila += 1  # Ajustar fila para que coincida con el tablero (A=1, B=2, etc)
        if not (0 <= fila <= 10 and 0 <= col <= 10): #si las coordenas no son correctas
            raise ValueError("Coordenadas fuera del rango. Usa A-J y 1-10")

        return fila, col