# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor

from scrapy_splash import SplashRequest


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["www.expedia.co.uk"]
    start_urls = ['https://www.expedia.co.uk/Marrakech-Hotels-Riad-Khadija-Spa.h17759812.Hotel-Information?adults=2&children=0&chkin=15%2F06%2F2019&chkout=16%2F06%2F2019/']

    # http_user = 'splash-user'
    # http_pass = 'splash-password'

    def parse(self, response):
        le = LinkExtractor()
        for link in le.extract_links(response):
            yield SplashRequest(
                link.url,
                self.parse_link,
                endpoint='render.json',
                args={
                    'har': 1,
                    'html': 1,
                }
            )

    def parse_link(self, response):
        print("PARSED", response.real_url, response.url)
        print(response.css("title").extract())
        print(response.data["har"]["log"]["pages"])
        print(response.headers.get('Content-Type'))
# import scrapy


# class ExpediaSpider(scrapy.Spider):
#     name = 'expedia'
#     allowed_domains = ['www.expedia.co.uk']
#     start_urls = ['http://https://www.expedia.co.uk/Marrakech-Hotels-Riad-Khadija-Spa.h17759812.Hotel-Information?adults=2&children=0&chkin=15%2F06%2F2019&chkout=16%2F06%2F2019/']

#     def start_requests(self):
#         for url in self.start_urls:
#             yield SplashRequest(url, self.parse, callback=self.parse_captchad, meta={'solve_captcha': True},
#                       errback=self.parse_fail,  endpoint='render.html', args={'wait': 2},
#             )


#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         filename = 'quotes-%s.html' % page
#         with open(filename, 'wb') as f:
#             f.write(response.body)
#         self.log('Saved file %s' % filename)




# yield scrapy.Request(url, self.parse_result, meta={
#     'splash': {
#         'args': {
#             # set rendering arguments here
#             'html': 1,
#             'png': 1,

#             # 'url' is prefilled from request url
#             # 'http_method' is set to 'POST' for POST requests
#             # 'body' is set to request body for POST requests
#         },

#         # optional parameters
#         'endpoint': 'render.json',  # optional; default is render.json
#         'splash_url': '<url>',      # optional; overrides SPLASH_URL
#         'slot_policy': scrapy_splash.SlotPolicy.PER_DOMAIN,
#         'splash_headers': {},       # optional; a dict with headers sent to Splash
#         'dont_process_response': True, # optional, default is False
#         'dont_send_headers': True,  # optional, default is False
#         'magic_response': False,    # optional, default is True
#     }
# })

    # def start_requests(self):
    #     urls = [
    #         'https://www.booking.com/hotel/ae/atana.en-gb.html?checkin=2019-05-28;checkout=2019-05-29',
    #     ]
    #     # headers = scrapy.Request.utils.default_headers()
    #     headers = {
    #         'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    #     }
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse, headers=headers)
    #
    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = 'quotes-%s.html' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Saved file %s' % filename)