from serename.scanner import Scanner
from unittest import TestCase

from serename.test import common


class TestScanner(TestCase):

    def setUp(self):
        common.create_tmp_dir()
        common.create_tmp_episodes()
        common.create_tmp_episodes_extensions()
        self.scanner = Scanner(common.TEMP_DIR)
        self.maxDiff = None
        pass

    def tearDown(self):
        common.remove_tmp_dir()
        pass

    def test_remove_filename_extension_avi(self):
        result = Scanner.remove_filename_extension(common.EPISODES_EXTENSIONS["avi"])
        expected = common.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_mkv(self):
        result = Scanner.remove_filename_extension(common.EPISODES_EXTENSIONS["mkv"])
        expected = common.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_mp4(self):
        result = Scanner.remove_filename_extension(common.EPISODES_EXTENSIONS["mp4"])
        expected = common.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_langsrt(self):
        result = Scanner.remove_filename_extension(common.EPISODES_EXTENSIONS["langsrt"])
        expected = common.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_srt(self):
        result = Scanner.remove_filename_extension(common.EPISODES_EXTENSIONS["srt"])
        expected = common.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_langsub(self):
        result = Scanner.remove_filename_extension(common.EPISODES_EXTENSIONS["langsub"])
        expected = common.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_sub(self):
        result = Scanner.remove_filename_extension(common.EPISODES_EXTENSIONS["sub"])
        expected = common.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_get_files(self):
        files_in_dir = self.scanner.get_files()
        files_expected = common.get_expected_files()
        self.assertListEqual(sorted(files_in_dir), sorted(files_expected))

    def test_get_episodes(self):
        episodes_in_dir = self.scanner.get_episodes()
        episodes_in_dir_expected = common.get_expected_episodes()
        self.assertDictEqual(episodes_in_dir, episodes_in_dir_expected)

    def test_file_hash(self):
        self.assertTrue(False)
        pass

    def test_filename_hash(self):
        self.assertTrue(False)
        pass
