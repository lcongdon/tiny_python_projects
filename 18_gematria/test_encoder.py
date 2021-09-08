#!/usr/bin/env python3
"""tests for encoder.py"""

import os
import re
from subprocess import getstatusoutput, getoutput

prg = './encoder.py'
spiders = '../inputs/spiders.txt'
fox = '../inputs/fox.txt'
sonnet = '../inputs/sonnet-29.txt'


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
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_text():
    """Text"""

    out = getoutput(f'{prg} "foo bar baz"')
    assert out.strip() == '434 412 428'


# --------------------------------------------------
def test_fox():
    """File"""

    out = getoutput(f'{prg} {fox}')
    assert out.strip() == '496 730 748 451 770 601 432 613 417'


# --------------------------------------------------
def test_spiders():
    """File"""

    out = getoutput(f'{prg} {spiders}')
    assert out.strip() == '658 790 1030\n201 563 745\n1177'


# --------------------------------------------------
def test_sonnet():
    """File"""

    out = getoutput(f'{prg} {sonnet}')
    expected = """
970 491
1075 1631

648 286 1112 602 1046 410 592 596
201 423 708 846 316 1062 750
474 1040 528 845 602 316 1197 716
474 593 614 892 410 743 316 559
1086 281 563 313 432 584 557 286 570
1205 563 421 563 421 602 1000 1347
1202 598 588 445 410 591 588 727
666 594 201 623 745 1303 734
528 286 727 1209 892 899 1298
795 201 731 299 565 410 581 316 750
627 313 432 575 292 691 284 429 1002
649 902 714 745 763 292 1007 560
501 467 757 595 1396 593 874 866
655 581 201 745 313 813 316 750 602 729
    """.strip()
    assert out.strip() == expected
