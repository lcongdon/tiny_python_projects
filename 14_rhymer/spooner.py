#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-09-01
Purpose: Tiny Python Projects spoonerism exercise
"""

import sys
import argparse
import re
import string


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description="Spoonerize words",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "text",
        nargs=2,
        type=str,
        help="Input words, 2 required",
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
    word1, word2 = args.text
    first_part1, second_part1 = stemmer(word1)
    first_part2, second_part2 = stemmer(word2)
    if (first_part1 == "") | (first_part2 == "") | (second_part1 == "") | (second_part2 == ""):
        sys.stderr.write(f'Cannot spoonerize "{word1} {word2}"\n')
        exit_code = 1
    else:
        print(first_part2 + second_part1 + ' ' + first_part1 + second_part2)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
