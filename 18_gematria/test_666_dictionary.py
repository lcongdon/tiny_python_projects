#!/usr/bin/env python3
"""tests for 666_dictionary.py"""

import os
import pytest
from subprocess import run


class Test666Dictionary:
    @pytest.fixture
    def program_name(self):
        """Name of program under test"""
        return "./666_dictionary.py"

    @pytest.fixture
    def dictionary_found(self):
        return "./test_666_dictionary_found.txt"

    @pytest.fixture
    def dictionary_not_found(self):
        return "./test_666_dictionary_not_found.txt"

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

        test_return = run(f'{program_name} "BBCDEFGHu"',
                          capture_output=True, text=True, shell=True)
        assert test_return.returncode == 0
        assert test_return.stdout.strip() == 'BBCDEFGHu'
        assert test_return.stderr.strip() == ""

    def test_text2(self, program_name):
        """Text"""

        text = 'test1'
        test_return = run(f'{program_name} "{text}"',
                          capture_output=True, text=True, shell=True)
        assert test_return.returncode == 1
        assert test_return.stdout.strip() == ""
        assert test_return.stderr.strip() == ""

    def test_file_found(self, program_name, dictionary_found):
        """File input"""

        expected = "BBCDEFGHu\nABCDEFGHv\nfloppy\ninsist\nosmium"
        test_return = run(f'{program_name} {dictionary_found}',
                          capture_output=True, text=True, shell=True)
        assert test_return.returncode == 0
        assert test_return.stdout.strip() == expected
        assert test_return.stderr.strip() == ""

    def test_file_not_found(self, program_name, dictionary_not_found):
        """File input"""

        test_return = run(f'{program_name} {dictionary_not_found}',
                          capture_output=True, text=True, shell=True)
        assert test_return.returncode == 1
        assert test_return.stdout.strip() == ""
        assert test_return.stderr.strip() == ""
