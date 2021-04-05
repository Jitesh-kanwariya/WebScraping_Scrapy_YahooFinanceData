# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class YahooscrapingPipeline(object):

    
    # def __init__(self):
    #     self.connection()
    #     self.createTable()

    # def connection(self):
    #     self.conn = sqlite3.connect('mydatabase.db')
    #     self.cursorObj = self.conn.cursor()

    # def createTable(self):
    #     self.cursorObj.execute("DROP TABLE IF EXISTS stock")
    #     self.cursorObj.execute("CREATE TABLE stock(stock_name text , intraday_price text , price_change text)")


    def process_item(self,item,spider):
        
        query="""INSERT INTO stock (stock_name,intraday_price,price_change) VALUES (%s, %s, %s)"""
        params=(item['stock_name'], item['intraday_price'], item['price_change'])
        spider.cursor.execute(query,params)
        
        return item

        
    

    