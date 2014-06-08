import os
import shutil

from serename.Scanner import Scanner
from unittest import TestCase
from unittest import TestSuite
from unittest import TestLoader


class TestScanner(TestCase):

    TEST_DIR = "test_data"
    EPISODES = [
        "The.Walking.Dead.avi",
        "The.Walking.Dead.mkv",
        "The.Walking.Dead.mp4",
        "The.Walking.Dead.en.srt",
        "The.Walking.Dead.srt",
        "The.Walking.Dead.en.sub",
        "The.Walking.Dead.sub"
    ]
    EPISODES_EXPECTED = [
        "The.Walking.Dead"
    ]

    def setUp(self):
        os.mkdir(TestScanner.TEST_DIR)
        self.scanner = Scanner()
        pass

    def tearDown(self):
        shutil.rmtree(TestScanner.TEST_DIR)
        pass

    def test_remove_filename_extension_avi(self):
        result = self.scanner.remove_filename_extension(TestScanner.EPISODES[0])
        expected = TestScanner.EPISODES_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_mkv(self):
        result = self.scanner.remove_filename_extension(TestScanner.EPISODES[1])
        expected = TestScanner.EPISODES_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_mp4(self):
        result = self.scanner.remove_filename_extension(TestScanner.EPISODES[2])
        expected = TestScanner.EPISODES_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_langsrt(self):
        result = self.scanner.remove_filename_extension(TestScanner.EPISODES[3])
        expected = TestScanner.EPISODES_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_srt(self):
        result = self.scanner.remove_filename_extension(TestScanner.EPISODES[4])
        expected = TestScanner.EPISODES_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_langsub(self):
        result = self.scanner.remove_filename_extension(TestScanner.EPISODES[5])
        expected = TestScanner.EPISODES_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_sub(self):
        result = self.scanner.remove_filename_extension(TestScanner.EPISODES[6])
        expected = TestScanner.EPISODES_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_scan_directory(self):
        pass


def suite():
    test_suite = TestSuite()
    test_suite.addTest(TestLoader().loadTestsFromTestCase(TestScanner))
    return test_suite