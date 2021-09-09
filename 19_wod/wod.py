#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-09-08
Purpose: Tiny Python Projects create workout of the day exercise
"""

import sys
import pathlib
import argparse
import csv
import random
from tabulate import tabulate


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description='Create Workout of (the) Day (WOD)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        default='inputs/exercises.csv',
                        type=argparse.FileType('rt', encoding='utf-8'),
                        help='CSV input file of exercises',
                        metavar='FILE')

    parser.add_argument('-s',
                        '--seed',
                        type=int,
                        help='Random seed',
                        metavar='seed')

    parser.add_argument('-n',
                        '--num',
                        default=4,
                        type=int,
                        help='Number of exercises',
                        metavar='exercises')

    parser.add_argument('-e',
                        '--easy',
                        default=False,
                        action='store_true',
                        help='Halve the reps')
    
    parser.add_argument('-t',
                        '--tab',
                        default=False,
                        action='store_true',
                        help='Tab delimiter in exercises')

    args = parser.parse_args()
    if(args.num <= 0):
        parser.error(f'--num "{args.num}" must be greater than 0')
    args.delimiter = '\t' if args.tab else ','
    p = pathlib.Path(args.file.name)
    if (p.suffix == '.tab'):
        args.delimiter = '\t'
    return args


def read_csv(fh, delimiter=','):
    """Read the CSV input"""
    exercises = []
    for rec in csv.DictReader(fh, delimiter=delimiter):
        if 'exercise' not in rec or 'reps' not in rec:
            continue
        name, reps = rec['exercise'], rec['reps']
        if len(reps.split('-')) != 2:
            continue
        low, high = reps.split('-')
        if not low.isnumeric() or not high.isnumeric():
            continue
        low = int(low)
        high = int(high)
        exercises.append((name, low, high))
    return exercises


def main():
    """Main program"""

    args = get_args()
    random.seed(args.seed)
    exercises = read_csv(args.file, args.delimiter)

    if not exercises:
        sys.exit(f'No usable data in --file "{args.file.name}"')

    num_exercises = len(exercises)
    if args.num > num_exercises:
        sys.exit(f'--num "{args.num}" > exercises "{num_exercises}"')

    workout = []
    for name, low, high in random.sample(exercises, k=args.num):
        reps = random.randint(low, high)
        if args.easy:
            reps = int(reps/2)
        workout.append((name, reps))
    print(tabulate(workout, headers=('Exercise', 'Reps')))


if __name__ == '__main__':
    main()
