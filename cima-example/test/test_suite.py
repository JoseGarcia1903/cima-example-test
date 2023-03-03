import unittest
from test.home.home_test import CimaTest
from test.forms.forms_test import CimaTest2

# Tomamos todos los test cases de las clases
testCase1 = unittest.TestLoader().loadTestsFromTestCase(CimaTest)
testCase2 = unittest.TestLoader().loadTestsFromTestCase(CimaTest2)

# Create a test suite combining all test classes
# Creamos un "test suite" combinando todos los "test cases"
smokeTest = unittest.TestSuite([testCase1, testCase2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)