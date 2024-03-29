START_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"


PLAYER_WHITE = True


LEGAL_FILTER = True


ENGINE_MOVE_TIME = 1000


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


STEP_X = SCREEN_WIDTH // 8
STEP_Y = SCREEN_HEIGHT // 8


LIGHT_SQ_COLOUR = (146, 215, 240)
DARK_SQ_COLOUR = (51, 48, 240)
LEGAL_MOVE_COLOUR = (10, 40, 89)


PIECE_VALUES = {
    "pawn" : 1,
    "knight" : 2,
    "bishop" : 3,
    "rook" : 4,
    "king" : 5,
    "queen" : 6
}