#!/usr/bin/env python3
"""tests for consonant generator"""

import random
from subprocess import run
import pytest
from pathlib import Path


class TestConsonant:
    @pytest.fixture
    def program_name(self):
        """Name of program under test"""
        # return "consonant_list.py"
        return "./consonant_list.py"

    @pytest.fixture
    def help_parameter(self):
        """Randomly either -h or --help"""
        return random.choice(('-h', '--help'))

    @pytest.fixture
    def bad_parameter(self):
        """Bad parameter"""
        return '--bad'

    def test_exists(self, program_name):
        """exists"""
        assert Path(program_name).exists()

    def test_usage(self, program_name, help_parameter):
        """usage"""
        test_return = run(
            f"{program_name} {help_parameter}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 0
        assert test_return.stdout.lower().startswith('usage')
        assert test_return.stderr == ""

    def test_bad(self, program_name, bad_parameter):
        """bad parameter"""
        test_return = run(
            f"{program_name} {bad_parameter}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 2
        assert test_return.stdout == ""
        assert test_return.stderr.lower().startswith('usage')

    def test_chat(self, program_name):
        """test chat"""

        test_return = run(
            f"{program_name} 'chat'",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 0
        assert test_return.stdout == "ch\nt"
        assert test_return.stderr == ""

    def test_chat_file(self, program_name):
        """test chat in file"""

        test_file = "consonant_test_chat.txt"
        test_return = run(
            f"{program_name} {test_file}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 0
        assert test_return.stdout == "ch\nt"
        assert test_return.stderr == ""

    def test_basic_file_stdout(self, program_name):
        """test basic phrases in file"""

        test_file = "consonant_test_basic.txt"
        test_return = run(
            f"{program_name} {test_file}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 0
        assert test_return.stdout.startswith('b')
        assert test_return.stdout.endswith('z')
        assert test_return.stderr == ""

    def test_basic_file(self, program_name, current_directory):
        """test basic phrases in file"""

        test_file = "consonant_test_basic.txt"
        output_file = "consonants.txt"
        test_return = run(
            f"{program_name} {test_file} {output_file}",
            capture_output=True,
            text=True,
            shell=True,
        )
        assert test_return.returncode == 0
        assert test_return.stdout == ""
        assert test_return.stderr == ""

        f = (current_directory / output_file).open()
        test_output = f.read().split()
        f.close()
        assert len(test_output) == 57
        assert test_output[0] == "b"
        assert test_output[-1] == "z"

