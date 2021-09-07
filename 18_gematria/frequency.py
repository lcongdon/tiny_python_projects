#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-09-06
Purpose: Tiny Python Projects number assignment frequency
"""

import os
import argparse
import re


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description='Assign numbers to words',
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
    words = dict()
    counts = dict()
    max_count = 0
    for line in args.text.splitlines():
        for word in re.split(r'\W+',line):
            key = word2num(word)
            if key in words:
                words[key].add(word)
            else:
                words[key] = set(word.split())
            if key in counts:
                counts[key] += 1
            else:
                counts[key] = 1
            if counts[key] > max_count:
                max_count = counts[key]
    for key in counts:
        if counts[key] >= max_count:
            print(f'Total occurences: {counts[key]}')
            for element in words[key]:
                print(element)


if __name__ == '__main__':
    main()
