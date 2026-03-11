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
    table_user.mostrar_dos_tableros(table_user.grid, table_pc.grid)
    
    print("\n¡BIENVENIDO A HUNDIR LA FLOTA!")
    print("Turno del jugador: Dispara a coordenadas del enemigo")
    print("Las máquinas disparan aleatoriamente a tu tablero\n")
    
    mecanica_juego(table_pc, table_user)
    

if __name__ == "__main__":
    main()