import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
import scrapy


class PwspiderSpider(scrapy.Spider):
    name = "pwspider"
    def start_requests(self):
        yield scrapy.Request("https://shoppable-campain-demo.netlify.app/#/", meta={"playwright": True})
        

    def parse(self, response):
        yield{
            'text': response.text
        }
