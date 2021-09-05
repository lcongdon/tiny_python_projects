#!/usr/bin/env python3
"""tests for html.py"""

import os
import pytest
from subprocess import run


class TestHtml:
    @pytest.fixture
    def program_name(self):
        """Name of program under test"""
        return "./html.py"

    @pytest.fixture
    def fox(self):
        return "./test_html_fox.txt"

    @pytest.fixture
    def bustle(self):
        return "./test_html_the-bustle.txt"

    @pytest.fixture
    def spiders(self):
        return "./test_html_spiders.txt"

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


    def test_file_bustle(self, program_name, bustle):
        """File input"""

        expected = """
<head>
<title>
</title>
</head>
<body>
<p>
<br>
</p>
</body>
        """.strip()
        test_return = run(f'{program_name} {bustle}',
                          capture_output=True, text=True, shell=True)
        assert test_return.stdout.strip() == expected.strip()

    def test_file_fox(self, program_name, fox):
        """File input"""

        test_return = run(f'{program_name} {fox}',
                          capture_output=True, text=True, shell=True)
        assert test_return.stdout.strip() == '<p>\n<em>\n</em>\n</p>'

    def test_file_spiders(self, program_name, spiders):
        """File input"""

        expected = "<br>\n<br>"
        test_return = run(f'{program_name} {spiders}',
                          capture_output=True, text=True, shell=True)
        assert test_return.stdout.strip() == expected
