from serename.scanner import Scanner
from serename.test import testutil
from unittest import TestCase
from unittest import TestSuite
from unittest import TestLoader


class TestScanner(TestCase):

    def setUp(self):
        testutil.create_tmp_dir()
        testutil.create_tmp_episodes()
        testutil.create_tmp_episodes_extensions()
        self.scanner = Scanner(testutil.TEST_DIR)
        self.maxDiff = None
        pass

    def tearDown(self):
        testutil.remove_tmp_dir()
        pass

    def test_remove_filename_extension_avi(self):
        result = Scanner.remove_filename_extension(testutil.EPISODES_EXTENSIONS["avi"])
        expected = testutil.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_mkv(self):
        result = Scanner.remove_filename_extension(testutil.EPISODES_EXTENSIONS["mkv"])
        expected = testutil.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_mp4(self):
        result = Scanner.remove_filename_extension(testutil.EPISODES_EXTENSIONS["mp4"])
        expected = testutil.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_langsrt(self):
        result = Scanner.remove_filename_extension(testutil.EPISODES_EXTENSIONS["langsrt"])
        expected = testutil.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_srt(self):
        result = Scanner.remove_filename_extension(testutil.EPISODES_EXTENSIONS["srt"])
        expected = testutil.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_langsub(self):
        result = Scanner.remove_filename_extension(testutil.EPISODES_EXTENSIONS["langsub"])
        expected = testutil.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_sub(self):
        result = Scanner.remove_filename_extension(testutil.EPISODES_EXTENSIONS["sub"])
        expected = testutil.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_get_files(self):
        files_in_dir = self.scanner.get_files()
        files_expected = testutil.get_expected_files()
        self.assertItemsEqual(files_in_dir, files_expected)

    def test_get_episodes(self):
        episodes_in_dir = self.scanner.get_episodes()
        episodes_in_dir_expected = testutil.get_expected_episodes()
        self.assertDictEqual(episodes_in_dir, episodes_in_dir_expected)


def suite():
    test_suite = TestSuite()
    test_suite.addTest(TestLoader().loadTestsFromTestCase(TestScanner))
    return test_suite