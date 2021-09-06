#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-09-06
Purpose: Tiny Python Projects find 666 words
"""

import os
import sys
import argparse
import re


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description='Find 666 words',
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

def word2num(word):
    """Compute sum of ordinal value of characters"""
    return str(sum(map(ord, clean(word))))

def main():
    """Main program"""

    args = get_args()
    found = False
    for line in args.text.splitlines():
        matches = filter(lambda x: word2num(x) == '666', line.split())
        for word in matches: 
            found = True
            print(word)
    if not found:
        sys.exit(1)

if __name__ == '__main__':
    main()
