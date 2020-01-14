from com.demo.pythondemo.http.http_requests import *


def get_config():
    r = get('https://app.modaily.cn/app_if/getConfig?appID=1')
    return r


def get_ads():
    r = get('https://app.modaily.cn:8966/adv-appif-server/getStartPage?siteID=1')
    return r


def get_ads_all():
    r = get('https://app.modaily.cn:8966/adv-appif-server//getStartPagesAll?siteID=1')
    return r
