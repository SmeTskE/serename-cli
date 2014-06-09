import os
import shutil

from serename.Scanner import Scanner
from serename.test import testutil
from unittest import TestCase
from unittest import TestSuite
from unittest import TestLoader


class TestScanner(TestCase):

    def setUp(self):
        testutil.create_tmp_dir()
        testutil.create_tmp_episodes()
        testutil.create_tmp_episodes_extensions()
        self.scanner = Scanner()
        pass

    def tearDown(self):
        testutil.remove_tmp_dir()
        pass

    def test_remove_filename_extension_avi(self):
        result = self.scanner.remove_filename_extension(testutil.EPISODES_EXTENSIONS["avi"])
        expected = testutil.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_mkv(self):
        result = self.scanner.remove_filename_extension(testutil.EPISODES_EXTENSIONS["mkv"])
        expected = testutil.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_mp4(self):
        result = self.scanner.remove_filename_extension(testutil.EPISODES_EXTENSIONS["mp4"])
        expected = testutil.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_langsrt(self):
        result = self.scanner.remove_filename_extension(testutil.EPISODES_EXTENSIONS["langsrt"])
        expected = testutil.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_srt(self):
        result = self.scanner.remove_filename_extension(testutil.EPISODES_EXTENSIONS["srt"])
        expected = testutil.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_langsub(self):
        result = self.scanner.remove_filename_extension(testutil.EPISODES_EXTENSIONS["langsub"])
        expected = testutil.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_sub(self):
        result = self.scanner.remove_filename_extension(testutil.EPISODES_EXTENSIONS["sub"])
        expected = testutil.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_scan_directory(self):
        files_in_dir = self.scanner.scan_directory(testutil.TEST_DIR)
        files_expected = testutil.get_expected_files()
        self.assertItemsEqual(files_in_dir, files_expected)
        pass


def suite():
    test_suite = TestSuite()
    test_suite.addTest(TestLoader().loadTestsFromTestCase(TestScanner))
    return test_suite