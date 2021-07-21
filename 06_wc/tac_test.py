#!/usr/bin/env python3
"""tests for cat.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput, getoutput

prg = "./tac.py"
os_prg = "tail -r"
empty = "./inputs/empty.txt"
one_line = "./inputs/one.txt"
two_lines = "./inputs/two.txt"
fox = "../inputs/fox.txt"
sonnet = "../inputs/sonnet-29.txt"


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return "".join(random.choices(string.ascii_letters + string.digits, k=k))


# --------------------------------------------------
def test_bad_file():
    """bad_file"""

    bad = random_string()
    rv, out = getstatusoutput(f"{prg} {bad}")
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_empty():
    """Test on empty"""

    rv, out = getstatusoutput(f"{prg} {empty}")
    assert rv == 0
    assert out.rstrip() == ""


# --------------------------------------------------
def test_one():
    """Test on one"""

    rv, out = getstatusoutput(f"{prg} {one_line}")
    assert rv == 0
    expected = getoutput(f"{os_prg} {one_line}")
    assert out == expected


# --------------------------------------------------
def test_two():
    """Test on two"""

    rv, out = getstatusoutput(f"{prg} {two_lines}")
    assert rv == 0
    expected = getoutput(f"{os_prg} {two_lines}")
    assert out == expected


# --------------------------------------------------
def test_fox():
    """Test on fox"""

    rv, out = getstatusoutput(f"{prg} {fox}")
    assert rv == 0
    expected = getoutput(f"{os_prg} {fox}")
    assert out == expected


# --------------------------------------------------
def test_stdin():
    """Test on stdin"""

    rv, out = getstatusoutput(f"{prg} < {fox}")
    assert rv == 0
    expected = getoutput(f"{os_prg} < {fox}")
    assert out == expected