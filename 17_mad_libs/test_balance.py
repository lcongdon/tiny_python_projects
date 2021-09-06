#!/usr/bin/env python3
"""tests for balance.py"""

import os
import pytest
from subprocess import run


class TestBalance:
    @pytest.fixture
    def program_name(self):
        """Name of program under test"""
        return "./balance.py"

    @pytest.fixture
    def fox(self):
        return "./test_balance_fox.txt"

    @pytest.fixture
    def bustle(self):
        return "./test_balance_the-bustle.txt"

    @pytest.fixture
    def spiders(self):
        return "./test_balance_spiders.txt"

    @pytest.fixture
    def romeo_juliet(self):
        return "./test_balance_romeo_juliet.txt"

    def test_exists(self, program_name):
        """exists"""
        assert os.path.isfile(program_name)

    def test_usage(self, program_name):
        """usage"""

        test_return = run(f'{program_name}',
                          capture_output=True, text=True, shell=True)
        assert test_return.returncode == 2
        assert test_return.stdout == ""
        assert test_return.stderr.lower().startswith("usage")

        for flag in ['-h', '--help']:
            test_return = run(f'{program_name} {flag}',
                              capture_output=True, text=True, shell=True)
        assert test_return.returncode == 0
        assert test_return.stdout.lower().startswith("usage")
        assert test_return.stderr == ""

    def test_file_fox(self, program_name, fox):
        """File input, unbalanced at end"""

        test_return = run(f'{program_name} {fox}',
                          capture_output=True, text=True, shell=True)
        assert test_return.returncode == 1
        assert test_return.stdout == ""
        assert test_return.stderr.strip() == 'Unbalanced "(" at end of file.'

    def test_file_bustle(self, program_name, bustle):
        """File input, balanced"""

        expected = ''.strip()
        test_return = run(f'{program_name} {bustle}',
                          capture_output=True, text=True, shell=True)
        assert test_return.returncode == 0
        assert test_return.stdout == ""
        assert test_return.stderr.strip() == expected.strip()

    def test_file_spiders(self, program_name, spiders):
        """File input, unbalanced in text"""

        expected = 'Unbalanced "}" at 55, stopping.'
        test_return = run(f'{program_name} {spiders}',
                          capture_output=True, text=True, shell=True)
        assert test_return.returncode == 1
        assert test_return.stdout == ""
        assert test_return.stderr.strip() == expected

    def test_file_romeo_juliet(self, program_name, romeo_juliet):
        """File input, unmatched in text"""

        expected = 'Unmatched "}" at 641, stopping.'
        test_return = run(f'{program_name} {romeo_juliet}',
                          capture_output=True, text=True, shell=True)
        assert test_return.returncode == 1
        assert test_return.stdout == ""
        assert test_return.stderr.strip() == expected
