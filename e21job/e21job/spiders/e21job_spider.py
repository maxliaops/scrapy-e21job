import re
import json

from scrapy.selector import Selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle
from scrapy import log

from e21job.items import *
from e21job.misc.log import *

class E21jobSpider(CrawlSpider):
    name = "e21job"
    allowed_domains = ["job.e21.edu.cn"]
    start_urls = [
        "http://job.e21.edu.cn/stu_more.php?page=0&fenye=yes"
    ]
    rules = [
        Rule(sle(allow=("stu_more.php\?page=\d{,5}&fenye=yes")), follow=True, callback='parse_item')
    ]

    def parse_item(self, response):
        items = []
        sel = Selector(response)
        base_url = get_base_url(response)
        #sites = sel.css('table:nth-child(5)').css('table:nth-child(2)').css('table.black12').css('tr')
        for i in range(1, 50, 2):
            item = GraduateItem()
            query = 'tr:nth-child(%d)' %i
            #print query
            site = sel.css('table:nth-child(5)').css('table:nth-child(2)').css('table.black12').css(query)
            item['name'] = site.css('a').xpath('text()').extract()
            item['school'] = site.css('td:nth-child(2)::text').extract()
            item['specialty'] = site.css('td:nth-child(3)::text').extract()
            item['education'] = site.css('td:nth-child(4)::text').extract()
            items.append(item)
            #print repr(item).decode("unicode-escape") + '\n'

        info('parsed ' + str(response))
        #log.msg(str('parsed ' + str(response)), level=log.INFO)
        return items


    def _process_request(self, request):
        #print request
        info('process ' + str(request))
        # log.msg(str('process ' + str(request)), level=log.INFO)
        return request

