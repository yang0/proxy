"""
Basic proxy ip crawler.
"""
from haipproxy.config.settings import SPIDER_COMMON_TASK
from ..redis_spiders import RedisSpider
from ..items import ProxyUrlItem
from .base import BaseSpider
import re
from loguru import logger

# notice multi inheritance order in python
class CommonSpider(BaseSpider, RedisSpider):
    name = 'common'
    task_queue = SPIDER_COMMON_TASK

    def __init__(self):
        super().__init__()
        self.parser_maps.setdefault('myproxy', self.parse_my_proxy)
        self.parser_maps.setdefault('xroxy', self.parse_xroxy)

    def parse_my_proxy(self, response):
        protocols = None
        if self.exists(response.url, 'socks-4'):
            protocols = ['socks4']
        if self.exists(response.url, 'socks-5'):
            protocols = ['socks5']

        items = list()
        infos = response.css('.list ::text').extract()
        for info in infos:
            if ':' not in info:
                continue
            pos = info.find('#')
            if pos != -1:
                info = info[:info.find('#')]
            ip, port = info.split(':')
            protocols = self.default_protocols if not protocols else protocols
            for protocol in protocols:
                items.append(ProxyUrlItem(url=self.construct_proxy_url(protocol, ip, port)))
        return items


    def parse_xroxy(self, response):
        items = list()
        ip_extract_pattern = '">(.*)\\n'
        infos = response.xpath('//tr').css('.row1') + response.xpath('//tr').css('.row0')

        for info in infos:
            m = re.search(ip_extract_pattern, info.css('a')[0].extract())
            if m:
                ip = m.group(1)
                port = info.css('a::text')[2].extract()
                protocol = info.css('a::text')[3].extract().lower()
                if protocol in ['socks4', 'socks5']:
                    items.append(ProxyUrlItem(url=self.construct_proxy_url(protocol, ip, port)))
                elif protocol == 'transparent':
                    continue
                else:
                    items.append(ProxyUrlItem(url=self.construct_proxy_url('http', ip, port)))
                    is_ssl = info.css('a::text')[4].extract().lower() == 'true'
                    if is_ssl:
                        items.append(ProxyUrlItem(url=self.construct_proxy_url('https', ip, port)))

        return items