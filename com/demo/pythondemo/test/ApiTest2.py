import unittest
# import a method in another py file
from com.demo.pythondemo.api.mob_api import *


# 在ApiTest中发现，执行test case的顺序并不是按照方法顺序执行的，因此通过更改test case 方法
# 的名称来控制其执行顺序

class MyTestCase(unittest.TestCase):
    def test_1_something(self):
        self.assertEqual(True, True)

    def test_2_get_config(self):
        r = get_config()
        self.assertEqual(r.ok, True, msg='get_config failed.')

    def test_3_get_ads(self):
        r = get_ads()
        self.assertEqual(r.ok, True, msg='get_ads failed')

    def test_4_get_ads_all(self):
        r = get_ads_all()
        self.assertEqual(r.ok, True, msg='get_ads_all failed')


if __name__ == '__main__':
    unittest.main()
