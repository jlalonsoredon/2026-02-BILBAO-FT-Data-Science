import random

class Turn:
    pass

def disparar_a_maquina(table_user):
    #generar coordenadas de disparo aleatorias para la máquina
    while True:
        try:
            fila = random.randint(1, 10)
            col = random.randint(1, 10)
            # Validar que no se haya disparado en este lugar antes
            if table_user.grid[fila, col] == 5 or table_user.grid[fila, col] == 6:
                continue  # Intentar con otras coordenadas
            coordenadas = (fila, col)
            print(f"Disparando a {coordenadas}...")
            return coordenadas
        except ValueError as e:
            print(e)

def obtener_coordenadas_usuario(table_pc):
    """Solicita al usuario que ingrese coordenadas y las valida"""
    while True:
        try:
            coordenadas_disparo = input("Introduce las coordenada (ej: A5): ").upper().strip()
            coordenadas = validar_coordenadas(coordenadas_disparo, table_pc) # Convertir a índices
            print(f"Disparando a {coordenadas}...")
            return coordenadas
        except ValueError as e:
            print(e)
    

def validar_coordenadas(coordenadas, table):
    """Valida el formato de las coordenadas ingresadas por el usuario (string como 'A5')"""
    if len(coordenadas) < 2:
        raise ValueError("Formato inválido. Usa letra+número (ej: A5)")
    
    fila = ord(coordenadas[0]) - ord('A')  # Convertir letra a índice (A=0, B=1, etc)
    col = int(coordenadas[1:])  # Convertir número a índice (1=0, 2=1, etc)
    fila += 1  # Ajustar fila para que coincida con el tablero (A=1, B=2, etc)
    if not (0 <= fila <= 10 and 0 <= col <= 10): #si las coordenas no son correctas
        raise ValueError("Coordenadas fuera del rango. Usa A-J y 1-10")
    # las coordenadas del tablero son distintas de 0, 
    # es que ese disparo ya se ha realizado y deberia pedir al usuario que ingrese otras coordenadas
    print(f"Coordenadas convertidas a índices: ({fila}, {col})")
    print(f"Valor en el tablero de la máquina en esas coordenadas: {table.grid[fila, col]}")
    if (table.grid[fila, col] == 5 or table.grid[fila, col] == 6):
        raise ValueError("Ya disparaste aquí! Introduce otras coordenadas.")
    return fila, col

def comprobar_acierto(table, coordenadas):
    """Comprueba si el disparo del usuario fue un acierto o un fallo"""
    fila, col = coordenadas
    if table.grid[fila, col] == 0:  # No hay nada (agua)
        table.grid[fila, col] = 5  # Marcar agua
        print("¡Agua!")
        return False  # Pierde el turno
    else:  # Hay barco (1-4)
        table.grid[fila, col] = 6  # Marcar impacto
        print("¡Acierto!")
        return True  # Gana otro turno
