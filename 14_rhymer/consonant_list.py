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
CONSONANTS = "".join([char for char in string.ascii_lowercase if char not in VOWELS])


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description="Build list of consonants",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "infile",
        nargs="?",
        default=sys.stdin,
        type=argparse.FileType("rt"),
        help="A dictionary file",
    )

    parser.add_argument(
        "outfile",
        nargs="?",
        default=sys.stdout,
        type=argparse.FileType("wt"),
        help="A list of consonant groups",
    )

    return parser.parse_args()


def finder(word):
    """Find the consonant strings in the word"""
    pattern = re.compile(f"[{CONSONANTS}]+")
    word = word.lower()
    return re.findall(pattern, word)


def test_finder():
    """Test finder"""
    assert finder("") == []
    assert finder("cake") == ["c", "k"]
    assert finder("chair") == ["ch", "r"]
    assert finder("apple") == ["ppl"]
    assert finder("APPLE") == ["ppl"]
    assert finder("123") == []
    assert finder("RDZNL") == ["rdznl"]


def main():
    """Main program"""

    args = get_args()
    consonants = set()
    for line in args.infile:
        for word in line.split():
            consonants.update(finder(word))
    args.outfile.write(
        "\n".join(sorted(consonants)) if consonants else "No consonants found"
    )
    args.outfile.write("\n")


if __name__ == "__main__":
    main()
