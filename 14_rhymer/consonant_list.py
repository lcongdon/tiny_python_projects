#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-08-20
Purpose: Build list of consonants exercise from Tiny Python Projects
"""

import string
import argparse
import sys
import re

VOWELS = "aeiou"
CONSONANTS = "".join(
    [char for char in string.ascii_lowercase if char not in VOWELS])

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

def breaker(word):
    """Break the word into vowel and consonant strings and return consonants"""
    result = set()
    # loop for the word parameter, finding consonant strings, drop trailing vowels
    pattern = f"([{CONSONANTS}]+)?([{VOWELS}])(.*)"
    word = word.lower()
    match = re.match(pattern, word)
    # if match, add to result set
    return result

def test_breaker():
    """Test breaker"""
    assert breaker("") == set()
    assert breaker("cake") == {'c', 'k'}
    assert breaker("chair") == {'ch', 'r'}
    assert breaker("apple") == {'ppl'}
    assert breaker("APPLE") == {'ppl'}
    assert breaker('123') == set()
    assert breaker('RDZNL') == {'rdznl'}


def main():
    """Main program"""

    args = get_args()
    consonants = set()
    for line in args.infile:
        for word in line.split():
            consonants.update(breaker(word))
    print(sorted(consonants) if consonants else "No consonants found")

if __name__ == '__main__':
    main()
