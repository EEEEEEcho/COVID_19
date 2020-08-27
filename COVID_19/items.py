# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Covid19Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    today_confirm = scrapy.Field()
    today_suspect = scrapy.Field()
    today_heal = scrapy.Field()
    today_dead = scrapy.Field()
    total_confirm = scrapy.Field()
    total_suspect = scrapy.Field()
    total_heal = scrapy.Field()
    total_dead = scrapy.Field()
    now_confirm = scrapy.Field()