from scrapy import Spider


class RedditSpider(Spider):
	name = 'reddit'
	start_urls = ['https://www.reddit.com/']
	def parse(self, response):
		base_url = "https://www.reddit.com"
		post_titles = response.css('h3::text').getall()
		votes = response.css('._1rZYMD_4xY3gRcSS3p8ODO._3a2ZHWaih05DgAOtvu6cIo ::text').extract()
		dates = response.css('._3jOxDPIQ0KaOWpzvSQo-1s::text').getall()

		urls = []
		for u in response.css('a.SQnoC3ObvgnGjWt90zD9Z._2INHSNB8V5eaWp4P0rY_mE'):
			urls.append(u.attrib['href'])


		url = response.css('a.SQnoC3ObvgnGjWt90zD9Z._2INHSNB8V5eaWp4P0rY_mE').attrib['href']    
		# urls = response.css('a.SQnoC3ObvgnGjWt90zD9Z._2INHSNB8V5eaWp4P0rY_mE').getall()

		for p in zip(post_titles, votes, dates, urls):
			yield {
				'title': p[0],
				'vote': p[1],
				'date': p[2],
				'url': base_url + p[3]
			}