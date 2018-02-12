import unittest

from testCalculadora import CalculadoraTest

class AllTest (unittest.TestCase):

    def runTest(self):
        """ Test addition and succeed. """

        self.failUnless(1+1 == 2 , 'one plus one fails!')

        self.failIf(1+1 != 2, 'one plus one fails again!')

        self.failUnlessEqual(1+1, 2, 'more trouble with one plus one!')

def suite():
    suite = unittest.TestSuite()
    suite.addTest(AllTest())
    suite.addTest(CalculadoraTest())
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)