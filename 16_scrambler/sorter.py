#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-09-02
Purpose: Tiny Python Projects sorter exercise
"""

import os
import argparse
import re


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description='Sort middle of words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        help='Input text or file',
                        metavar='text')

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text, "r", encoding="utf-8").read()
    return args


def sort_middle(word):
    """Sort the middle of a word"""
    if len(word) > 3 and re.match(r'\w+', word):
        middle = sorted(list(word[1:-1]))
        word = word[0] + ''.join(middle) + word[-1]

    return word


def test_sort_middle():
    """Test sort_middle function"""
    assert sort_middle("a") == "a"
    assert sort_middle("ab") == "ab"
    assert sort_middle("abc") == "abc"
    assert sort_middle("neat") == "naet"
    assert sort_middle("anode") == "adnoe"
    assert sort_middle("bustle") == "blstue"
    assert sort_middle("spiders") == "sdeiprs"


def main():
    """Main program"""

    args = get_args()
    splitter = re.compile(r"([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")
    for line in args.text.splitlines():
        print(''.join(map(sort_middle, splitter.split(line.rstrip()))))


if __name__ == '__main__':
    main()
