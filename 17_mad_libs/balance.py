#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-09-05
Purpose: Tiny Python Projects balanced brackets exercise
"""

import sys
import argparse


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description='Balanced brackets checker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file',
                        type=argparse.FileType('rt'),
                        metavar='FILE')

    return parser.parse_args()

def match(open, close):
    """Deterine if brackets match"""
    if open == '(' and close == ')':
        return True
    if open == '[' and close == ']':
        return True
    if open == '{' and close == '}':
        return True
    return False

def main():
    """Main program"""

    args = get_args()
    text = args.file.read().rstrip()
    stack = []
    for index, char in enumerate(text):
        if char in ['(', '[', '{']:
            stack.append(char)
        elif (char in [')', ']', '}']):
            if not stack:
                sys.exit(f'Unbalanced "{char}" at {index}, stopping.')
            elif not match(stack.pop(), char):
                sys.exit(f'Unmatched "{char}" at {index}, stopping.')
    if stack:
        sys.exit(f'Unbalanced "{stack.pop()}" at end of file.')


if __name__ == '__main__':
    main()
