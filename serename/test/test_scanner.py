from serename.scanner import Scanner
from unittest import TestCase

from serename.test import common2

import os


class TestScanner(TestCase):

    def setUp(self):
        common2.create_tmp_dir()
        common2.create_tmp_episodes()
        common2.create_tmp_episodes_extensions()
        self.scanner = Scanner(common2.TEMP_DIR)
        self.maxDiff = None
        pass

    def tearDown(self):
        common2.remove_tmp_dir()
        pass

    def test_remove_filename_extension_avi(self):
        result = Scanner.remove_filename_extension(common2.EPISODES_EXTENSIONS["avi"])
        expected = common2.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_mkv(self):
        result = Scanner.remove_filename_extension(common2.EPISODES_EXTENSIONS["mkv"])
        expected = common2.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_mp4(self):
        result = Scanner.remove_filename_extension(common2.EPISODES_EXTENSIONS["mp4"])
        expected = common2.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_langsrt(self):
        result = Scanner.remove_filename_extension(common2.EPISODES_EXTENSIONS["langsrt"])
        expected = common2.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_srt(self):
        result = Scanner.remove_filename_extension(common2.EPISODES_EXTENSIONS["srt"])
        expected = common2.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_langsub(self):
        result = Scanner.remove_filename_extension(common2.EPISODES_EXTENSIONS["langsub"])
        expected = common2.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_remove_filename_extension_sub(self):
        result = Scanner.remove_filename_extension(common2.EPISODES_EXTENSIONS["sub"])
        expected = common2.EPISODES_EXTENSIONS_EXPECTED[0]
        self.assertEqual(result, expected, "Got: " + result + ", Expected: " + expected)

    def test_get_files(self):
        files_in_dir = self.scanner.get_files()
        files_expected = common2.get_expected_files()
        self.assertListEqual(sorted(files_in_dir), sorted(files_expected))

    def test_get_episodes(self):
        episodes_in_dir = self.scanner.get_episodes()
        episodes_in_dir_expected = common2.get_expected_episodes()
        self.assertDictEqual(episodes_in_dir, episodes_in_dir_expected)

    def test_file_hash(self):
        episode = common2.EPISODES[0].files[0]
        filename = os.path.join(common2.TEMP_DIR_EPISODES, episode["file_name"])
        result = self.scanner.get_file_hash(filename)
        expected_result = episode["content_md5"]
        self.assertEqual(result, expected_result)

    def test_filename_hash(self):
        episode = common2.EPISODES[0].files[0]
        filename = episode["file_name"]
        result = self.scanner.get_filename_hash(filename)
        expected_result = episode["filename_md5"]
        self.assertEqual(result, expected_result)
