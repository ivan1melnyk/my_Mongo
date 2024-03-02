import json
import scrapy
from scrapy.crawler import CrawlerProcess

def add_json(file_path, new_data):
    # Read existing JSON data from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Append the new data to the existing data
    data.append(new_data)

    # Write the updated data back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

class QuotesSpider(scrapy.Spider):
    name = 'authors'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse_author(self, response):
        author_list = {
            "fullname": response.xpath("//h3[@class='author-title']/text()").get(),
            "born_date": response.xpath("//span[@class='author-born-date']/text()").get(),
            "born_location": response.xpath("//span[@class='author-born-location']/text()").get(),
            "description": response.xpath("//div[@class='author-description']/text()").get()
        }
        add_json('json/authors.json', author_list)

    def parse(self, response):
        for quote in response.xpath("/html//div[@class='quote']"):
            author_resourse = response.urljoin(quote.xpath("span/a/@href").get())
            #print('#@! author_resourse:', type(quote), author_resourse)
            yield scrapy.Request(url=author_resourse, callback=self.parse_author)
            quote_list = {
                "tags": quote.xpath("div[@class='tags']/a/text()").extract(),
                "author": quote.xpath("span/small/text()").extract(),
                "quote": quote.xpath("span[@class='text']/text()").get()
            }
            add_json('json/quotes.json', quote_list)
            yield quote_list
        next_link = response.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=response.urljoin(next_link))

# run spider
process = CrawlerProcess()
process.crawl(QuotesSpider)
process.start()


