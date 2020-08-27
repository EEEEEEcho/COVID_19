# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class Covid19Pipeline(object):
    def __init__(self):
        self.db = pymysql.connect(host="localhost",user="root",passwd="s814466057",db="covid",charset="utf8",port=3306)
        self.cur = self.db.cursor()
    def process_item(self, item, spider):

        # sql = """
        #     insert into countrys(name,today_confirm,today_suspect,today_heal,today_dead,
        #     total_confirm,total_suspect,total_heal,total_dead,now_confirm)
        #     values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update name=%s,today_confirm=%s,today_suspect=%s,
        #    today_heal=%s,today_dead=%s,total_confirm=%s,total_suspect=%s,
        #    total_heal=%s,total_dead=%s,now_confirm=%s
        #
        # """

        sql = """
            update countrys set name=%s,today_confirm=%s,today_suspect=%s,today_heal=%s,today_dead=%s,
            total_confirm=%s,total_suspect=%s,total_heal=%s,total_dead=%s,now_confirm=%s where name=%s
        """
        # self.cur.execute(sql,(item['name'],item['today_confirm'],item['today_suspect'],item['today_heal'],
        #                        item['today_dead'],item['total_confirm'],item['total_suspect'],
        #                        item['total_heal'],item['total_dead'],item['now_confirm'],item['name'],item['today_confirm'],item['today_suspect'],item['today_heal'],
        #                        item['today_dead'],item['total_confirm'],item['total_suspect'],
        #                        item['total_heal'],item['total_dead'],item['now_confirm']))
        self.cur.execute(sql, (item['name'], item['today_confirm'], item['today_suspect'], item['today_heal'],
                               item['today_dead'], item['total_confirm'], item['total_suspect'],
                               item['total_heal'], item['total_dead'], item['now_confirm'], item['name']))
        self.db.commit()
        print("更新成功")
        return item

    def close_spider(self,spider):
        self.cur.close()
        self.db.close()
