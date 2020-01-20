import time


def timer(n, your_callback_method):
    r"""
    :param n: The duration to execute the task (in seconds)
    :param your_callback_method: The task method to execute
    :return:
    """

    while True:
        current_time = time.strftime('%Y-%m-%d %X', time.localtime())
        print('self:' + current_time)
        your_callback_method(current_time)
        time.sleep(n)
