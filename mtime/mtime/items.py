# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MtimeItem(scrapy.Item):
    rank = scrapy.Field()
    name = scrapy.Field()
    direct = scrapy.Field()
    role = scrapy.Field()
    type = scrapy.Field()
    describe = scrapy.Field()
    point = scrapy.Field()
    pointnum = scrapy.Field()
