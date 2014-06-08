from unittest import TestCase
from unittest import TestSuite
from unittest import TestLoader
from serename.Scanner import Scanner


class TestScanner(TestCase):

    def setUp(self):
        self.scanner = Scanner()
        pass

    def test_remove_filename_extensions(self):
        self.assertTrue(self.scanner.remove_filename_extensions(), "Yay!")

    def tearDown(self):
        pass


def suite():
    test_suite = TestSuite()
    test_suite.addTest(TestLoader().loadTestsFromTestCase(TestScanner))
    return test_suite