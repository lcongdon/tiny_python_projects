"""Test functions for balance.py"""

from balance import match

def test_match():
    """Test match function"""
    assert match('(', ')')
    assert match('[', ']')
    assert match('{', '}')
    assert not match('{', ']')
    assert not match(']', ']')
    assert not match(')', '(')