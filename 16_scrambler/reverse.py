#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-09-02
Purpose: Tiny Python Projects reverse exercise
"""

import os
import argparse
import re


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description='Reverse words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        help='Input text or file',
                        metavar='text')

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text, "r", encoding="utf-8").read()
    return args


def reverse(word):
    """Reverse a word"""
    if re.match(r'\w+', word):
        return word[::-1]
    else:
        return word



def test_reverse():
    """Test reverse function"""
    assert reverse("a") == "a"
    assert reverse("ab") == "ba"
    assert reverse("abc") == "cba"
    assert reverse("neat") == "taen"
    assert reverse("anode") == "edona"
    assert reverse("bustle") == "eltsub"
    assert reverse("spiders") == "sredips"


def main():
    """Main program"""

    args = get_args()
    splitter = re.compile(r"([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")
    for line in args.text.splitlines():
        print(''.join(map(reverse, splitter.split(line.rstrip()))))


if __name__ == '__main__':
    main()
