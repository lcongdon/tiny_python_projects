#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-09-01
Purpose: Tiny Python Projects southern speech exercise
"""

import os
import io
import argparse
import re


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description='Southern speech',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        help='Input text or file',
                        metavar='text')

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text, "r", encoding="utf-8").read()
    return args

def fry(word):
    match = re.search(r'(.+)ing$', word)
    if match is not None:
        first = match.group(1)
        match = re.search('[aeiouy]', first.lower())
        if match is not None:
            return first + "in'"
        else:
            return word
    match = re.match(r'([yY])ou$', word)
    if match is not None:
        return match.group(1) + "'all"
    return word


def test_fry():
    assert fry('you') == "y'all"
    assert fry('You') == "Y'all"
    assert fry('fishing') == "fishin'"
    assert fry('Aching') == "Achin'"
    assert fry('swing') == "swing"


def main():
    """Main program"""

    args = get_args()
    for line in args.text.splitlines():
        words = []
        for word in re.split(r'(\W+)', line.rstrip()):
            words.append(fry(word))
        print(''.join(words))

if __name__ == '__main__':
    main()
