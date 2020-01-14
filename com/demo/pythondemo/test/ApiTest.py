import unittest
# import a method in another py file
from com.demo.pythondemo.api.mob_api import get_config


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_get_config(self):
        r = get_config()
        self.assertEqual(r.ok, True, msg='get_config failed.')


if __name__ == '__main__':
    unittest.main()
