from serename.Episode import Episode
from unittest import TestCase
from unittest import TestSuite
from unittest import TestLoader


class TestEpisode(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


def suite():
    test_suite = TestSuite()
    test_suite.addTest(TestLoader().loadTestsFromTestCase(TestEpisode))
    return test_suite