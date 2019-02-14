# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import MyspiderItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = (
        "http://www.dy100.me/",
    )

    def parse(self, response):
        items = []
        print("打印结果:",response.xpath(
            '//*[@id="post_container"]/li[1]/div[2]/h2/a/text()'
        ).extract_first())


        print(response.xpath('//*[@id="post_container"]'))
        for foo in response.xpath('//*[@id="post_container"]/li'):
            print("foo:",foo.xpath('div[1]/a/@href').extract_first())

        return items

