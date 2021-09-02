#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-09-01
Purpose: Tiny Python Projects southern speech exercise
"""

import os
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
    """Drop 'g' from '-ing' words, change 'you' to 'y'all'"""
    ing_match = re.search(r'(.+)ing$', word)
    you_match = re.match(r'([yY])ou$', word)
    if ing_match:
        first = ing_match.group(1)
        if re.search('[aeiouy]', first, re.IGNORECASE):
            return first + "in'"
    elif you_match:
        return you_match.group(1) + "'all"
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
    splitter = re.compile(r'(\W+)')
    for line in args.text.splitlines():
        print(''.join(map(fry, splitter.split(line.rstrip()))))


if __name__ == '__main__':
    main()
