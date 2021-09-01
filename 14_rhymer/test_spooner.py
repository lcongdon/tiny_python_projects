#!/usr/bin/env python3
"""tests for spooner.py"""

import os
from subprocess import run
import pytest


class TestSpooner:
    @pytest.fixture
    def program_name(self):
        """Name of program under test"""
        return "./spooner.py"

    def test_exists(self, program_name):
        """exists"""
        assert os.path.isfile(program_name)

    def test_usage(self, program_name):
        """usage"""

        test_return = run(
            f'{program_name}',
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 2
        assert test_return.stdout == ""
        assert test_return.stderr.lower().startswith('usage')

        for flag in ['-h', '--help']:
            test_return = run(
                f'{program_name} {flag}',
                capture_output=True,
                text=True,
                shell=True,
            )
        assert test_return.returncode == 0
        assert test_return.stdout.lower().startswith('usage')
        assert test_return.stderr == ""

    def test_take(self, program_name):
        """leading consonants"""

        test_string = "take two"
        test_return = run(
            f"{program_name} {test_string}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 0
        assert test_return.stdout == "twake to\n"
        assert test_return.stderr == ""

    def test_chair(self, program_name):
        """consonant cluster"""

        test_string = "chair seat"
        test_return = run(
            f"{program_name} {test_string}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 0
        assert test_return.stdout == "sair cheat\n"
        assert test_return.stderr == ""

    def test_chair_uppercase(self, program_name):
        """consonant cluster in uppercase"""

        test_string = "CHAIR SEAT"
        test_return = run(
            f"{program_name} {test_string}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 0
        assert test_return.stdout == "sair cheat\n"
        assert test_return.stderr == ""

    def test_apple(self, program_name):
        """leading vowel"""

        test_string = "apple pie"
        test_return = run(
            f"{program_name} {test_string}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 1
        assert test_return.stdout == ""
        assert test_return.stderr == f'Cannot spoonerize "{test_string}"\n'

    def test_one_parameter(self, program_name):
        """one string"""

        test_string = "fgh"
        test_return = run(
            f"{program_name} {test_string}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 2
        assert test_return.stdout == ""
        assert test_return.stderr.lower().startswith('usage')

    def test_invalid(self, program_name):
        """invalid string(s)"""

        test_string = "123 456" 
        test_return = run(
            f"{program_name} {test_string}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 1
        assert test_return.stdout == ""
        assert test_return.stderr == f'Cannot spoonerize "{test_string}"\n'
