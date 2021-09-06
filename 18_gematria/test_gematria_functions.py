"""Test functions for gematria.py"""

from gematria import clean
from gematria import word2num

def test_clean():
    """Test clean function"""
    assert clean('a') == 'a'
    assert clean('boat') == 'boat'
    assert clean("don't") == 'dont'
    assert clean('a<or>b') == 'aorb'

def test_word2num():
    assert word2num("a") == "97"
    assert word2num("abc") == "294"
    assert word2num("ab'c") == "294"
    assert word2num("4a-b'c,") == "346"