from itictactoe import format_board, find_winner, find_draw, State
import random


# --------------------------------------------------
def test_board_default_state():
    """makes default board"""

    board = """
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
""".strip()
    state = State()
    assert format_board(state) == board


# --------------------------------------------------
def test_board_with_state():
    """makes board"""

    board = """
-------------
| 1 | 2 | 3 |
-------------
| O | X | X |
-------------
| 7 | 8 | 9 |
-------------
""".strip()
    state = State(board="...OXX...")
    assert format_board(state) == board


# --------------------------------------------------
def test_winning():
    """test winning states"""

    wins = [
        ("PPP......"),
        ("...PPP..."),
        ("......PPP"),
        ("P..P..P.."),
        (".P..P..P."),
        ("..P..P..P"),
        ("P...P...P"),
        ("..P.P.P.."),
    ]

    for player in "XO":
        other_player = "O" if player == "X" else "X"

        for state in wins:
            state = state.replace("P", player)
            dots = [i for i in range(len(state)) if state[i] == "."]
            mut = random.sample(dots, k=2)
            test_state = State(
                board="".join(
                    [other_player if i in mut else state[i] for i in range(len(state))]
                )
            )
            assert find_winner(test_state).winner == player


# --------------------------------------------------
def test_losing():
    """test losing states"""

    losing_state = list("XXOO.....")

    for i in range(10):
        random.shuffle(losing_state)
        assert find_winner(State(board="".join(losing_state))).winner == None


# --------------------------------------------------
def test_draw():
    """test draw states"""

    draw_state = list("XXOOOXXOX")
    assert find_draw(State(board="".join(draw_state))).draw == True
