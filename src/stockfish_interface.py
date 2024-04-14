"""
Handle interactions with the Stockfish chess engine.
"""

import chess
import chess.engine
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class StockfishInterface:
    def __init__(self, path_to_engine="stockfish/16.1/bin/stockfish"):
        self.engine = chess.engine.SimpleEngine.popen_uci(os.path.join(ROOT_DIR, path_to_engine))
        self.engine.configure({"Skill Level": 10})
        self.board = chess.Board()

    def get_current_fen(self):
        return self.board.fen()

    def make_move(self, move):
        try:
            move = self.board.parse_san(move)
            self.board.push(move)
            self.print_board()
            return True
        except ValueError:
            return False
    
    def print_board(self):
        print("Current board layout:")
        print(self.board) 
    
    def engine_move(self, time_limit=0.1):
        result = self.engine.play(self.board, chess.engine.Limit(time=time_limit))
        self.board.push(result.move)
        self.print_board()

    # def __del__(self):
    #     self.engine.quit()
