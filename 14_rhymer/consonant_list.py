#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-08-20
Purpose: Build list of consonants exercise from Tiny Python Projects
"""

import argparse
import sys


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description='Build list of consonants',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('infile',
                        nargs ='?',
                        default=sys.stdin,
                        type=argparse.FileType('rt'),
                        help='A dictionary file')

    parser.add_argument('outfile',
                        nargs = '?',
                        default=sys.stdout,
                        type=argparse.FileType('wt'),
                        help='A list of consonant groups')

    return parser.parse_args()


def main():
    """Main program"""

    args = get_args()
    print(args.infile)


if __name__ == '__main__':
    main()
