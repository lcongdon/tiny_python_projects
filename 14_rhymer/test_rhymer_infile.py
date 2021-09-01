#!/usr/bin/env python3
"""tests for rhymer.py infile"""

import random
from subprocess import run
import pytest
from pathlib import Path


class TestRhymerInfile:
    @pytest.fixture
    def program_name(self):
        """Name of program under test"""
        return "./rhymer.py"

    @pytest.fixture
    def output_directory(self):
        """Randomly either -d or --outdir"""
        return "-d" if random.randint(0, 1) else "--outdir"

    def test_good(self, tmp_path, program_name, output_directory):
        """test input file with only valid inputs"""

        test_file = "infile_test_good.txt"
        test_directory = str(tmp_path)
        test_return = run(
            f"{program_name} {output_directory} {test_directory} {test_file}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 0
        assert test_return.stdout == ""
        assert test_return.stderr == ""

        p = Path(tmp_path)
        q = p / "take.txt"
        f = q.open()
        test_output_take = f.read().split()
        f.close()
        assert len(test_output_take) == 21
        assert test_output_take[0] == "bake"
        assert test_output_take[-1] == "wake"

        q = p / "chair.txt"
        f = q.open()
        test_output_chair = f.read().split()
        f.close()
        assert len(test_output_chair) == 14
        assert test_output_chair[1] == "fair"
        assert test_output_chair[-2] == "vair"

        q = p / "apple.txt"
        f = q.open()
        test_output_apple = f.read().split()
        f.close()
        assert len(test_output_apple) == 8
        assert test_output_apple[5] == "scrapple"
        assert test_output_apple[-5] == "grapple"

    def test_bad(self, program_name):
        """test input file with only invalid inputs"""

        test_file = "infile_test_bad.txt"
        test_return = run(
            f"{program_name} {test_file}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 1
        assert test_return.stdout == ""
        assert test_return.stderr == 'Cannot rhyme "fgh"\nCannot rhyme "123"\n'

    def test_mixed(self, tmp_path, program_name, output_directory):
        """test input file with mixed validity inputs"""

        test_file = "infile_test_mixed.txt"
        test_directory = str(tmp_path)
        test_return = run(
            f"{program_name} {output_directory} {test_directory} {test_file}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 1
        assert test_return.stdout == ""
        assert test_return.stderr == 'Cannot rhyme "123"\nCannot rhyme "fgh"\n'

        p = Path(tmp_path)
        q = p / "take.txt"
        f = q.open()
        test_output_take = f.read().split()
        f.close()
        assert len(test_output_take) == 21
        assert test_output_take[0] == "bake"
        assert test_output_take[-1] == "wake"

        q = p / "chair.txt"
        f = q.open()
        test_output_chair = f.read().split()
        f.close()
        assert len(test_output_chair) == 14
        assert test_output_chair[1] == "fair"
        assert test_output_chair[-2] == "vair"

        q = p / "apple.txt"
        f = q.open()
        test_output_apple = f.read().split()
        f.close()
        assert len(test_output_apple) == 8
        assert test_output_apple[5] == "scrapple"
        assert test_output_apple[-5] == "grapple"

        q = p / "chat.txt"
        f = q.open()
        test_output_chat = f.read().split()
        f.close()
        assert len(test_output_chat) == 45
        assert test_output_chat[2] == "blat"
        assert test_output_chat[-3] == "what"
