import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_splash import SplashRequest
from myScrapy.items import WebcrawlerItem
import json
from pprint import pprint


class StockSpider(scrapy.Spider):
    name = 'stocks'
    start_urls = ['https://rahavard365.com/stock/']
    raw_url = ['https://rahavard365.com/']
    # start_urls = ['https://rahavard365.com/asset/772/آبادا']
    allowed_domains = ['hr.tencent.com', 'rahavard365.com']

    rules = [Rule(LinkExtractor(allow=''), callback='parse_for_url', follow=True)]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse,
                                endpoint='render.html')


    def parse(self, response):
        x = response.xpath("//span[@class='companybuyvolume volume']/text()").extract()
        print(x)
        all_rows = response.xpath("//tbody/tr").extract()
        count = 0

        all_the_market = response.xpath("//tbody/tr").extract()   #successful
        # print(len(all_rows))

        while count < 20:
            count += 1
            webCrawler = WebcrawlerItem()

            webCrawler['symbol'] = response.xpath("//tbody/tr[{}]/td[1]/div/div/a[@class=\'symbol\']/text()".format(count)).extract()
            webCrawler['market'] = response.xpath("//tbody/tr[{}]/td[2]/text()".format(count)).extract()
            webCrawler['dateOfTransaction'] = response.xpath("//tbody/tr[{}]/td[3]/text()".format(count)).extract()
            webCrawler['lastPrice'] = response.xpath("//tbody/tr[{}]/td[4]/span/text()".format(count)).extract()

            webCrawler['change'] = response.xpath("//tbody/tr[{}]/td[5]/span/text()".format(count)).extract()
            webCrawler['percentChange'] = response.xpath("//tbody/tr[{}]/td[6]/span[@dir=\'ltr\']/text()".format(count)).extract()
            webCrawler['volume'] = response.xpath("//tbody/tr[{}]/td[7]/span/text()".format(count)).extract()
            webCrawler['value'] = response.xpath("//tbody/tr[{}]/td[8]/span/text()".format(count)).extract()

            webCrawler['open'] = response.xpath("//tbody/tr[{}]/td[9]/span/text()".format(count)).extract()
            webCrawler['theMost'] = response.xpath("//tbody/tr[{}]/td[10]/span/text()".format(count)).extract()
            webCrawler['theLeast'] = response.xpath("//tbody/tr[{}]/td[11]/span/text()".format(count)).extract()
            webCrawler['numberOfDemands'] = response.xpath("//tbody/tr[{}]/td[12]/span/text()".format(count)).extract()

            webCrawler['demandPrice'] = response.xpath("//tbody/tr[{}]/td[13]/span/text()".format(count)).extract()
            webCrawler['supplyPrice'] = response.xpath("//tbody/tr[{}]/td[14]/span/text()".format(count)).extract()
            webCrawler['supplyCount'] = response.xpath("//tbody/tr[{}]/td[15]/span/text()".format(count)).extract()

            symbol_url = self.raw_url[0] + response.xpath(".//tbody/tr[{}]/td[1]/div/div/a[1]/@href".format(count)).extract_first()
            print(symbol_url)
            yield scrapy.Request(symbol_url, callback=self.parse_symbol, encoding='utf-8')



    def parse_symbol(self, response):
        print('Goooooooooooo')

        compayVolume = response.xpath("//span[@class='companybuyvolume volume']").extract_first()
        personVolume = response.xpath("//span[@class='personbuyvolume volume']").extract()
        print(compayVolume)
        print(personVolume)



