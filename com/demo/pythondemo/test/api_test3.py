import unittest
# import a method in another py file
from com.demo.pythondemo.api.mob_api import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_get_config(self):
        r = get_config()
        self.assertEqual(r.ok, True, msg='get_config failed.')

    def test_get_ads(self):
        r = get_ads()
        self.assertEqual(r.ok, True, msg='get_ads failed')

    def test_get_ads_all(self):
        r = get_ads_all()
        self.assertEqual(r.ok, True, msg='get_ads_all failed')

    # if __name__ == '__main__':
    #    unittest.main()


suite = unittest.TestSuite()
test_case1 = MyTestCase('test_something')
suite.addTest(test_case1)
test_case2 = MyTestCase('test_get_config')
suite.addTest(test_case2)
unittest.TextTestRunner(verbosity=3).run(suite)
