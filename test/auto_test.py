import unittest
import constants
import sys
from unittest.mock import patch
import os

sys.path.append(constants.REPO_PATH)
import Autovermietung


class AutoTest(unittest.TestCase):
    """
    Testclass for CamundaRuntime.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def test_show_menu(self):
        """
        Test for run().
        """

        # set variables
        user_input = 6

        # overwrite functions
        input_backup = __builtins__['input']
        print_backup = __builtins__['print']
        sys_backup = os.system
        __builtins__['input'] = lambda: user_input
        __builtins__['print'] = lambda _: None
        os.system = lambda _: None

        # test
        self.assertEqual(Autovermietung.show_menu(), user_input)

        # restore defaults
        __builtins__['input'] = input_backup
        __builtins__['print'] = print_backup
        os.system = lambda _: sys_backup

# run the test
def run_tests():
    """
    run test direct from python console
    """
    unittest.main(exit=False, module=AutoTest())