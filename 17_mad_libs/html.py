#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-09-05
Purpose: Tiny Python Projects html exercise
"""

import sys
import argparse
import re


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description='Mad Libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file',
                        type=argparse.FileType('rt'),
                        metavar='FILE')

    return parser.parse_args()


def main():
    """Main program"""

    args = get_args()
    text = args.file.read().rstrip()
    pattern = re.compile(r'(<[^<>]+>)')
    matches = re.findall(pattern, text)
    if not matches:
        sys.exit(f'"{args.file.name}" has no html.')
    for tag in matches:
        print(tag)


if __name__ == '__main__':
    main()
