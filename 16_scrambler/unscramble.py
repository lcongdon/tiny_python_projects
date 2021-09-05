#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-09-02
Purpose: Tiny Python Projects unscramble exercise
"""

from operator import pos
import os
import argparse
import re


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description='Unscramble words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        help='Input text or file',
                        metavar='text')

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text, "r", encoding="utf-8").read()
    return args


def anagram(word):
    """Return a list of word anagrams"""
    sorted_word = ''.join(sorted(word))
    entries = {}
    with open("./test_dictionary.txt", "r", encoding='utf-8') as dictionary:
        for entry in dictionary.read().split():
            sorted_entry = ''.join(sorted(entry))
            if sorted_entry not in entries:
                entries[sorted_entry] = []
            entries[sorted_entry].append(entry)
    if sorted_word in entries:
        return entries[sorted_word]
    else:
        return []


def unscramble(word):
    """Unscramble a word"""
    if len(word) > 3 and re.match(r'\w+', word):
        for possible_word in anagram(word):
            if (possible_word[0] == word[0]) & (possible_word[-1] == word[-1]):
                word = possible_word

    return word


def main():
    """Main program"""

    args = get_args()
    splitter = re.compile(r"([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")
    for line in args.text.splitlines():
        print(''.join(map(unscramble, splitter.split(line.rstrip()))))


if __name__ == '__main__':
    main()
