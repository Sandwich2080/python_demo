from com.demo.pythondemo.http.http_requests import *


def get_config():
    r = get('https://app.modaily.cn/app_if/getConfig?appID=1')
    return r
