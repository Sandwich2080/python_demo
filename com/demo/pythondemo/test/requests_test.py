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


def test_head():
    r = requests.head('http://httpbin.org/get')
    print_log(r.headers)


def test_post_key_value():
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post('http://httpbin.org/post', data=payload)
    print_log(r.text)


def test_post_str():
    r = requests.post('http://httpbin.org/post', data='Hello,world')
    print_log(r.text)


def test_post_file():
    files = {'files': open('../resources/files.md', 'rb')}
    r = requests.post('http://httpbin.org/post', files=files)
    print_log(r.text)


def test_put():
    payload = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    r = requests.put('http://httpbin.org/put', data=payload)
    print_log(r.text)


def test_patch():
    payload = {'key1': 'value1_0'}
    r = requests.patch('http://httpbin.org/patch', data=payload)
    print_log(r.text)


def test_request():
    try:
        r = requests.request('get', 'http://www.baidu.com', timeout=0.001)  # 30s timeout
        print_log(r.text)
    except:
        print_log('Exception occurs.')


# test_get()
# test_get2()
# test_head()
# test_post_key_value()
# test_post_str()
# test_post_file()
# test_put()
# test_patch()
test_request()
