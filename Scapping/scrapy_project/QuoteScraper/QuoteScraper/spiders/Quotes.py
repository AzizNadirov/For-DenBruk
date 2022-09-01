from scrapy import Spider

"""
Simple quote scraper. Scapes quotes from
'quotes.toscrape.com' web site.
"""

class QuoteSpyder(Spider):
	name = 'quote'
	start_urls = ['https://quotes.toscrape.com/']

	def parse(self, response):
		for q in response.css('div.quote'):
			yield {
			'author': q.css('span small.author::text').get(),
			'text': q.css('span.text::text').get(),
			'author_url': q.css('span a').attrib['href'],
			'tags': q.css('div.tags a.tag::text').getall()
			}

