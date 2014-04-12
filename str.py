#!/usr/bin/env python3
import sys
import unittest
from unittest import TestCase

def remove_prefix(theString, prefix):
    if theString.startswith(prefix):
        return theString[len(prefix):]
    return theString

class TestStrFunctions(TestCase):
    # Called before each test
    def setUp(self):
        pass

    #called after each test
    def tearDown(self):
        pass

    def test_remove_prefix(self):
        self.assertEqual(remove_prefix("helloworld", "hello"), "world")
        self.assertEqual(remove_prefix("helloworld", ""), "helloworld")
        self.assertEqual(remove_prefix("world", "hello"), "world")
        self.assertEqual(remove_prefix("", "hello"), "")

#Test module functionality from the command line
if __name__ == '__main__':
    unittest.main()