from unittest import TestCase
from serename.episode import Episode
from serename.test import common


class TestEpisode(TestCase):
    def setUp(self):
        self.episode = Episode()
        pass

    def tearDown(self):
        pass

    def test_add_file(self):
        self.episode.add_file("The.Walking.Dead.mp4")
        expected_episode = Episode({"files": ["The.Walking.Dead.mp4"]})
        self.assertEqual(self.episode, expected_episode)
        pass

    def test_add_files(self):
        self.assertTrue(False)
        pass

    def test_get_name(self):
        self.assertTrue(False)
        pass

    def test_get_files(self):
        self.assertTrue(False)
        pass

    def test_set_files(self):
        self.assertTrue(False)
        pass

    def test_set_name(self):
        self.assertTrue(False)
        pass
