"""
Useful base class for all the validators.
"""
import time

from twisted.internet.error import (
    TimeoutError, TCPTimedOutError)

# from logger import crawler_logger
from ..items import (
    ProxyScoreItem, ProxyVerifiedTimeItem,
    ProxySpeedItem)
from loguru import logger



class BaseValidator:
    """base validator for all the validators"""
    name = 'base'
    init_score = 5
    # slow down each spider
    custom_settings = {
        'CONCURRENT_REQUESTS': 50,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 50,
        'RETRY_ENABLED': False,
        'DOWNLOADER_MIDDLEWARES': {
            'haipproxy.crawler.middlewares.RequestStartProfileMiddleware': 500,
            'haipproxy.crawler.middlewares.RequestEndProfileMiddleware': 500,
            'haipproxy.crawler.middlewares.UserAgentMiddleware': 543
        },
        'ITEM_PIPELINES': {
            'haipproxy.crawler.pipelines.ProxyCommonPipeline': 200,
        }

    }
    use_set = True
    success_key = ''
    # all the children validators must specify the following args
    # unless you overwrite the set_item_queue() method
    urls = None
    task_queue = None
    score_queue = None
    ttl_queue = None
    speed_queue = None
    ok_num = 0

    def parse(self, response):
        logger.debug(f"spider name:{self.name}")
        # logger.debug(response.text)
        proxy = response.meta.get('proxy')
        speed = response.meta.get('speed')
        url = response.url
        transparent = self.is_transparent(response)
        if transparent:
            return
        incr = 1 if self.is_ok(response) else '-inf'
        items = self.set_item_queue(url, proxy, self.init_score, incr, speed)
        for item in items:
            yield item

    def is_transparent(self, response):
        return False

    def parse_error(self, failure):
        request = failure.request
        proxy = request.meta.get('proxy')
        # crawler_logger.error('proxy {} has failed, {} is raised'.format(proxy, failure))
        # logger.debug('proxy {} has been failed,{} is raised'.format(proxy, failure))
        if failure.check(TimeoutError, TCPTimedOutError):
            decr = -1
        else:
            decr = '-inf'

        items = self.set_item_queue(request.url, proxy, self.init_score, decr)
        for item in items:
            yield item

    def is_ok(self, response):
        result = self.success_key in response.text
        if result:
            self.ok_num += 1
        logger.debug(f"is_ok: {result}, 累计ok_num：{self.ok_num}")
        return result

    def set_item_queue(self, url, proxy, score, incr, speed=0):
        score_item = ProxyScoreItem(url=proxy, score=score, incr=incr)
        ttl_item = ProxyVerifiedTimeItem(url=proxy, verified_time=int(time.time()), incr=incr)
        speed_item = ProxySpeedItem(url=proxy, response_time=speed, incr=incr)
        score_item['queue'] = self.score_queue
        ttl_item['queue'] = self.ttl_queue
        speed_item['queue'] = self.speed_queue

        return score_item, ttl_item, speed_item
