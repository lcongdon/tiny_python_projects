#!/usr/bin/env python3
"""tests for rhymer.py outfile"""

import random
from subprocess import run
import pytest


class TestRhymerOutfile:
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

    def test_take(self, tmp_path, program_name, output_parameter):
        """leading consonant with output file"""

        test_string = "take"
        out_path = tmp_path / (test_string + ".txt")
        test_return = run(
            f"{program_name} {test_string} {output_parameter} {out_path}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 0
        assert test_return.stdout == ""
        assert test_return.stderr == ""
        test_output = out_path.read_text().split()
        assert len(test_output) == 21
        assert test_output[0] == "bake"
        assert test_output[-1] == "wake"

    def test_chair(self, tmp_path, program_name, output_parameter):
        """consonant cluster with output file"""

        test_string = "chair"
        out_path = tmp_path / (test_string + ".txt")
        test_return = run(
            f"{program_name} {test_string} {output_parameter} {out_path}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 0
        assert test_return.stdout == ""
        assert test_return.stderr == ""
        test_output = out_path.read_text().split()
        assert len(test_output) == 14
        assert test_output[1] == "fair"
        assert test_output[-2] == "vair"

    def test_chair_uppercase(self, tmp_path, program_name, output_parameter):
        """consonant cluster with output file in uppercase"""

        test_string = "CHAIR"
        out_path = tmp_path / (test_string + ".txt")
        test_return = run(
            f"{program_name} {test_string} {output_parameter} {out_path}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 0
        assert test_return.stdout == ""
        assert test_return.stderr == ""
        test_output = out_path.read_text().split()
        assert len(test_output) == 14
        assert test_output[1] == "fair"
        assert test_output[-2] == "vair"

    def test_apple(self, tmp_path, program_name, output_parameter):
        """leading vowel with output file"""

        test_string = "apple"
        out_path = tmp_path / (test_string + ".txt")
        test_return = run(
            f"{program_name} {test_string} {output_parameter} {out_path}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 0
        assert test_return.stdout == ""
        assert test_return.stderr == ""
        test_output = out_path.read_text().split()
        assert len(test_output) == 8
        assert test_output[5] == "scrapple"
        assert test_output[-5] == "grapple"

    def test_no_vowels(
        self, tmp_path, program_name, output_parameter, random_consonants
    ):
        """no vowels with output file"""

        test_string = random_consonants
        out_path = tmp_path / (test_string + ".txt")
        test_return = run(
            f"{program_name} {test_string} {output_parameter} {out_path}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 1
        assert test_return.stdout == ""
        assert test_return.stderr == f'Cannot rhyme "{test_string}"\n'
