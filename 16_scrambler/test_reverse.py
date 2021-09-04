#!/usr/bin/env python3
"""tests for reverse.py"""

import os
import pytest
from subprocess import run


class TestReverse:
    @pytest.fixture
    def program_name(self):
        """Name of program under test"""
        return "./reverse.py"

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
        assert test_return.stdout.strip() == 'raboof'

    def test_text2(self, program_name):
        """Text"""

        text = 'The quick brown fox jumps over the lazy dog.'
        expected = 'ehT kciuq nworb xof spmuj revo eht yzal god.'
        test_return = run(f'{program_name} "{text}"',
                          capture_output=True, text=True, shell=True)
        assert test_return.stdout.strip() == expected

    def test_file_bustle(self, program_name, bustle):
        """File input"""

        expected = """
ehT eltsub ni a esuoh
ehT gninrom retfa htaed
sI tsenmelos fo seirtsudni
detcanE nopu htrae,--

ehT gnipeews pu eht traeh,
dnA gnittup evol yawa
eW llahs ton tnaw ot esu niaga
litnU ytinrete.
        """.strip()
        test_return = run(f'{program_name} {bustle}',
                          capture_output=True, text=True, shell=True)
        assert test_return.stdout.strip() == expected.strip()

    def test_file_fox(self, program_name, fox):
        """File input"""

        test_return = run(f'{program_name} {fox}',
                          capture_output=True, text=True, shell=True)
        assert test_return.stdout.strip() == 'ehT kciuq nworb xof spmuj revo eht yzal god.'

    def test_file_spiders(self, program_name, spiders):
        """File input"""

        expected = "t'noD yrrow, sredips,\nI peek esuoh\nyllausac."
        test_return = run(f'{program_name} {spiders}',
                          capture_output=True, text=True, shell=True)
        assert test_return.stdout.strip() == expected
