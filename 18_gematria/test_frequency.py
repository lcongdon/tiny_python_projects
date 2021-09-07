#!/usr/bin/env python3
"""tests for frequency.py"""

import os
import pytest
from subprocess import run


class TestFrequency:
    @pytest.fixture
    def program_name(self):
        """Name of program under test"""
        return "./frequency.py"

    @pytest.fixture
    def test_file(self):
        return "./test_frequency.txt"

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

        expected = """
Total occurences: 1
foo
Total occurences: 1
bar
Total occurences: 1
baz
    """.strip()
        test_return = run(f'{program_name} "foo bar baz"',
                          capture_output=True, text=True, shell=True)
        assert test_return.returncode == 0
        assert test_return.stdout.strip() == expected
        assert test_return.stderr.strip() == ""

    def test_text2(self, program_name):
        """Text"""

        text = 'the the the only one'
        test_return = run(f'{program_name} "{text}"',
                          capture_output=True, text=True, shell=True)
        assert test_return.returncode == 0
        assert test_return.stdout.strip() == "Total occurences: 3\nthe"
        assert test_return.stderr.strip() == ""

    def test_text3(self, program_name):
        """Text"""

        text = 'exhort fizzer glumly grisly locust locust locust motley'
        expected = 'exhort fizzer glumly grisly motley locust'.split()
        test_return = run(f'{program_name} "{text}"',
                          capture_output=True, text=True, shell=True)
        assert test_return.returncode == 0
        assert test_return.stdout.strip()[:19] == "Total occurences: 8"
        assert sorted(test_return.stdout[20:].split()) == sorted(expected)
        assert test_return.stderr.strip() == ""

    def test_file_input(self, program_name, test_file):
        """File input"""

        expected = 'exhort fizzer glumly grisly locust motley'.split()
        test_return = run(f'{program_name} {test_file}',
                          capture_output=True, text=True, shell=True)
        assert test_return.returncode == 0
        assert test_return.stdout.strip()[:19] == "Total occurences: 8"
        assert sorted(test_return.stdout[20:62].split()) == sorted(expected)
        assert test_return.stdout.strip()[62:] == "Total occurences: 8\nthe"
        assert test_return.stderr == ""
