# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

from pictures.items import ZiLiao6Item


class Ziliao6Spider(scrapy.Spider):
    name = 'ziliao6'
    allowed_domains = ['www.ziliao6.com']
    start_urls = ['http://www.ziliao6.com/picture/']

    def start_requests(self):
        splash_args = {'wait': 5}
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, endpoint='render.html', args=splash_args)

    def parse(self, response):
        pictures = response.css('.jigsaw .item')
        for pic in pictures:
            url = pic.css('img::attr(data-realurl)').extract_first()
            title = pic.css('img::attr(alt)').extract_first()

            item = ZiLiao6Item()
            for field in item.fields:
                try:
                    item[field] = eval(field)
                except NameError:
                    self.logger.debug('Field is not Defined' + field)
            yield item
