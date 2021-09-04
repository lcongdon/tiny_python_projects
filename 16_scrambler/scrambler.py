#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-09-02
Purpose: Tiny Python Projects scrambler exercise
"""

import os
import argparse
import random
import re


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description='Scramble words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s',
                        '--seed',
                        type=int,
                        default=None,
                        help='Random number generator seed',
                        metavar='seed')

    parser.add_argument('text',
                        help='Input text or file',
                        metavar='text')

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text, "r", encoding="utf-8").read()
    return args


def scramble(word):
    """Scramble a word"""
    if len(word) > 3 and re.match(r'\w+', word):
        middle = list(word[1:-1])
        random.shuffle(middle)
        word = word[0] + ''.join(middle) + word[-1]

    return word

def test_scramble():
    """Test Scramble function"""
    state = random.getstate()
    random.seed(1)
    assert scramble("a") == "a"
    assert scramble("ab") == "ab"
    assert scramble("abc") == "abc"
    assert scramble("abcd") == "acbd"
    assert scramble("abcde") == "acbde"
    assert scramble("abcdef") == "aecbdf"
    assert scramble("abcde'f") == "abcd'ef"
    random.setstate(state)


def main():
    """Main program"""

    args = get_args()
    random.seed(args.seed)
    splitter = re.compile(r"([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")
    for line in args.text.splitlines():
        print(''.join(map(scramble, splitter.split(line))))

if __name__ == '__main__':
    main()
