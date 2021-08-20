#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-08-16
Purpose: Tiny Python Projects rhymer exercise
"""

import sys
import os
import argparse
import re
import string

VOWELS = "aeiou"
CONSONANTS = "".join(
    [char for char in string.ascii_lowercase if char not in VOWELS])
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

PREFIXES = list(CONSONANTS) + GROUPS


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

    parser.add_argument(
        "-o",
        "--outfile",
        default=sys.stdout,
        type=argparse.FileType("wt"),
        help="Output file",
        metavar="FILE",
    )
    # parser.add_argument(
    #     "-d",
    #     "--outdir",
    #     default = '.',
    #     help="Output directory",
    #     metavar="str",
    #     type=str,
    # )
    parser.add_argument(
        "text",
        type=str,
        help="Input text or file",
        metavar="text",
    )

    args = parser.parse_args()

    args.handles = []
    if os.path.isfile(args.text):
        for line in open(args.text):
            for word in line.split():
                args.handles.append((word, word + ".txt"))
    else:
        args.handles.append((args.text, args.outfile))
    return args


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
    exit_code = 0
    args = get_args()
    for word, outfile in args.handles:
        first_part, second_part = stemmer(word)
        if second_part:
            if isinstance(outfile, str):
                outfile = open(outfile, "wt")
            outfile.write(
                "\n".join(
                    sorted(
                        [
                            prefix + second_part
                            for prefix in PREFIXES
                            if prefix != first_part
                        ]
                    )
                )
            )
        else:
            sys.stderr.write(f'Cannot rhyme "{word}"\n')
            exit_code = 1
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
