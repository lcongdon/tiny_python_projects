#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-08-16
Purpose: Tiny Python Projects rhymer exercise
"""

import argparse
from re import S


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description="Make rhyming 'words'", formatter_class=argparse.ArgumentDefaultsHelpFormatter
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

    # parser.add_argument('-f',
    #                     '--file',
    #                     default=None,
    #                     type=argparse.FileType('rt'),
    #                     help='A readable file',
    #                     metavar='FILE')

    # parser.add_argument('-o',
    #                     '--on',
    #                     action='store_true',
    #                     help='A boolean flag')

    parser.add_argument("word", help="Word to rhyme", metavar="word")

    return parser.parse_args()

def stemmer(word):
    """Return leading consonants (if any), and 'stem' of word"""
    pass

def test_stemmer():
    """Test stemmer"""
    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDZNL') == ('rdznl', '')
    assert stemmer('123') == ('123', '')

def main():

    prefixes = [
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
    consonants = [

    ]
    """Main program"""

    args = get_args()
    pos_arg = args.word

    print(f'word = "{pos_arg}"')


if __name__ == "__main__":
    main()
