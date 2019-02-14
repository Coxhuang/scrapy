# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MyspiderItem(scrapy.Item):
    name = scrapy.Field()  # 电影名
    director = scrapy.Field()  # 导演
    info = scrapy.Field()  # 电影详细信息url
