'''
hundir la Flota

'''

import src.utils.helpers as helpers
from src.utils.constants import header
from src.board.board import Board
from src.game.turn import Turn
from src.game.game import obtener_coordenadas_usuario
import numpy as np

helpers.limpiar_consola()
print(header)

def main():
    # Crear tableros
    tablero_jugador = Board()
    tablero_maquina = Board()
    tablero_jugador.mostrar_dos_tableros(tablero_jugador.grid, tablero_maquina.grid)
    
    # Crear gestor de turnos
    turn_manager = Turn(tablero_jugador, tablero_maquina, "Jugador")
    obtener_coordenadas_usuario()  # Solo para mostrar el mensaje de bienvenida y solicitar la primera coordenada
    
    
    
    print("\n¡BIENVENIDO A HUNDIR LA FLOTA!")
    print("Turno del jugador: Dispara a coordenadas del enemigo")
    print("Las máquinas disparan aleatoriamente a tu tablero\n")
    

    
    # Fin del juego
    ganador = turn_manager.get_winner()
    print(f"\n¡¡¡GAME OVER!!!")
    print(f"¡¡¡{ganador} HA GANADO!!!")

if __name__ == "__main__":
    main()