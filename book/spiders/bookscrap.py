import scrapy


class BookscrapSpider(scrapy.Spider):
    name = "bookscrap"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        BOOkdata= response.css("h3 > a::attr(title)").getall()
        for title in BOOkdata:
            print()
            print()
            print()
            print()
            print(title)
            print() 
            print() 
            print() 

            yield {
            'Title': title
             }
