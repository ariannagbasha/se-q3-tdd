#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implements a test fixture for the echo.py module

Students MUST EDIT this module, to add more tests to run
against the 'echo.py' program.
"""

__author__ = "ariannagbasha, and collabs: Sondos and Shanquel"

import sys
import importlib
import argparse
import unittest
import subprocess

# devs: change this to 'soln.echo' to run this suite against the solution
PKG_NAME = 'echo'

# suppress __pycache__ and .pyc files
sys.dont_write_bytecode = True


# Students should use this function in their tests
def run_capture(pyfile, args=()):
    """
    Runs a python program in a separate process,
    returns the output lines as a list.
    """
    cmd = ["python", pyfile]
    cmd.extend(args)
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=True
        )
        output = result.stdout.decode()
    except subprocess.CalledProcessError as err:
        output = err.stdout.decode()
    assert output, "Nothing was printed!"
    return output.splitlines()


# Students: complete this TestEcho class so that all tests run and pass.
class TestEcho(unittest.TestCase):
    """Main test fixture for 'echo' module"""
    @classmethod
    def setUpClass(cls):
        """Performs module import and suite setup at test-runtime"""
        # check for python3
        cls.assertGreaterEqual(cls, sys.version_info[0], 3)
        # This will import the module to be tested (the student's echo.py)
        cls.module = importlib.import_module(PKG_NAME)

    def test_parser(self):
        """Check if create_parser() returns a parser object"""
        result = self.module.create_parser()
        self.assertIsInstance(
            result, argparse.ArgumentParser,
            "create_parser() function is not returning a parser object")

    #
    # Students: add more parser tests here:
    # - Does it understand the --upper option?
    # - Does it understand `--lower` ? or `--title` ?
    # - If you enable one option as true, are the rest false?
    #
    def test_parser_namespace(self):
        p = self.module.create_parser()
        ns = p.parse_args(['-l', 'HELLO WORLD'])
        self.assertEqual(ns.upper and ns.title, False)
        self.assertEqual(ns.lower, True)
        self.assertEqual(ns.text.lower(), 'hello world')

    def test_echo(self):
        """Check if main() function prints anything at all"""
        module_to_test = self.module.__file__
        run_capture(module_to_test)

    def test_simple_echo(self):
        """Check if main actually echoes an input string"""
        args = ['Was soll die ganze Aufregung?']
        output = run_capture(self.module.__file__, args)
        self.assertEqual(
            output[0], args[0],
            "The program is not performing simple echo"
            )

    def test_lower_short(self):
        """Check if short option '-l' performs lowercasing"""
        args = ["-l", "HELLO WORLD"]
        output = run_capture(self.module.__file__, args)
        self.assertEqual(output[0], "hello world")

    #
    # Students: add more cmd line options tests below.
    # Replace `self.fail()` with your own code
    #

    def test_lower_long(self):
        args = ["--lower", "HELLO WORLD"]
        output = run_capture(self.module.__file__, args)
        self.assertEqual("hello world", output[0])

    def test_upper_short(self):
        args = ["-u", "Hello World"]
        output = run_capture(self.module.__file__, args)
        self.assertEqual("HELLO WORLD", output[0])

    def test_upper_long(self):
        args = ["--upper", "Hello World"]
        output = run_capture(self.module.__file__, args)
        self.assertEqual("HELLO WORLD", output[0])

    def test_title_short(self):
        args = ["-t", "hello world"]
        output = run_capture(self.module.__file__, args)
        self.assertEqual("Hello World", output[0])

    def test_title_long(self):
        args = ["--title", "hello world"]
        output = run_capture(self.module.__file__, args)
        self.assertEqual("Hello World", output[0])

    def test_multiple_options(self):
        args = ["-tul", 'heLLo!']
        output = run_capture(self.module.__file__, args)
        self.assertEqual("Hello!", output[0])

    def test_help_message(self):
        with open('USAGE') as f:
            expected = f.read().splitlines()
        output = run_capture(self.module.__file__, ['-h'])
        self.assertEqual(output, expected)

    #
    # Students: add a flake8 test here.
    # You may borrow some test code from previous assignments!
    #
    def test_flake8(self):
        """Checking for PEP8/flake8 compliance"""
        result = subprocess.run(['flake8', self.module.__file__])
        self.assertEqual(result.returncode, 0)

    #
    # Students: add an __author__ test here.
    # You may borrow some test code from previous assignments!
    #
    def test_author(self):
        """Checking for author string"""
        self.assertIsNotNone(self.module.__author__)
        self.assertNotEqual(
            self.module.__author__, "???",
            "Author string is not completed"
        )


if __name__ == '__main__':
    unittest.main()
