# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScholarItem(scrapy.Item):
    name = scrapy.Field()
    id = scrapy.Field()
    children = scrapy.Field()
