from unscramble import anagram
from unscramble import unscramble

def test_anagram():
    """Test anagram function"""
    assert sorted(anagram("a")) == ["a"]
    assert sorted(anagram("ad")) == ["ad", "da"]
    assert sorted(anagram("bat")) == ["bat", "tab"]
    assert sorted(anagram("atb")) == ["bat", "tab"]
    assert sorted(anagram("cat")) == ["act", "cat"]
    assert sorted(anagram("beet")) == ["beet"]
    assert sorted(anagram("ate")) == ["ate", "eat", "eta", "tae", "tea"]
    assert sorted(anagram("sidpre")) == ["spider", "spired", "spried"]

def test_unscramble():
    """Test unscramble function"""
    assert unscramble("a") == "a"
    assert unscramble("ad") == "ad"
    assert unscramble("bat") == "bat"
    assert unscramble("naet") == "neat"
    assert unscramble("adone") == "anode"
    assert unscramble("btluse") == "bustle"
    assert unscramble("balls") == "balls"