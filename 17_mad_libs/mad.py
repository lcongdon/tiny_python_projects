#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-09-05
Purpose: Tiny Python Projects Mad Libs exercise
"""

import sys
import argparse
import re


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description='Mad Libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-i',
                        '--inputs',
                        nargs='*',
                        default='',
                        type=str,
                        help='Input strings (for testing)',
                        metavar='input')

    parser.add_argument('file',
                        help='Input file',
                        type=argparse.FileType('rt'),
                        metavar='FILE')

    return parser.parse_args()


def main():
    """Main program"""

    args = get_args()
    text = args.file.read().rstrip()
    pattern = re.compile(r'(<([^<>]+)>)')
    matches = re.findall(pattern, text)
    if not matches:
        sys.exit(f'"{args.file.name}" has no placeholders.')
    if not args.inputs:
        args.inputs = []
        for _, name in matches:
            article = 'an' if name[0].lower() in 'aeiou' else 'a'
            args.inputs.append(input(f'Give me {article} {name}: '))
    for replacement in args.inputs:
        text = re.sub(pattern, replacement, text, count=1)
    print(text)

if __name__ == '__main__':
    main()
