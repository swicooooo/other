# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl,pymysql

class DBPipeline:
    def __init__(self) -> None:
        self.conn=pymysql.connect()
        self.cursor=self.conn.cursor()
        self.data=[]

    def close_spider(self,spider):
        self.cursor.executemany('insert into top_movie (title, ranking, subject, duration, intro) values(%s,%s,%s)',self.data)
        self.conn.commit()
        self.conn.close()

    def process_item(self,item):
        title=item.get('title','')
        rank=item.get('rank',0)
        subject=item.get('subject','')
        duration=item.get('duration',0)
        intro=item.get('intro','')
        self.data.append((title,rank,subject,duration,intro))
        return item

class ExcelPipeline:

    def __init__(self):
        self.wb=openpyxl.Workbook()
        self.basic_ws=self.wb.active
        self.basic_ws.title='Top250'
        self.basic_ws.append(['title','rank','subject', 'duration', 'intro'])

    def close_spider(self,spider):
        self.wb.save('./douban_movie.xlsx')

    def process_item(self, item, spider):
        title=item.get('title','')
        rank=item.get('rank',0)
        subject=item.get('subject','')
        duration=item.get('duration',0)
        intro=item.get('intro','')
        self.basic_ws.append((title,rank,subject,duration,intro))
        return item
