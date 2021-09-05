#!/usr/bin/env python3
"""tests for unscramble.py"""

import os
import pytest
from subprocess import run


class TestUnscramble:
    @pytest.fixture
    def program_name(self):
        """Name of program under test"""
        return "./unscramble.py"

    @pytest.fixture
    def fox(self):
        return "./test_unscramble_fox.txt"

    @pytest.fixture
    def bustle(self):
        return "./test_unscramble_the-bustle.txt"

    @pytest.fixture
    def spiders(self):
        return "./test_unscramble_spiders.txt"

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

    def test_text1(self, program_name):
        """Text"""

        test_return = run(f'{program_name} "tldidwe"',
                          capture_output=True, text=True, shell=True)
        assert test_return.stdout.strip() == 'twiddle'

    def test_text2(self, program_name):
        """Text"""

        text = 'The qicuk bworn fox jpmus over the lzay dog.'
        expected = 'The quick brown fox jumps over the lazy dog.'
        test_return = run(f'{program_name} "{text}"',
                          capture_output=True, text=True, shell=True)
        assert test_return.stdout.strip() == expected

    def test_file_bustle(self, program_name, bustle):
        """File input"""

        expected = """
The bustle in a house
The morning after death
Is solemnest of industries
Enacted upon earth,--

The sweeping up the heart,
And putting love away
We shall not want to use again
Until eternity.

        """.strip()
        test_return = run(f'{program_name} {bustle}',
                          capture_output=True, text=True, shell=True)
        assert test_return.stdout.strip() == expected.strip()

    def test_file_fox(self, program_name, fox):
        """File input"""

        test_return = run(f'{program_name} {fox}',
                          capture_output=True, text=True, shell=True)
        assert test_return.stdout.strip() == 'The quick brown fox jumps over the lazy dog.'

    def test_file_spiders(self, program_name, spiders):
        """File input"""

        expected = "Don't worry, spiders,\nI keep house\ncasually."
        test_return = run(f'{program_name} {spiders}',
                          capture_output=True, text=True, shell=True)
        assert test_return.stdout.strip() == expected
