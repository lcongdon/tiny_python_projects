#!/usr/bin/env python3
"""tests for rhymer.py outfile"""

import os
import random
from subprocess import run
import pytest
import pathlib


class TestRhymerOutfile:

    @pytest.fixture
    def program_name(self):
        """Name of program under test"""
        return('./rhymer.py')

    @pytest.fixture
    def output_parameter(self):
        """Randomly either -o or --output"""
        # return "-o" if random.randint(0, 1) else "--output"
        return('--output')

    def test_take(self, tmp_path, program_name, output_parameter):
        """leading consonant with output file"""

        test_string = "take"
        out_path = tmp_path / (test_string + ".txt")
        test_return = run(
            [f"{program_name}", f"{test_string}", f"{output_parameter}" f"{out_path}"],
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 0
        assert test_return.stdout == ''
        assert test_return.stderr == ''
        test_output = out_path.read_text()
        assert len(test_output) == 56
        assert test_output[0] == "bake"
        assert test_output[-1] == "zake"

    # # --------------------------------------------------
    # def test_chair(tmp_path):
    #     """consonant cluster"""

    #     out = getoutput(f"{prg} chair").splitlines()
    #     assert len(out) == 56
    #     assert out[1] == "blair"
    #     assert out[-2] == "yair"

    # # --------------------------------------------------
    # def test_chair_uppercase(tmp_path):
    #     """consonant cluster"""

    #     out = getoutput(f"{prg} CHAIR").splitlines()
    #     assert len(out) == 56
    #     assert out[1] == "blair"
    #     assert out[-2] == "yair"

    # # --------------------------------------------------
    # def test_apple(tmp_path):
    #     """leading vowel"""

    #     out = getoutput(f"{prg} apple").splitlines()
    #     assert len(out) == 57
    #     assert out[10] == "flapple"
    #     assert out[-10] == "thwapple"

    # # --------------------------------------------------
    # def test_no_vowels(tmp_path):
    #     """no vowels"""

    #     consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    #     bad = "".join(random.sample(consonants, k=random.randint(4, 10)))
    #     out = getoutput(f"{prg} {bad}")
    #     assert out == f'Cannot rhyme "{bad}"'
