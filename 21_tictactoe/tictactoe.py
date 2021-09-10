#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-09-09
Purpose: Tiny Python Programs Tic Tac Toe exercise
"""

import argparse
import re
from tabulate import tabulate


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description="Tic-Tac-Toe",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-b",
        "--board",
        default="." * 9,
        type=str,
        help="The state of the board",
        metavar="board",
    )

    parser.add_argument(
        "-c",
        "--cell",
        type=int,
        choices=range(1, 10),
        help="Cell 1-9",
        metavar="cell",
    )

    parser.add_argument(
        "-p",
        "--player",
        type=str,
        choices=("XO"),
        help="Player X or O",
        metavar="player",
    )

    args = parser.parse_args()
    pattern = re.compile(r"^[.XO]{9}$")
    args.board = args.board.upper()
    if not re.search(pattern, args.board):
        parser.error(f'--board "{args.board}" must be 9 characters of ., X, O')
    if (args.cell and not args.player) or (args.player and not args.cell):
        parser.error(f"Must provide both --player and --cell")
    if args.cell and args.player and args.board[args.cell - 1] != ".":
        parser.error(f'--cell "{args.cell}" already taken')
    return args


def format_board(board):
    """Format the board state for display"""
    board = [str(index) if char == '.' else char for index, char in enumerate(board, 1)]
    board = [list(board[:3]), list(board[3:6]), list(board[6:])]
    return tabulate(board, tablefmt="grid").replace("+", "-")


def find_winner(board):
    """Determine whether there is a winner"""
    for player in "XO":
        if board[0] == board[1] == board[2] == player:
            return player
        if board[3] == board[4] == board[5] == player:
            return player
        if board[6] == board[7] == board[8] == player:
            return player
        if board[0] == board[3] == board[6] == player:
            return player
        if board[1] == board[4] == board[7] == player:
            return player
        if board[2] == board[5] == board[8] == player:
            return player
        if board[0] == board[4] == board[8] == player:
            return player
        if board[2] == board[4] == board[6] == player:
            return player
    return None


def main():
    """Main program"""

    args = get_args()
    board = list(args.board)
    if args.cell and args.player:
        board[args.cell - 1] = args.player
    print(format_board(board))
    if result := find_winner(board):
        print(f"{result} has won!")
    else:
        print("No winner.")


if __name__ == "__main__":
    main()
