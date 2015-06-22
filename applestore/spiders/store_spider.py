import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule 
from scrapy.contrib.linkextractors import LinkExtractor
from applestore.items import ApplestoreItem 
from scrapy.selector import Selector 

class iSpider(CrawlSpider):
	"""docstring for StoreSpider"""
	name = "iSpider"
	allowed_domains = ["apple.com"]
	start_urls = [
			"https://itunes.apple.com/us/genre/ios-education/id6017?mt=8"
	]

	def parse_item(self,response):
		self.log('A response just arrived' % response.url)
		hxs = HtmlXPathSelector(response)
		items = hxs.select('/html/body/main/content/padder/selectedgenre/selectedcontent/ul')
		scraped_items = []
	
		for item in items:
			scraped_item = ApplestoreItem
			scraped_item["title"] = item.select('li/a/text()').extract()
			scraped_item["app_url"] = item.select()
			scraped_items.append(scraped_item)
			return (items)

		filename = outfile
		with open(filename,'w') as f:
			f.write(scraped_items) 
