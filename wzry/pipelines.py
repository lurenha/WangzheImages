# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import re
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from wzry.settings import IMAGES_STORE as images_store


class WzryPipeline(ImagesPipeline):
    # 配置下载图片的url
    def get_media_requests(self, item, info):
        image_url = item['image_url']
        return [scrapy.Request(re.sub("\d(?=.jpg)", str(i), image_url)) for i in range(1, 10)]

    # 设置下载到本地的文件name
    def item_completed(self, results, item, info):
        image_path = [x["path"] for ok, x in results if ok]
        print(image_path)
        for index in range(len(image_path)):
            os.rename(images_store + image_path[index], images_store + item["name"]+"-"+ str(index+1)+ ".jpg")
        return item
