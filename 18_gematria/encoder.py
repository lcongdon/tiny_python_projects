#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-09-06
Purpose: Tiny Python Projects assign EBCDIC numbers to words
"""

import os
import argparse
import re
import functools


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description='Assign EBCDIC bnumbers to words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        help='Input text or file',
                        metavar='text')

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    return args

def clean(word):
    """Remove all non-numbers and non-letters"""
    pattern = re.compile(r'[^A-Za-z0-9]')
    return re.sub(pattern, '', word)

def encoder(word):
    """Convert characters to list of EBCDIC values"""
    return [int.from_bytes(char.encode('cp500'), byteorder='big') for char in word] 

def word2num(word):
    """Compute sum of EBCDIC value of characters"""
    return str(sum(encoder(clean(word))))

def main():
    """Main program"""

    args = get_args()
    for line in args.text.splitlines():
        print(' '.join(map(word2num, line.split())))

if __name__ == '__main__':
    main()