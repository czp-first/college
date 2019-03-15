# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CollegeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MajorLineItem(scrapy.Item):
    major_name = scrapy.Field()
    school_name = scrapy.Field()
    province = scrapy.Field()
    type = scrapy.Field()
    year = scrapy.Field()
    batch = scrapy.Field()
    average = scrapy.Field()
    max = scrapy.Field()


class SchoolLineItem(scrapy.Item):
    # icon = scrapy.Field()
    school = scrapy.Field()
    province = scrapy.Field()
    type = scrapy.Field()
    year = scrapy.Field()
    min = scrapy.Field()
    max = scrapy.Field()
    average = scrapy.Field()
    count = scrapy.Field()
    batch = scrapy.Field()
