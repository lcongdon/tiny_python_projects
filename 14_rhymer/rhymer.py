#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-08-16
Purpose: Tiny Python Projects rhymer exercise
"""

import argparse
from asyncio.subprocess import STDOUT
import re
import string

VOWELS = "aeiou"
CONSONANTS = "".join([char for char in string.ascii_lowercase if char not in VOWELS])
GROUPS = [
    "bl",
    "br",
    "ch",
    "cl",
    "cr",
    "dr",
    "fl",
    "fr",
    "gl",
    "gr",
    "pl",
    "pr",
    "sc",
    "sh",
    "sk",
    "sl",
    "sm",
    "sn",
    "sp",
    "st",
    "sw",
    "th",
    "tr",
    "tw",
    "thw",
    "wh",
    "wr",
    "sch",
    "scr",
    "shr",
    "sph",
    "spl",
    "spr",
    "squ",
    "str",
    "thr",
]


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description="Make rhyming 'words'",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # parser.add_argument('-a',
    #                     '--arg',
    #                     default='',
    #                     type=str,
    #                     help='A named string argument',
    #                     metavar='str')

    # parser.add_argument('-i',
    #                     '--int',
    #                     default=0,
    #                     type=int,
    #                     help='A named integer argument',
    #                     metavar='int')

    parser.add_argument('-o',
                        '--outfile',
                        default=STDOUT,
                        type=argparse.FileType('wt'),
                        help='Output file',
                        metavar='FILE')

    # parser.add_argument('-o',
    #                     '--on',
    #                     action='store_true',
    #                     help='A boolean flag')

    parser.add_argument("word", help="Word to rhyme", metavar="word")

    return parser.parse_args()


def stemmer(word):
    """Return leading consonants (if any), and 'stem' of word"""
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
    assert stemmer("cake") == ("c", "ake")
    assert stemmer("chair") == ("ch", "air")
    assert stemmer("APPLE") == ("", "apple")
    assert stemmer("RDZNL") == ("rdznl", "")
    assert stemmer("123") == ("123", "")


def main():

    """Main program"""
    args = get_args()
    pos_arg = args.word
    prefixes = list(CONSONANTS) + GROUPS
    first_part, second_part = stemmer(pos_arg)
    if second_part:
       print('\n'.join(sorted([prefix + second_part for prefix in prefixes if prefix != first_part])))
    else:
        print(f'Cannot rhyme "{pos_arg}"')

if __name__ == "__main__":
    main()
