# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class MyscrapyItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class WebcrawlerItem(scrapy.Item):
    symbol = scrapy.Field()
    market =scrapy.Field()
    dateOfTransaction =scrapy.Field()
    lastPrice = scrapy.Field()

    change = scrapy.Field()
    percentChange = scrapy.Field()
    volume = scrapy.Field()
    value = scrapy.Field()

    open = scrapy.Field()
    theMost = scrapy.Field()
    theLast = scrapy.Field()
    numberOfRequests = scrapy.Field()

    demandPrice = scrapy.Field()
    supplyPrice = scrapy.Field()
    supplyCount = scrapy.Field()

    legalPurchaseVolume = scrapy.Field()
    actualPurchaseVolume = scrapy.Field()
    eps = scrapy.Field()
    ratio = scrapy.Field()
