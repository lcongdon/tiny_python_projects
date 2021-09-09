#!/usr/bin/env python3
"""tests for wod.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './wod.py'
tab = 'inputs/bad-delimiter.tab'
input1 = 'inputs/exercises.csv'
input2 = 'inputs/silly-exercises.csv'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_bad_num():
    """Dies on bad --num"""

    bad = random.choice(range(-10, 0))
    rv, out = getstatusoutput(f'{prg} -n {bad}')
    assert rv != 0
    assert re.search(f'--num "{bad}" must be greater than 0', out)


# --------------------------------------------------
def test_bad_file():
    """Dies on bad file"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} -f {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_tab_delimiter():
    """tab delimiter"""

    expected = """
Exercise      Reps
----------  ------
Pushups         56
Situps          88
Crunches        27
Burpees         35
"""
    tab_flag = '-t' if random.choice([0, 1]) else '--tab'
    rv, out = getstatusoutput(f'{prg} -f {tab} -s 1 {tab_flag}')
    assert rv == 0
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_tab_delimiter_extension():
    """tab delimiter based on file extension"""

    expected = """
Exercise      Reps
----------  ------
Pushups         56
Situps          88
Crunches        27
Burpees         35
"""
    rv, out = getstatusoutput(f'{prg} -f {tab} -s 1')
    assert rv == 0
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_seed1():
    """Runs OK"""

    expected = """
Exercise      Reps
----------  ------
Pushups         56
Situps          88
Crunches        27
Burpees         35
"""

    seed_flag = '-s' if random.choice([0, 1]) else '--seed'
    rv, out = getstatusoutput(f'{prg} {seed_flag} 1')
    assert rv == 0
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_seed1_easy():
    """Runs OK"""

    expected = """
Exercise      Reps
----------  ------
Pushups         28
Situps          44
Crunches        13
Burpees         17
"""

    seed_flag = '-s' if random.choice([0, 1]) else '--seed'
    easy_flag = '-e' if random.choice([0, 1]) else '--easy'
    rv, out = getstatusoutput(f'{prg} {easy_flag} {seed_flag} 1')
    assert rv == 0
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_seed2_num8():
    """Runs OK"""

    expected = """
Exercise              Reps
------------------  ------
Burpees                 39
Situps                  42
Crunches                29
Pushups                 68
Plank                   35
Hand-stand pushups      18
Pullups                 30
Lunges                  32
"""

    seed_flag = '-s' if random.choice([0, 1]) else '--seed'
    num_flag = '-n' if random.choice([0, 1]) else '--num'
    cmd = f'{prg} {num_flag} 8 {seed_flag} 2 -f {input1}'
    rv, out = getstatusoutput(cmd)
    assert rv == 0
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_seed4_num3_input2():
    """Runs OK"""

    expected = """
Exercise             Reps
-----------------  ------
Hanging Chads          86
Red Barchettas         50
Squatting Chinups      35
"""

    seed_flag = '-s' if random.choice([0, 1]) else '--seed'
    num_flag = '-n' if random.choice([0, 1]) else '--num'
    rv, out = getstatusoutput(f'{prg} {num_flag} 3 {seed_flag} 4 -f {input2}')
    assert rv == 0
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_bad_tablefmt():
    """Dies on bad --tablefmt"""

    bad = 'badformat'
    rv, out = getstatusoutput(f'{prg} -tf {bad}')
    assert rv != 0
    assert re.search(f"argument -tf/--tablefmt: invalid choice: '{bad}'", out)

# --------------------------------------------------


def test_seed2_num8_tablefmt_plain():
    """Runs OK, plain formatting"""

    expected = """
Exercise              Reps
Burpees                 39
Situps                  42
Crunches                29
Pushups                 68
Plank                   35
Hand-stand pushups      18
Pullups                 30
Lunges                  32
"""

    seed_flag = '-s' if random.choice([0, 1]) else '--seed'
    num_flag = '-n' if random.choice([0, 1]) else '--num'
    format_flag = '-tf' if random.choice([0, 1]) else '--tablefmt'
    cmd = f'{prg} {num_flag} 8 {seed_flag} 2 -f {input1} {format_flag} plain'
    rv, out = getstatusoutput(cmd)
    assert rv == 0
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_seed4_num3_input2_tablefmt_github():
    """Runs OK, github formatting"""

    expected = """
+-------------------+--------+
| Exercise          |   Reps |
+===================+========+
| Hanging Chads     |     86 |
+-------------------+--------+
| Red Barchettas    |     50 |
+-------------------+--------+
| Squatting Chinups |     35 |
+-------------------+--------+
"""

    seed_flag = '-s' if random.choice([0, 1]) else '--seed'
    num_flag = '-n' if random.choice([0, 1]) else '--num'
    format_flag = '-tf' if random.choice([0, 1]) else '--tablefmt'
    rv, out = getstatusoutput(
        f'{prg} {num_flag} 3 {seed_flag} 4 -f {input2} {format_flag} grid')
    assert rv == 0
    assert out.strip() == expected.strip()


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
