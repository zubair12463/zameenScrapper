# pakages
import scrapy
from scrapy.crawler import CrawlerProcess
import json
import urllib
from scrapy.selector import Selector

# Scrapy Class
class Zameen(scrapy.Spider):
    # name
    name = 'zameen'
    # Url
    base_url = 'https://www.zameen.com/Homes/Karachi-2-4.html'
    # Custom Headers
    Headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    # Custome Settings
    custom_settings = {
        'LOG_LEVEL': 'ERROR',
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'zameen4.csv'
    }
    curent_page = 1
    # Scrapy Request Method
    def start_requests(self):
        # Request for base Url
        yield scrapy.Request(url=self.base_url, headers=self.Headers, callback=self.parse_listing)
        
    # Scrapy Response Method
    def parse_listing(self,res):


        # data = ''.join([i.get() for i in res.css('script::text') if 'window.state =' in i.get()])
        # data = data.split('window.state =')[-1]
        # print(data.encode('utf-8').decode('utf-8'))
        data = [i.get() for i in res.css('script::text')]
        print(data[-2])
        with open('aab.txt', 'w',encoding='utf-8') as f:
            f.write(data[-2])
            
        # data = json.loads(data)
        # print(json.dumps(data, indent=2))
        # getting all listings URLS
        
        # listings_URL = res.xpath("//div[@class='f74e80f3']/a/@href").getall()
        # # loop over all urls
        # for url in listings_URL:
        #     url = 'https://www.zameen.com/' + url
        #     yield scrapy.Request(url=url, headers=self.Headers,callback=self.parse)
        #     break

        # Handle Pagination
        # Next_page_url = res.xpath("//li/a[@title = 'Next']/@href").get()
        # if Next_page_url:
        #     self.curent_page += 1
        #     print('Scraping Page ',self.curent_page)
        #     Next_page_url = 'https://www.zameen.com/' + Next_page_url
        #     yield scrapy.Request(url=Next_page_url,headers=self.Headers,callback=self.parse_listing)
        # else:
        #     self.curent_page = 1
        #     pass

    # Scrapy Response Method For Data Extarction
    def parse(self,res):
        # For Debuging Purpose
        # content = ''
        # with open('response.html','r',encoding='utf-8') as f:
        #     for line in f.read():
        #         content += line
        # res = Selector(text=content)

        ''''
        # Data Extraction
        features = {
            # 'URL': res.url,
            # 'ID': res.url.split('-')[1],
            'Title': res.xpath("//h1[@class='_64bb5b3b']/text()").get(),
            'Adress': res.xpath("//div[@class = 'cbcd1b2b']/text()").get(),
            'Built_in_Year': ''.join([i.replace('Built in year','').replace(':','').strip() for i in res.xpath
                            ("//span[@class = '_17984a2c' and contains(text(),'Built in year')]/text()")
                            .getall()]),
            'Floors': ''.join([i.replace('Floors','').replace(':','').strip() for i in res.xpath
                        ("//span[@class='_17984a2c' and contains(text(),'Floors')]/text()")
                        .getall()]),
            "Type": "",
            "Price": "",
            "Location": "",
            "Bath(s)": "",
            "Area": "",
            "Purpose": "",
            "Bedroom(s)": "",
            "Added": "",            
            'img_URLS': [i for i in res.xpath("//picture[@class='_219b7e0a']/img/@src").getall() if '120x90' not in i]          
        }
        

        # Getting All Details
        Detail_Keys = res.xpath("//span[@class = '_3af7fa95']/text()").getall() 
        Detail_Values = res.css('span[class = "_812aa185"] *::text').getall()
        New_Detail_Values = []
        for i in Detail_Values:
            if i == 'PKR':
                continue
            else:
                New_Detail_Values.append(i)
        for key, value in zip(Detail_Keys, New_Detail_Values):
            features[key] = value
'''
        # print(json.dumps(features, indent=2))
        # data = ''.join([i.get() for i in res.css('script::text') if 'window.state =' in i.get()])
        
        # data = data.split('window.state =')[-1]
        # print(res._text)
        # data = json.loads(data)
        # print(json.dumps(data, indent=2))
        
        # yield features



# Main Driver
if __name__ == '__main__':
    # Run Spider
    process = CrawlerProcess()
    process.crawl(Zameen)
    process.start()

    # Zameen.parse_listing(Zameen, '')