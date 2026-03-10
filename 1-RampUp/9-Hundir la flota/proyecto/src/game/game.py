'''
Este módulo contiene la logica principal del juego
'''
def obtener_coordenadas_usuario():
    """Solicita al usuario que ingrese coordenadas y las valida"""
    while True:
        try:
            coordenadas_disparo = input("Ingresa coordenada (ej: A5): ").upper().strip()
            coordenadas = validar_coordenadas(coordenadas_disparo) # Convertir a índices
            print(f"Disparando a {coordenadas}...")
            #coord_matriz = coord_a_indices(coordenadas)
            #print (f"coordenadas: {coord_matriz}")
            return coordenadas
        except ValueError as e:
            print(e)
    

def validar_coordenadas(coordenadas):
    """Valida el formato de las coordenadas ingresadas por el usuario"""
    if len(coordenadas) < 2:
        raise ValueError("Formato inválido. Usa letra+número (ej: A5)")
    
    fila = ord(coordenadas[0]) - ord('A')  # Convertir letra a índice (A=0, B=1, etc)
    col = int(coordenadas[1:])  # Convertir número a índice (1=0, 2=1, etc)
    fila += 1  # Ajustar fila para que coincida con el tablero (A=1, B=2, etc)
    if not (0 <= fila <= 10 and 0 <= col <= 10):
        
        raise ValueError("Coordenadas fuera del rango. Usa A-J y 1-10")
    
    return fila, col

def coord_a_indices(coord):

    fila = ord(coord[0].upper()) - ord("A")
    col = int(coord[1:]) - 1

    return fila, col