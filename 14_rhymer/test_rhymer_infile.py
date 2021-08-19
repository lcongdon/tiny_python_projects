#!/usr/bin/env python3
"""tests for rhymer.py infile"""

import random
from subprocess import run
import pytest


class TestRhymerInfile:
    @pytest.fixture
    def program_name(self):
        """Name of program under test"""
        return "./rhymer.py"

    @pytest.fixture
    def output_parameter(self):
        """Randomly either -o or --outfile"""
        return "-o" if random.randint(0, 1) else "--outfile"

    @pytest.fixture
    def random_consonants(self):
        """Random string of consonants in mixed case"""
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        return "".join(random.sample(consonants, k=random.randint(4, 10)))

    def test_take(self, tmp_path, program_name):
        """test input file with only valid inputs"""

        test_file = "infile_test_good.txt"
        test_return = run(
            f"{program_name} {test_file}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 0
        assert test_return.stdout == ""
        assert test_return.stderr == ""

        test_output_take = ("take.txt").read_text().split()
        assert len(test_output_take) == 56
        assert test_output_take[0] == "bake"
        assert test_output_take[-1] == "zake"

        test_output_chair = ("chair.txt").read_text().split()
        assert len(test_output_chair) == 56
        assert test_output_chair[1] == "blair"
        assert test_output_chair[-2] == "yair"

        test_output_apple = ("apple.txt").read_text().split()
        assert len(test_output_apple) == 57
        assert test_output_apple[10] == "flapple"
        assert test_output_apple[-10] == "thwapple"
