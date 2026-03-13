'''
hundir la Flota

'''

import src.utils.helpers as helpers
from src.utils.constants import HEADER
from src.board.board import Board
from src.game.game import mecanica_juego
import numpy as np

helpers.limpiar_consola()
print(HEADER)

def main():
    # Crear tableros
    table_user = Board()
    table_pc = Board()
    
    # Preguntar al usuario cómo quiere colocar sus barcos
    print("\n¿Cómo deseas colocar tus barcos?")
    print("1. Automáticamente (aleatorio)")
    print("2. Manualmente (ingresa las coordenadas)")
    
    while True:
        opcion = input("\nSelecciona 1 o 2: ").strip()
        if opcion in ['1', '2']:
            break
        print("Opción inválida. Por favor, ingresa 1 o 2.")
    
    # Colocar barcos según la opción del usuario
    if opcion == '1':
        helpers.limpiar_consola()
        print(HEADER)
        print("Colocando tus barcos automáticamente...")
        table_user.grid = table_user.put_ships(table_user.grid, table_pc.grid)
    else:
        helpers.limpiar_consola()
        print(HEADER)
        table_user.grid = table_user.put_ships_manual(table_user.grid, table_pc.grid)
    
    # Colocar barcos de la máquina automáticamente
    table_pc.grid = table_pc.put_ships_pc(table_pc.grid)
    
    mecanica_juego(table_pc.grid, table_user.grid)
    

if __name__ == "__main__":
    main()