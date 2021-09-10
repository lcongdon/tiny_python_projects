#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-09-10
Purpose: Tiny Python Projects interactive tic tac toe exercise
"""

import sys
from typing import NamedTuple, List, Optional
from tabulate import tabulate

class State(NamedTuple):
    board: List[str] = list('.' * 9)
    player: str = 'X'
    quit: bool = False
    draw: bool = False
    error: Optional[str] = None
    winner: Optional[str] = None

def format_board(state) -> str:
    """Format the board state for display"""
    board = state.board
    board = [str(index) if char == '.' else char for index, char in enumerate(board, 1)]
    board = [list(board[:3]), list(board[3:6]), list(board[6:])]
    return tabulate(board, tablefmt="grid").replace("+", "-")

def find_winner(state) -> State:
    """Determine whether there is a winner"""
    board = state.board
    player = state.player
    for player in "XO":
        if board[0] == board[1] == board[2] == player:
            return state._replace(winner=player)
        if board[3] == board[4] == board[5] == player:
            return state._replace(winner=player)
        if board[6] == board[7] == board[8] == player:
            return state._replace(winner=player)
        if board[0] == board[3] == board[6] == player:
            return state._replace(winner=player)
        if board[1] == board[4] == board[7] == player:
            return state._replace(winner=player)
        if board[2] == board[5] == board[8] == player:
            return state._replace(winner=player)
        if board[0] == board[4] == board[8] == player:
            return state._replace(winner=player)
        if board[2] == board[4] == board[6] == player:
            return state._replace(winner=player)
    return state

def find_draw(state) -> State:
    """Determine if the game is a draw"""
    return state if '.' in state.board else state._replace(draw=True)

def get_input(state) -> State:
    """Get input and update player and board"""
    player = state.player
    board = state.board
    valid_input = False
    while not valid_input:
        move = input(f"Player {player}, what is your move? [q to quit] ")
        if move == 'q':
            return state._replace(quit=True)
        try:
            move_int = int(move)
        except ValueError:
            print(f'Invalid cell "{move}", please use 1-9')
            continue
        if move_int < 1 or move_int > 9:
            print(f'Invalid cell "{move}", please use 1-9')
            continue
        if board[move_int - 1] != '.':
            print(f'Cell "{move}" already taken')
            continue
        valid_input = True
    board[move_int - 1] = player 
    player = 'X' if player == 'O' else 'O'
    return state._replace(board=board, player=player)


def main() -> None:
    """Main program"""

    state = State()
    while True:
        print("\033[H\033[J")
        print(format_board(state))
        state = get_input(state)
        if state.quit:
            print("You lose, loser!")
            sys.exit()
        state = find_winner(state)
        if state.winner:
            print(format_board(state))
            print(f'{state.winner} has won!')
            sys.exit()
        state = find_draw(state)
        if state.draw:
            print(format_board(state))
            print("No winner.")
            sys.exit()

if __name__ == '__main__':
    main()
