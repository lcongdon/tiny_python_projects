"""Test functions for encoder.py"""

from encoder import clean
from encoder import encoder
from encoder import word2num

def test_clean():
    """Test clean function"""
    assert clean('a') == 'a'
    assert clean('boat') == 'boat'
    assert clean("don't") == 'dont'
    assert clean('a<or>b') == 'aorb'

def test_encoder():
    """Test encoder function"""
    assert encoder("a") == [129]
    assert encoder("abc") == [129, 130, 131]
    assert encoder("ab'c") == [129, 130, 125, 131]
    assert encoder("4a-b'c,") == [244, 129, 96, 130, 125, 131, 107]

def test_word2num():
    assert word2num("a") == "129"
    assert word2num("abc") == "390"
    assert word2num("ab'c") == "390"
    assert word2num("4a-b'c,") == "634"