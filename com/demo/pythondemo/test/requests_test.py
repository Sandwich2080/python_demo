import requests

from com.demo.pythondemo.util.log_util import print_log

URL_BAIDU = 'https://www.baidu.com'


def test_get():
    r = requests.get(URL_BAIDU)
    print_log('status_code : ' + str(r.status_code))
    print_log('text : ' + r.text)
    print_log('encoding : ' + r.encoding)
    print_log('apparent_encoding : ' + r.apparent_encoding)


def test_get2():
    try:
        r = requests.get(URL_BAIDU, timeout=0.001)  # 30s timeout.
        r.raise_for_status()  # if the status code is not 200, exception will occur.
        r.encoding = r.apparent_encoding  # set the encoding format
        print_log(r.text)
        return r.text
    except:
        print_log('exception')
        return 'exception'

# test_get()
# test_get2()
