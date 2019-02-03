"""docstring"""
import board

BOARD_SIZE = (10, 10) #horizontal, vertical

HIDDEN_BOARD_P1 = []
VISIBLE_BOARD_P1 = []
HIDDEN_BOARD_P2 = []
VISIBLE_BOARD_P2 = []

PLAYER_BOARD = {"p1": HIDDEN_BOARD_P1, "p2": HIDDEN_BOARD_P2
}

def init_board():
    """This function initializes boards, by using the init_board function"""
    global HIDDEN_BOARD_P1, VISIBLE_BOARD_P1
    HIDDEN_BOARD_P1 = board.init_board(BOARD_SIZE)
    VISIBLE_BOARD_P1 = board.init_board(BOARD_SIZE)


def check_for_hit(area, player):
    """Selects the player to check for hit, then goes to the location where
    the shot was made via a dictionairy, and then checks for hit"""
    board_to_check = []
    horizontal = 0
    vertical = 0
    if player.lower() == "p1":
        board_to_check = HIDDEN_BOARD_P1
    elif player.lower() == "p2":
        board_to_check = HIDDEN_BOARD_P2

    vertical = board.LETTER_TO_NUMBER[area[0]]-1
    horizontal = int(area[1])

    if vertical in range(BOARD_SIZE[1]) and horizontal in range(BOARD_SIZE[0]):
        if board_to_check[vertical][horizontal] == "O":
            return "Hit"
        return "Miss"
    return "Out of bounds"

def set_ship(player, begin_ship, end_ship):
    """This function checks if a ship can be set somewhere, and sets it if it
    can indeed be set there."""
    board_to_check = PLAYER_BOARD[player]
    print(board_to_check)
    if begin_ship[0] == end_ship[0]:
        for i in range(begin_ship[1], end_ship[1]):
            pass


init_board()
HIDDEN_BOARD_P1[0][1] = "O"
print(set_ship("p1", 5,6))
#print(board.LETTER_TO_NUMBER["A"])
print(check_for_hit("A1", "P1"))
