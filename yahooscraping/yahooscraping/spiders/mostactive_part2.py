import scrapy
import csv
import mysql.connector
# Import the ItemObjects
from ..items import YahooscrapingItem

class MostactiveSpider(scrapy.Spider):
    name = 'mostactive_part2'

    # host = 'localhost'
    # user = 'root'
    # password = ''
    # db = 'stockathon'

    def __init__(self):
        self.connection = mysql.connector.connect(host = 'localhost', user = 'root', password = '', db = 'stockathon',use_unicode=True, charset="utf8")
        self.cursor = self.connection.cursor()

    def insert(self, query,params):
        try:
            self.cursor.execute(query,params)
            self.connection.commit()
        except Exception as ex:
            self.connection.rollback()


    def __del__(self):
        self.connection.close()

    def start_requests(self):
        urls = ['https://finance.yahoo.com/most-active/']  # Most active Stocks start URL
        for url in urls:
            yield scrapy.Request(url=url, callback=self.get_stocks)

    def get_stocks(self, response):
        # Get all the stock symbols
        with open(r'C:\Users\Jitesh\Downloads\UsStock.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            for i, row in enumerate(reader):
                if i == 0: continue #skip header row
                yield scrapy.Request(url=f'https://finance.yahoo.com/quote/{row[0]}?p={row[0]}', callback=self.parse)

                # stocks = response.xpath('//*[@id="scr-res-table"]/div[1]/table/tbody//tr/td[1]/a').css('::text').extract()
        # for stock in stocks:
            # Follow the link to the stock details page.
            

    def parse(self, response):
        #Declare the item objects
        items = YahooscrapingItem()
        #Save the extracted data in the item objects
        items['stock_name'] = response.xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1').css('::text').get()
        items['intraday_price'] = response.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]').css('::text').get()
        items['price_change'] = response.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[2]').css('::text').get()

        yield items


        
