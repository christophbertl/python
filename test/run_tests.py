import unittest
import coverage
import sys
import os

# constants
import constants


sys.path.append(constants.REPO_PATH)

# COV = coverage.Coverage(data_file=os.path.join(constants.COV_PATH, 'coverage.json'))
# COV.start()

# vehicle test
import vehicle_test
vehicle_test.run_tests()

# auto test
import auto_test
auto_test.run_tests()

# COV.stop()
# COV.save()

# COV.xml_report(outfile=os.path.join(constants.COV_PATH, 'coverage.xml'))
