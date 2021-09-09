#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-09-09
Purpose: Tiny Python Projects password exercise
"""

import argparse
import random
import re
import string


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description='Password maker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        nargs='+',
                        default=None,
                        type=argparse.FileType('rt'),
                        help='Input file(s)',
                        metavar='FILE')

    parser.add_argument('-n',
                        '--num',
                        default=3,
                        type=int,
                        help='Number of passwords to generate',
                        metavar='num_passwords')

    parser.add_argument('-w',
                        '--num_words',
                        default=4,
                        type=int,
                        help='Number of words to use for password',
                        metavar='num_words')

    parser.add_argument('-m',
                        '--min_word_len',
                        default=3,
                        type=int,
                        help='Minimum word length',
                        metavar='minimum')

    parser.add_argument('-x',
                        '--max_word_len',
                        default=6,
                        type=int,
                        help='Maximum word length',
                        metavar='maximum')

    parser.add_argument('-s',
                        '--seed',
                        default=None,
                        type=int,
                        help='Random seed',
                        metavar='seed')

    parser.add_argument('-l',
                        '--l33t',
                        action='store_true',
                        help='Obfuscate letters')

    return parser.parse_args()


def clean(word):
    """Remove all non-letters"""
    pattern = re.compile(r'[^A-Za-z]')
    return re.sub(pattern, '', word)


def ransom(word):
    """Randomly capitalize characters"""
    return ''.join([char.lower() if random.choice([True, False])
                    else char.upper() for char in word])


def l33t(password):
    """Transform a fraction of password with character substitutions"""
    mapping = {'a': '@', 'A': '4', 'O': '0',
               't': '+', 'E': '3', 'I': '1', 'S': '5'}
    fraction_to_change = 0.1
    len_password = len(password)
    num_changes = round(fraction_to_change * len_password)
    new_password = list(ransom(password))
    for i in random.sample(range(len_password), num_changes):
        new_password[i] = mapping.get(new_password[i], new_password[i])
    return ''.join(new_password) + random.choice(string.punctuation)


def main():
    """Main program"""

    args = get_args()
    random.seed(args.seed)
    words = set()

    def word_len(word):
        return args.min_word_len <= len(word) <= args.max_word_len

    for fh in args.file:
        for line in fh:
            for word in filter(word_len, map(clean, line.lower().split())):
                words.add(word.title())
    words = sorted(words)
    passwords = [''.join(random.sample(words, args.num_words))
                 for _ in range(args.num)]
    if args.l33t:
        passwords = map(l33t, passwords)
    print('\n'.join(passwords))


if __name__ == '__main__':
    main()
