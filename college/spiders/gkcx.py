# -*- coding: utf-8 -*-
import time

import scrapy


class GkcxSpider(scrapy.Spider):
    name = 'gkcx'
    allowed_domains = ['gkcx.eol.cn']
    # start_urls = ['http://gkcx.eol.cn/']

    def start_requests(self):
        for page in range(1, 1000):
            base_url = "https://data-gkcx.eol.cn/soudaxue/querySpecialtyScore.html?messtype=jsonp&callback=jQuery183008793827256737519_1552288275357&provinceforschool=&schooltype=&page={}&size=10&keyWord=&schoolproperty=&schoolflag=&province=&fstype=&zhaoshengpici=&fsyear=&zytype=&_={}"

            # jQuery18308445231731283713_1552288333505
            # 1552288333659
            # 1552289475.908781

            referer = "https://gkcx.eol.cn/soudaxue/querySpecialtyScore.html?&page=".format(page)
            headers = {
                'Accept': '*/*',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Host": "data-gkcx.eol.cn",
                "Referer": referer,
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36"

            }

            url = base_url.format(page, int(time.time()*1000))
            yield scrapy.Request(url=url, callback=self.parse, headers=headers)

    def parse(self, response):
        # print(response.text)
        pass
