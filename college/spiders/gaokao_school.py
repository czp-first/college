# -*- coding: utf-8 -*-
import scrapy
from college.items import SchoolLineItem
from scrapy.loader import ItemLoader


class GaokaoSchoolSpider(scrapy.Spider):
    name = 'gaokao_school'
    allowed_domains = ['gaokao.com']
    # start_urls = ['http://gaokao.com/']

    PROVINCE_DICT = {
        "北京": "1",
        "天津": "2",
        "辽宁": "3",
        "吉林": "4",
        "黑龙江": "5",
        "上海": "6",
        "江苏": "7",
        "浙江": "8",
        "安徽": "9",
        "福建": "10",
        "山东": "11",
        "湖北": "12",
        "湖南": "13",
        "广东": "14",
        "重庆": "15",
        "四川": "16",
        "陕西": "17",
        "甘肃": "18",
        "河北": "19",
        "山西": "20",
        "内蒙古": "21",
        "河南": "22",
        "海南": "23",
        "广西": "24",
        "贵州": "25",
        "云南": "26",
        "西藏": "27",
        "青海": "28",
        "宁夏": "29",
        "新疆": "30",
        "江西": "31"
    }

    TYPE_DICT = {
        "li": "1",
        "wen": "2"
    }

    SCHOOL_COUNT = 2646

    def start_requests(self):
        base_url = "http://college.gaokao.com/school/tinfo/{}/result/{}/{}/"
        for school in range(1001, 1301):
            for province, pro_num in self.PROVINCE_DICT.items():
                for ty, ty_num in self.TYPE_DICT.items():
                    url = base_url.format(school, pro_num, ty_num)
                    yield scrapy.Request(url=url, callback=self.parse_school_line, meta={"province": province, "type": ty})
                    # break

    def parse_school_line(self, response):
        lines = response.xpath("//tr[contains(@class, 'sz')]")
        school = response.xpath("//h2/text()").extract()[0]
        for line in lines:
            loader = ItemLoader(item=SchoolLineItem(), selector=line)
            loader.add_value("school", school)
            loader.add_value("province", response.meta["province"])
            loader.add_value("type", response.meta["type"])
            loader.add_xpath("year", ".//td[1]/text()")
            loader.add_xpath("min", ".//td[2]/text()")
            loader.add_xpath("max", ".//td[3]/text()")
            loader.add_xpath("average", ".//td[4]/a/text()")
            loader.add_xpath("count", ".//td[5]/text()")
            loader.add_xpath("batch", ".//td[6]/text()")
            yield loader.load_item()
