import scrapy
import urllib
import re

from wzry.items import ZeroItem


class ZeroimagesSpider(scrapy.Spider):
    name = 'zeroImages'
    #域名限制
    allowed_domains = ['qq.com']
    #起始url地址
    start_urls = ['https://pvp.qq.com/web201605/herolist.shtml']

    #首页获取所有英雄的名称，和详情url
    def parse(self, response):
        li_list = response.xpath("//ul[@class='herolist clearfix']/li")
        for li in li_list:
            item = ZeroItem()
            item["name"] = li.xpath(".//a/text()").extract_first()
            item["detail_href"] = li.xpath(".//a/@href").extract_first()
            item["detail_href"] = urllib.parse.urljoin(response.url, item["detail_href"])
            yield scrapy.Request(
                item["detail_href"],
                callback=self.parse_detail,
                meta={"item": item}
            )

    #详情页获取图片URL
    def parse_detail(self, response):
        item = response.meta["item"]
        item['image_url'] = response.xpath(
            "//div[@class='zk-con1 zk-con']/@style").extract_first()
        item['image_url'] = 'http:'+re.search("(?<=url\(').*?(?=')", item['image_url']).group()
        yield item
