import os
import time
from .constants import EXIT_MESSAGE
from .constants import RESET_MESSAGE


def limpiar_consola():
    # os.name nos dice el sistema operativo ('nt' es Windows, 'posix' es Unix/Mac)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def exit_game():
    limpiar_consola()
    print(EXIT_MESSAGE)
    time.sleep(2)
    limpiar_consola()
    exit()

def reset_game():
    limpiar_consola()
    print(RESET_MESSAGE)
    time.sleep(2)
    # Importar main dinámicamente desde la raíz del proyecto
    import sys
    from pathlib import Path
    ruta_raiz = str(Path(__file__).parent.parent.parent)  # Subir a proyecto/
    if ruta_raiz not in sys.path:
        sys.path.insert(0, ruta_raiz)
    from main import main
    main()