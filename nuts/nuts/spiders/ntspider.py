from scrapy.spider			import BaseSpider
from scrapy.selector		import HtmlXPathSelector
from nuts.items			import NutsItem 
from scrapy.http			import Request
import re

class MySpider(BaseSpider):
	name			= "nettuts"
	allowed_domains	= ["news.baidu.com"]
	start_urls		= ["http://news.baidu.com/"]

	def parse(self, response):
		hxs				= HtmlXPathSelector(response)
		links			= hxs.select("//a/@href").extract()
#
#		#We stored already crawled links in this list
#		crawledLinks	= []
#
#		#Pattern to check proper link
#		linkPattern		= re.compile("^(?:ftp|http|https):\/\/(?:[\w\.\-\+]+:{0,1}[\w\.\-\+]*@)?(?:[a-z0-9\-\.]+)(?::[0-9]+)?(?:\/|\/(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+)|\?(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+))?$")
#
#		for link in links:
#			# If it is a proper link and is not checked yet, yield it to the Spider
#			if linkPattern.match(link) and not link in crawledLinks:
#				crawledLinks.append(link)
#				yield Request(link, self.parse)

		titles	= hxs.select('//li[@class="bold-item"]/a/text()').extract()
		for title in titles:
			item			= NutsItem()
			item["title"]	= title
			print 'title', title
			yield item
