#-*-codinf:utf-8-*-
from urllib import request
import time
import http.cookiejar
class DownHtml(object):
    def __init__(self):
        pass

    def download(self,url):
        time.sleep(3)
        # 如果链接为空 或者访问异常返回空
        if url is None:
            return None
        # 设置代理IP，有多个时，以字典的形式存放
        # 设置代理IP
        proxy = {"http": "192.168.69.118",
                 "http": "192.168.69.117",
                 "http": "192.168.69.115",
                 "http": "192.168.69.114",
                 "http": "192.168.69.113",
                 "http": "192.168.69.112",
                 "http": "192.168.69.111",
                 "http": "192.168.69.110",
                 "http": "192.168.69.109",
                 "http": "192.168.69.108",
                 "http": "192.168.69.107",
                 "http": "192.168.69.106",
                 "http": "192.168.69.105",
                 "http": "192.168.69.104",
                 "http": "192.168.69.103",
                 "http": "192.168.69.102",
                 "http": "192.168.69.101",
                 "http": "192.168.69.100",
                 "http": "192.168.69.99",
                 "http": "192.168.69.98",
                 "http": "192.168.69.97",
                 "http": "192.168.69.96",
                 "http": "192.168.69.95",
                 "http": "192.168.69.94",
                 "http": "192.168.69.93",
                 "http": "192.168.69.92",
                 "http": "192.168.69.91",
                 "http": "192.168.69.90",
                 "http": "192.168.69.89",
                 "http": "192.168.69.88",
                 "http": "192.168.69.87",
                 "http": "192.168.69.86",
                 "http": "192.168.69.85",
                 "http": "192.168.69.84",
                 "http": "192.168.69.83",
                 "http": "192.168.69.82",
                 "http": "192.168.69.81",
                 "http": "192.168.69.80",
                 "http": "192.168.69.79",
                 "http": "192.168.69.78",
                 "http": "192.168.69.77",
                 "http": "192.168.69.76",
                 "http": "192.168.69.75",
                 "http": "192.168.69.74",
                 "http": "192.168.69.73",
                 "http": "192.168.69.72",
                 "http": "192.168.69.71",
                 "http": "192.168.69.69",
                 "http": "192.168.69.68",
                 "http": "192.168.69.67",
                 "http": "192.168.69.66",
                 "http": "192.168.69.65",
                 "http": "192.168.69.64",
                 "http": "192.168.69.63",
                 "http": "192.168.69.62",
                 "http": "192.168.69.61",
                 "http": "192.168.69.60",
                 "http": "192.168.69.52",
                 "http": "192.168.69.50",
                 "http": "192.168.69.49",
                 "http": "192.168.69.48",
                 "http": "192.168.69.47",
                 "http": "192.168.69.46",
                 "http": "192.168.69.45",
                 "http": "192.168.69.44",
                 "http": "192.168.69.43",
                 "http": "192.168.69.42",
                 "http": "192.168.69.41",
                 "http": "192.168.69.40",
                 "http": "192.168.69.39",
                 "http": "192.168.69.38",
                 "http": "192.168.69.37",
                 "http": "192.168.69.36",
                 "http": "192.168.69.35",
                 "http": "192.168.69.34",
                 "http": "192.168.69.33",
                 "http": "192.168.69.32",
                 "http": "192.168.69.31",
                 "http": "192.168.69.30",
                 "http": "192.168.69.29",
                 "http": "192.168.69.28",
                 "http": "192.168.69.27",
                 "http": "192.168.69.26",
                 "http": "192.168.69.25",
                 "http": "192.168.69.24",
                 "http": "192.168.69.23",
                 "http": "192.168.69.22",
                 "http": "192.168.69.21",
                 "http": "192.168.69.19",
                 "http": "192.168.69.18",
                 "http": "192.168.69.17",
                 "http": "192.168.69.16",
                 "http": "192.168.69.15",
                 "http": "192.168.69.14",
                 "http": "192.168.69.13",
                 "http": "192.168.69.12",
                 "http": "192.168.69.11",
                 "http": "192.168.69.10",
                 }
        proxy_support = request.ProxyHandler(proxy)
        opener = request.build_opener(proxy_support)
        request.install_opener(opener)

        #设置一个cookie处理器，负责从服务器下载cookie到本地，并在发送请求时带上本地的cookie
        cj = http.cookiejar.LWPCookieJar()
        cookie_support  = request.HTTPCookieProcessor(cj)
        opener_cookie =   request.build_opener(cookie_support,request.HTTPHandler)
        request.install_opener(opener_cookie)

        #加进header，伪装成浏览器访问
        #  req.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')      #添加header
        hdr = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        req = request.Request(url,headers=hdr)
        response = request.urlopen(req)

        if response.getcode() != 200:
           return None
        #返回网页源代码
        return response.read()
