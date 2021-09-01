#!/usr/bin/env python3
"""tests for pig_latin.py"""

import random
from subprocess import run
import pytest


class TestPigLatin:
    @pytest.fixture
    def program_name(self):
        """Name of program under test"""
        return "./pig_latin.py"

    def test_take(self, program_name):
        """leading consonant"""

        test_string = "take"
        test_return = run(
            f"{program_name} {test_string}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 0
        assert test_return.stdout == "aketay\n"
        assert test_return.stderr == ""

    def test_chair(self, program_name):
        """consonant cluster"""

        test_string = "chair"
        test_return = run(
            f"{program_name} {test_string}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 0
        assert test_return.stdout == "airchay\n"
        assert test_return.stderr == ""

    def test_chair_uppercase(self, program_name):
        """consonant cluster in uppercase"""

        test_string = "CHAIR"
        test_return = run(
            f"{program_name} {test_string}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 0
        assert test_return.stdout == "airchay\n"
        assert test_return.stderr == ""

    def test_apple(self, program_name):
        """leading vowel"""

        test_string = "apple"
        test_return = run(
            f"{program_name} {test_string}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 0
        assert test_return.stdout == "appleyay\n"
        assert test_return.stderr == ""

    def test_no_vowels(self, program_name):
        """no vowels"""

        test_string = "fgh"
        test_return = run(
            f"{program_name} {test_string}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 1
        assert test_return.stdout == ""
        assert test_return.stderr == f'Cannot translate "{test_string}"\n'
    
    def test_invalid(self, program_name):
        """invalid string"""

        test_string = "123"
        test_return = run(
            f"{program_name} {test_string}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 1
        assert test_return.stdout == ""
        assert test_return.stderr == f'Cannot translate "{test_string}"\n'
