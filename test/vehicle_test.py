import unittest
import constants
import sys
from unittest.mock import patch

sys.path.append(constants.REPO_PATH)
import vehicle


class TestVehicle(unittest.TestCase):
    """
    Testclass for Vehicle.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def test_get_number_plate(self):
        """
        Test for get_number_plate().
        """

        # set variables
        color = 'red'
        seats = 4
        price = 50
        category = 'Kleinwagen'
        fuel = 'Benzin'
        brand = 'Toyota'
        model = 'i20'
        number_plate = 'DD-AB 123'

        # create object
        v = vehicle.Vehicle(color, seats, price,category, fuel, brand, model, \
            number_plate)

        # test number plate
        self.assertEqual(v.get_number_plate(), number_plate)

# run the test
def run_tests():
    """
    run test direct from python console
    """
    unittest.main(exit=False, module=TestVehicle())