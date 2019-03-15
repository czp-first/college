# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class CollegePipeline(object):
    def process_item(self, item, spider):
        return item


class MajorLinePipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_uri=crawler.settings.get("MONGO_URI"), mongo_db=crawler.settings.get("MONGO_DB"))

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host=self.mongo_uri, port=27017)
        self.db = self.client[self.mongo_db]
        # self.collection = self.db["gapkao_major_3"]
        self.collection = self.db["gapkao_school_3"]

    def process_item(self, item, spider):
        mongo_item = {
            "school": item["school"][0],
            "province": item["province"][0],
            "type": item["type"][0],
            "year": item["year"][0],
            "min": item["min"][0],
            "max": item["max"][0],
            "average": item["average"][0],
            "count": item["count"][0],
            "batch": item["batch"][0],
        }
        self.collection.insert_one(mongo_item)
        return item

    def close_spider(self, spider):
        self.client.close()
