class Turn:
    """Gestiona los turnos del juego"""
    
    def __init__(self, player_board, opponent_board, player_name="Jugador"):
        self.player_board = player_board  # Mi tablero (defensa)
        self.opponent_board = opponent_board  # Tablero del oponente (ataque)
        self.player_name = player_name
        self.is_active = True
    
    def player_turn(self, row, col):
        """
        Ejecuta el turno del jugador.
        Devuelve True si acertó (repite turno), False si falló
        """
        result = self.opponent_board.disparar(row, col)
        return result  # True = impacto, False = agua
    
    def opponent_turn(self):
        """
        Ejecuta el turno del oponente (máquina).
        Dispara a una coordenada aleatoria en el tablero del jugador.
        Devuelve True si acertó, False si falló
        """
        import random
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        result = self.player_board.disparar(row, col)
        return result
    
    def is_game_over(self):
        """Comprueba si el juego ha terminado"""
        return (not self.player_board.have_ships() or 
                not self.opponent_board.have_ships())
    
    def get_winner(self):
        """Devuelve el ganador"""
        if not self.opponent_board.have_ships():
            return self.player_name
        elif not self.player_board.have_ships():
            return "Máquina"
        return None