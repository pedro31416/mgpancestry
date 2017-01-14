import scrapy
from mgpspider.items import ScholarItem


class MgpSpider(scrapy.Spider):
  name = "ancestryspider"

  def __init__(self, root='202169', *args, **kargs):
    super(MgpSpider, self).__init__(*args, **kargs)
    self.start_urls = [
        'https://www.genealogy.math.ndsu.nodak.edu/id.php?id=' + root
      ]

  def url_to_id(self, url):
    tokens = url.split('=')
    if len(tokens) != 2:
      return None
    else:
      return int(tokens[1])

  def parse(self, response):
    item = ScholarItem()
    item['name'] = response.css('h2::text').extract_first().strip()
    item['id'] = self.url_to_id(response.url)
    children_urls = response.css('table').re('id\.php\?id=\d*')
    item['children'] = [self.url_to_id(url) for url in children_urls]
    yield item

    for href in response.xpath('//div[@id="mainContent"]').re('id\.php\?id=\d*'):
          if href not in children_urls:
            yield scrapy.Request(response.urljoin(href), callback=self.parse)
