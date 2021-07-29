#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-07-29
Purpose: Tiny Python Project Twelve Days of Christmas exercise
"""

import argparse
import sys


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description="Twelve Days of Christmas",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-n",
        "--num",
        default=12,
        type=int,
        help="Number of days to sing",
        metavar="days",
    )

    parser.add_argument(
        "-o",
        "--outfile",
        default=sys.stdout,
        type=argparse.FileType("wt"),
        help="Outfile",
        metavar="FILE",
    )

    args = parser.parse_args()

    if args.num < 1 or args.num > 12:
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


def verse(day):
    """Return the verse for day"""
    ordinal = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth",
    ]
    phrase = [
        "And a partridge in a pear tree.",
        "Two turtle doves,",
        "Three French hens,",
        "Four calling birds,",
        "Five gold rings,",
        "Six geese a laying,",
        "Seven swans a swimming,",
        "Eight maids a milking,",
        "Nine ladies dancing,",
        "Ten lords a leaping,",
        "Eleven pipers piping,",
        "Twelve drummers drumming,",
    ]
    alt_phrase = "A partridge in a pear tree."

    result = [
        f"On the {ordinal[day - 1]} day of Christmas,",
        "My true love gave to me,",
    ]

    result.extend(reversed(phrase[1:day]))
    result.append(f"{phrase[0] if day != 1 else alt_phrase}")
    return "\n".join(result)


def test_verse():
    assert verse(1) == "\n".join(
        [
            "On the first day of Christmas,",
            "My true love gave to me,",
            "A partridge in a pear tree.",
        ]
    )
    assert verse(2) == "\n".join(
        [
            "On the second day of Christmas,",
            "My true love gave to me,",
            "Two turtle doves,",
            "And a partridge in a pear tree.",
        ]
    )


def main():
    """Main program"""

    args = get_args()
    # for day in range(1, args.num + 1):
    #     print(verse(day), end='\n\n')
    args.outfile.write("\n\n".join(verse(day) for day in range(1, args.num + 1)) + "\n")


if __name__ == "__main__":
    main()
