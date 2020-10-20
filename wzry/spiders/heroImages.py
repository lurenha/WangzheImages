import scrapy
import json
import re
from wzry.items import HeroItem


class HeroimagesSpider(scrapy.Spider):
    name = 'heroImages'
    allowed_domains = ['qq.com']
    start_urls = ['https://pvp.qq.com/web201605/js/herolist.json']

    # 根据Json文件构造url地址
    # 可构造图片请求链接如下
    # https://game.gtimg.cn/images/yxzj/img201606/heroimg/{ename}/{ename}-bigskin-{x}.jpg
    def parse(self, response):
        tar = "https://game.gtimg.cn/images/yxzj/img201606/heroimg/{ename}/{ename}-bigskin-{x}.jpg"
        data_list = json.loads(response.text)
        print(data_list)
        for data in data_list:
            cname = data["cname"]
            ename = data["ename"]
            skin_list_name = data["skin_name"].split('|')
            skin_list_name.insert(0, "默认")
            for i in range(len(skin_list_name)):
                item = HeroItem()
                item["name"] = cname +"-"+ skin_list_name[i]
                tem = re.sub("{ename}", str(ename), tar)
                item["image_url"] = re.sub("{x}", str(i + 1), tem)
                yield item
