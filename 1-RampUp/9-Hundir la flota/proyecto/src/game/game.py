'''
Este módulo contiene la logica principal del juego
'''
from . import turn
import numpy as np
from ..board.board import Board
import time
from ..utils.constants import NUM_SHIPS
from ..utils.constants import SIZE_SHIPS
from ..utils.constants import VICTORY_MESSAGE
from ..utils.constants import LOSER_MESSAGE
from ..utils.helpers import reset_game
from ..utils.helpers import exit_game

puntos_totales = sum(SIZE_SHIPS[ship] * NUM_SHIPS[ship] for ship in NUM_SHIPS)  # Total de puntos necesarios para ganar

def mecanica_juego(table_pc, table_user):
    # Aquí se implementará la lógica principal del juego, como el bucle de turnos, la verificación de ganadores, etc.
    while True:
        continue_user = True
        while continue_user == True:
            # Turno del jugador
            print("\nTurno del jugador: Dispara a coordenadas del enemigo")
            my_point = np.sum(table_pc == 6)
            enemy_point = np.sum(table_user == 6)
            print(f"Puntos del jugador: {my_point} / {puntos_totales}")
            print(f"Puntos de la máquina: {enemy_point} / {puntos_totales}")
            coordenadas_usuario = turn.obtener_coordenadas_usuario(table_pc)
            # Aquí se debería verificar si el disparo fue un acierto o un fallo, actualizar el tablero, etc.
            continue_user = turn.comprobar_acierto(table_pc, coordenadas_usuario)
            Board.mostrar_dos_tableros(table_user, table_pc)
            verificar_ganador(table_pc, table_user)
        
        continue_pc = True
        while continue_pc == True:
            # Turno de la máquina
            print("\nTurno de la máquina: Dispara aleatoriamente a tu tablero")
            time.sleep(2)  # Simular tiempo de pensamiento de la máquina
            coordenadas_maquina = turn.disparar_a_maquina(table_user)    
            continue_pc = turn.comprobar_acierto(table_user, coordenadas_maquina)
            Board.mostrar_dos_tableros(table_user, table_pc)
            verificar_ganador(table_pc, table_user)
    
    
def verificar_ganador(table_pc, table_user):
    # Aquí se implementará la lógica para verificar si el jugador o la máquina ha ganado el juego
    
    if np.sum(table_pc == 6) == puntos_totales:
        print(VICTORY_MESSAGE)
        reiniciar_juego()
        return True
    elif np.sum(table_user == 6) == puntos_totales:
        print(LOSER_MESSAGE)
        reiniciar_juego()
        return True
    
def reiniciar_juego():
    print("pulsa 1 para reiniciar el juego o 2 para salir")
    opcion = input()
    if opcion == "1":
        reset_game()
    elif opcion == "2":
        exit_game()