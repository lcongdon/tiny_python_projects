#!/usr/bin/env python3
"""tests for sorter.py"""

import os
import pytest
from subprocess import run


class TestSorter:
    @pytest.fixture
    def program_name(self):
        """Name of program under test"""
        return "./sorter.py"

    @pytest.fixture
    def fox(self):
        return "../inputs/fox.txt"

    @pytest.fixture
    def bustle(self):
        return "../inputs/the-bustle.txt"

    @pytest.fixture
    def spiders(self):
        return "../inputs/spiders.txt"

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

        test_return = run(f'{program_name} foobar',
                          capture_output=True, text=True, shell=True)
        assert test_return.stdout.strip() == 'faboor'

    def test_text2(self, program_name):
        """Text"""

        text = 'The quick brown fox jumps over the lazy dog.'
        expected = 'The qciuk borwn fox jmpus oevr the lazy dog.'
        test_return = run(f'{program_name} "{text}"',
                          capture_output=True, text=True, shell=True)
        assert test_return.stdout.strip() == expected

    def test_file_bustle(self, program_name, bustle):
        """File input"""

        expected = """
The blstue in a hosue
The minnorg aeftr daeth
Is seelmnost of ideinrstus
Eacentd uopn earth,--

The seeinpwg up the haert,
And pinttug love aawy
We sahll not want to use aagin
Uintl eeinrtty.
        """.strip()
        test_return = run(f'{program_name} {bustle}',
                          capture_output=True, text=True, shell=True)
        assert test_return.stdout.strip() == expected.strip()

    def test_file_fox(self, program_name, fox):
        """File input"""

        test_return = run(f'{program_name} {fox}',
                          capture_output=True, text=True, shell=True)
        assert test_return.stdout.strip() == 'The qciuk borwn fox jmpus oevr the lazy dog.'

    def test_file_spiders(self, program_name, spiders):
        """File input"""

        expected = "D'not worry, sdeiprs,\nI keep hosue\ncaallsuy."
        test_return = run(f'{program_name} {spiders}',
                          capture_output=True, text=True, shell=True)
        assert test_return.stdout.strip() == expected
