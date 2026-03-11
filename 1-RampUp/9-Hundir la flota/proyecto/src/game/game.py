'''
Este módulo contiene la logica principal del juego
'''
from . import turn
import time

def mecanica_juego(table_pc, table_user):
    # Aquí se implementará la lógica principal del juego, como el bucle de turnos, la verificación de ganadores, etc.
    while True:
        continue_user = True
        while continue_user == True:
            # Turno del jugador
            print("\nTurno del jugador: Dispara a coordenadas del enemigo")
            coordenadas_usuario = turn.obtener_coordenadas_usuario(table_pc)
            # Aquí se debería verificar si el disparo fue un acierto o un fallo, actualizar el tablero, etc.
            continue_user = turn.comprobar_acierto(table_pc, coordenadas_usuario)
            table_user.mostrar_dos_tableros(table_user.grid, table_pc.grid)
        
        continue_pc = True
        while continue_pc == True:
            # Turno de la máquina
            print("\nTurno de la máquina: Dispara aleatoriamente a tu tablero")
            time.sleep(2)  # Simular tiempo de pensamiento de la máquina
            coordenadas_maquina = turn.disparar_a_maquina(table_user)    
            continue_pc = turn.comprobar_acierto(table_user, coordenadas_maquina)
            table_pc.mostrar_dos_tableros(table_user.grid, table_pc.grid)
    