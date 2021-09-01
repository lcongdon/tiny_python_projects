#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-09-01
Purpose: Tiny Python Projects pig latin exercise
"""

import sys
import os
import argparse
import re
import string


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description="Translate words to pig latin",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "text",
        type=str,
        help="Input text or file",
        metavar="text",
    )

    return parser.parse_args()


def stemmer(word):
    """Return leading consonants (if any), and 'stem' of word"""
    VOWELS = "aeiou"
    CONSONANTS = "".join(
        [char for char in string.ascii_lowercase if char not in VOWELS])
    pattern = f"([{CONSONANTS}]+)?([{VOWELS}])(.*)"
    word = word.lower()
    match = re.match(pattern, word)
    if match:
        part1 = match.group(1) or ""
        part2 = match.group(2) or ""
        part3 = match.group(3) or ""
        return (part1, part2 + part3)
    else:
        return (word, "")


def test_stemmer():
    """Test stemmer"""
    assert stemmer("") == ("", "")
    assert stemmer("pig") == ("p", "ig")
    assert stemmer("cake") == ("c", "ake")
    assert stemmer("smile") == ("sm", "ile")
    assert stemmer("chair") == ("ch", "air")
    assert stemmer("APPLE") == ("", "apple")
    assert stemmer("RDZNL") == ("rdznl", "")
    assert stemmer("123") == ("123", "")


def main():
    """Main program"""
    exit_code = 0
    args = get_args()
    word = args.text
    first_part, second_part = stemmer(word)
    if second_part:
        if first_part:
            print(second_part + first_part + "ay")
        else:
            print(second_part + "yay")
    else:
        sys.stderr.write(f'Cannot translate "{word}"\n')
        exit_code = 1
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
