import os
import shutil

from serename.Scanner import Scanner
from serename.test import util
from unittest import TestCase
from unittest import TestSuite
from unittest import TestLoader


class TestScanner(TestCase):

    def setUp(self):
        tmp_dir = util.TEST_DIR
        tmp_files = util.EPISODES
        os.mkdir(tmp_dir)
        for key, value in tmp_files.iteritems():
            tmp_file_path = os.path.join(tmp_dir, value[0])
            tmp_file = open(tmp_file_path, 'w+')
            tmp_file.write(value[0])
        self.scanner = Scanner()
        pass

    def tearDown(self):
        shutil.rmtree(util.TEST_DIR)
        pass

    def test_remove_filename_extension_avi(self):
        result = self.scanner.remove_filename_extension(util.EPISODES["avi"][0])
        expected = util.EPISODES_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_mkv(self):
        result = self.scanner.remove_filename_extension(util.EPISODES["mkv"][0])
        expected = util.EPISODES_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_mp4(self):
        result = self.scanner.remove_filename_extension(util.EPISODES["mp4"][0])
        expected = util.EPISODES_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_langsrt(self):
        result = self.scanner.remove_filename_extension(util.EPISODES["langsrt"][0])
        expected = util.EPISODES_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_srt(self):
        result = self.scanner.remove_filename_extension(util.EPISODES["srt"][0])
        expected = util.EPISODES_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_langsub(self):
        result = self.scanner.remove_filename_extension(util.EPISODES["langsub"][0])
        expected = util.EPISODES_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_sub(self):
        result = self.scanner.remove_filename_extension(util.EPISODES["sub"][0])
        expected = util.EPISODES_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_scan_directory(self):
        files_in_dir = self.scanner.scan_directory(util.TEST_DIR)
        files_expected = util.get_expected_files()
        self.assertItemsEqual(files_in_dir, files_expected)
        pass


def suite():
    test_suite = TestSuite()
    test_suite.addTest(TestLoader().loadTestsFromTestCase(TestScanner))
    return test_suite