import time


def timer(n, your_callback_method):
    while True:
        current_time = time.strftime('%Y-%m-%d %X', time.localtime())
        print('self:'+current_time)
        your_callback_method(current_time)
        time.sleep(n)
