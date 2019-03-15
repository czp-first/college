# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from college.items import MajorLineItem


class GaokaoSpider(scrapy.Spider):
    name = 'gaokao'
    allowed_domains = ['college.gaokao.com']
    # start_urls = ['http://college.gaokao.com/']

    def start_requests(self):
        # 2017, 6184
        # 2016, 8249
        # 2015, 9984
        # 2014, 15950
        # 2013, 9494
        # 2012, 10277
        # 2011, 12426
        # 2010, 9396
        # 2009, 10956
        # 2008, 5838
        # 2007, 5485
        years_pages = {
            # "2017": "6184",
            # "2016": "8249",
            # "2015": "9984",
            # "2014": "15950",
            # "2013": "9494",
            # "2012": "10277",
            # "2011": "12426",
            "2010": "9396",
            "2009": "10956",
            "2008": "5838",
            "2007": "5485"
        }
        base_url = "http://college.gaokao.com/spepoint/y{}/p{}/"
        for year_page in years_pages.items():
            year = year_page[0]
            page = int(year_page[1])
            for page in range(1, page+1):
                url = base_url.format(year, page)
                yield scrapy.Request(url=url)
                # break

    def parse(self, response):
        doc = etree.HTML(response.text)
        trs = doc.xpath("//tr[contains(@class, 'sz')]")
        for tr in trs:
            item = MajorLineItem()
            item["major_name"] = tr.xpath(".//td[1]/a/text()")[0]
            item["school_name"] = tr.xpath(".//td[2]/a/text()")[0]
            item["average"] = tr.xpath(".//td[3]/a/text()")[0]
            item["max"] = tr.xpath(".//td[4]/text()")[0]
            item["province"] = tr.xpath(".//td[5]/text()")[0]
            item["type"] = tr.xpath(".//td[6]/text()")[0]
            item["year"] = tr.xpath(".//td[7]/text()")[0]
            item["batch"] = tr.xpath(".//td[8]/text()")[0]
            yield item

