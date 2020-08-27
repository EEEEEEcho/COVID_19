# -*- coding: utf-8 -*-
import scrapy
import json
from COVID_19.items import Covid19Item

class Covid19Spider(scrapy.Spider):
    name = 'covid19'
    allowed_domains = ['https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=317249238170']
    start_urls = ['https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=317249238170/']

    def parse(self, response):
        data = json.loads(response.text)
        item = Covid19Item()
        for country in data['data']['areaTree']:
            item['name']= country['name']
            today_dict = country['today']
            total_dict = country['total']

            item['today_confirm'] = today_dict['confirm'] if (today_dict['confirm'] != None) else 0
            item['today_suspect'] = today_dict['suspect'] if (today_dict['suspect'] != None) else 0
            item['today_heal'] = today_dict['heal'] if (today_dict['heal'] != None) else 0
            item['today_dead'] = today_dict['dead'] if (today_dict['dead'] != None) else 0

            item['total_confirm'] = total_dict['confirm'] if (total_dict['confirm'] != None) else 0
            item['total_suspect'] = total_dict['suspect'] if (total_dict['suspect'] != None) else 0
            item['total_heal'] = total_dict['heal'] if (total_dict['heal'] != None) else 0
            item['total_dead'] = total_dict['dead'] if (total_dict['dead'] != None) else 0
            item['now_confirm'] = item['total_confirm'] - item['total_heal'] - item['total_dead']
            yield item
            # print("国家:" + str(name) + ",今日确诊:" + str(today_confirm) + ",今日疑似:" + str(today_suspect) + ",今日治愈:"
            #       + str(today_heal) + ",今日死亡:" + str(today_dead) + ",累计确诊:" + str(total_confirm) + ",累计疑似:" + str(
            #     total_suspect) +
            #       ",累计治愈:" + str(total_heal) + ",累计死亡:" + str(total_dead) + ",现有确诊:" + str(now_confirm))
