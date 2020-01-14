import requests


def print_log(str_content):
    r"""A custom log print method.

    :param str_content: The content to print to console
    """
    # print(str_content)


def get(request_url, params=''):
    r""" http get test

    :return:
    """

    # request_url = 'https://api.github.com/repos/psf/requests'
    print_log('request_url:' + request_url + '\n')
    r = requests.get(request_url, params)

    # print headers
    headers = r.headers
    for key in headers:
        print_log(key + ':' + headers[key])
    print_log('\n')

    content_type = ''
    if 'Content-Type' in headers.keys():
        content_type = headers['Content-Type']

    if content_type.find('text/html') != -1:
        print_log(r.text)
    if content_type.find('application/json') != -1:
        print_log(r.json())
    else:
        print_log(r.text)

    print_log('Content-Type: ' + content_type)

    return r

    # print body content
    # json_response = r.json()
    # print_log(json_response)

    # print(headers)
    # print('Date:'+headers['Date'])
    # print('Content-Type:'+headers['Content-Type'])
    # print('Transfer-Encoding:'+headers['Transfer-Encoding'])


# Http test
# get('https://api.github.com/repos/psf/requests', params='')
# get('https://www.baidu.com', params='')
# get('https://v.douyin.com/qmhAK6', params='')
