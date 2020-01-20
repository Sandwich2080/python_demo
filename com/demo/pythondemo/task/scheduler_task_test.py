import unittest

from com.demo.pythondemo.task.scheduler_task import timer


def callback_task(input_str):
    print('callback_task:' + input_str)


class MyTestCase(unittest.TestCase):
    def test_scheduler_task(self):
        timer(5, callback_task)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
