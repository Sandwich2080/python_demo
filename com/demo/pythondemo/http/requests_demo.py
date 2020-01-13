import requests


def print_log(str_content):
    r"""A custom log print method.

    :param str_content: The content to print to console
    """
    print(str_content)


def http_get_test(request_url):
    r""" http get test

    :return:
    """

    # request_url = 'https://api.github.com/repos/psf/requests'
    print_log('request_url:' + request_url + '\n')
    r = requests.get(request_url)

    # print headers
    headers = r.headers
    for key in headers:
        print_log(key + ':' + headers[key])
    print_log('\n')

    content_type = headers['Content-Type']
    if content_type.find('text/html') != -1:
        print_log(r.text)
    if content_type.find('application/json') != -1:
        print_log(r.json())
    if 'application/json' in content_type:
        print_log('Response body format is json')
    else:
        print_log('Response body is not json')

    # print body content
    # json_response = r.json()
    # print_log(json_response)

    # print(headers)
    # print('Date:'+headers['Date'])
    # print('Content-Type:'+headers['Content-Type'])
    # print('Transfer-Encoding:'+headers['Transfer-Encoding'])


# Http test
http_get_test('https://api.github.com/repos/psf/requests')
http_get_test('https://www.baidu.com')
