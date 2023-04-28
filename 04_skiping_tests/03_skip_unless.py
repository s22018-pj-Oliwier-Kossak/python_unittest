import unittest
import sys


class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('aws'.upper(), 'AWS')

    @unittest.skipUnless(sys.platform.startswith('win'), 'required windows')
    def test_case_2(self):
        self.assertEqual('aws'.upper(), 'AWS')

    @unittest.skipUnless(sys.platform.startswith('linux'), 'required windows')
    def test_case_3(self):
        self.assertEqual('aws'.upper(), 'AWS')

