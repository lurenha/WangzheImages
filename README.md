# WangzheImages
## 项目介绍
#### 使用scrapy框架爬取王者荣耀英雄图片

1. 创建Scrapy项目
scrapy startproject wzry
1. 生成爬虫
scrapy genspider zeroImages "qq.com"
1. 提取数据
完善spider使用xpath等方法提取图片链接
1. 保存数据
完善pipleline 保存url的图片到本地
