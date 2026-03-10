import os

def limpiar_consola():
    # os.name nos dice el sistema operativo ('nt' es Windows, 'posix' es Unix/Mac)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
